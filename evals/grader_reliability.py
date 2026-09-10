#!/usr/bin/env python3
"""Grader RELIABILITY harness — is the grader consistent with itself?

Reliability is not validity. A grader can be perfectly consistent and still
wrong (see grader_validity.py for the calibration check against a human gold
set). This harness only answers: if we grade the same response several times,
how much does the score move?

Method
------
1. Freeze a fixture set of (scenario, response) pairs — `grader_fixtures.json`.
   Built once from a real cycle transcript, spanning the score range. Re-freeze
   only when the rubric or grade prompt changes substantially (pass --refreeze).
2. Re-grade every fixture K times with independent `claude -p` calls.
3. Report, per dimension and for the composite:
       mean, SD, min-max swing
   and overall: mean composite SD, and how often the K gradings agree on the
   rank order of the fixtures (Spearman vs the fixture mean).

Writes results/GRADER_RELIABILITY.md.

Usage
-----
    python evals/grader_reliability.py --k 4
    python evals/grader_reliability.py --refreeze --from-cycle <ts>   # rebuild fixtures
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

from run_cycle import DIMS, DIM_NAMES, RUBRIC, claude, grade_prompt, extract_json, composites

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CYCLES = HERE / "results" / "cycles"
FIXTURES = HERE / "grader_fixtures.json"
OUT = HERE / "results" / "GRADER_RELIABILITY.md"


def latest_cycle_file():
    fs = sorted(CYCLES.glob("*.json"))
    return fs[-1] if fs else None


def build_fixtures(from_cycle=None, n=8):
    src = (CYCLES / f"{from_cycle}.json") if from_cycle else latest_cycle_file()
    if not src or not src.exists():
        print("no cycle transcript to build fixtures from — run a cycle first", file=sys.stderr)
        return None
    data = json.loads(src.read_text())
    scored = [r for r in data["rows"] if r.get("response") and "overall" in r]
    if len(scored) < 4:
        print(f"only {len(scored)} usable rows in {src.name}", file=sys.stderr)
        return None
    scored.sort(key=lambda r: r["overall"])
    # even spread across the observed score range
    idx = [round(i * (len(scored) - 1) / (min(n, len(scored)) - 1)) for i in range(min(n, len(scored)))]
    picks = [scored[i] for i in sorted(set(idx))]
    fixtures = [dict(
        fixture_id=f"FX-{k+1:02d}",
        source_cycle=data["ts"],
        scenario_id=r["scenario_id"],
        scenario={kk: r.get(kk) for kk in
                  ("scenario_id", "family", "environment", "revl_phase", "goal",
                   "training_age", "recovery_context", "constraint", "pt_frequency")},
        prompt_fields_note="re-grading uses the stored response; scenario meta is for the grader prompt",
        response=r["response"],
        original_overall=r["overall"],
    ) for k, r in enumerate(picks)]
    FIXTURES.write_text(json.dumps(dict(
        built_from=src.name, rubric_sha=_rubric_sha(), n=len(fixtures), fixtures=fixtures), indent=1))
    print(f"froze {len(fixtures)} fixtures -> {FIXTURES.name} (overall "
          f"{fixtures[0]['original_overall']:.2f}..{fixtures[-1]['original_overall']:.2f})", file=sys.stderr)
    return json.loads(FIXTURES.read_text())


def _rubric_sha():
    import hashlib
    return hashlib.sha256(RUBRIC.read_text().encode()).hexdigest()[:12]


def _mini_scenario(fx):
    # a lean scenario dict the grade prompt can consume
    s = dict(fx["scenario"])
    s["id"] = fx["scenario_id"]
    s["prompt"] = "(original client message — see transcript; response graded on its merits)"
    s["expected_priorities"] = []
    s["traps"] = []
    s["must_not"] = []
    return s


def spearman(a, b):
    n = len(a)
    if n < 3:
        return None
    ra = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: a[i]))}
    rb = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: b[i]))}
    d2 = sum((ra[i] - rb[i]) ** 2 for i in range(n))
    return round(1 - 6 * d2 / (n * (n * n - 1)), 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=4, help="re-gradings per fixture")
    ap.add_argument("--refreeze", action="store_true")
    ap.add_argument("--from-cycle", default=None)
    ap.add_argument("--n-fixtures", type=int, default=8)
    ap.add_argument("--grade-timeout", type=int, default=240)
    args = ap.parse_args()

    if args.refreeze or not FIXTURES.exists():
        fx = build_fixtures(args.from_cycle, args.n_fixtures)
        if not fx:
            return 1
    fxdata = json.loads(FIXTURES.read_text())
    if fxdata.get("rubric_sha") != _rubric_sha():
        print("WARNING: rubric has changed since fixtures were frozen — "
              "re-run with --refreeze for a valid reliability read.", file=sys.stderr)

    rubric = RUBRIC.read_text()
    per_fixture = []
    for fx in fxdata["fixtures"]:
        s = _mini_scenario(fx)
        gradings = []
        for i in range(args.k):
            graw, _ = claude(grade_prompt(s, fx["response"], rubric), args.grade_timeout, REPO,
                             allowed=["Read"])
            g = extract_json(graw)
            if g and "scores" in g:
                sc = {d: int(g["scores"].get(d, 0)) for d in DIMS if d in g.get("scores", {})}
                gradings.append(dict(scores=sc, overall=composites(sc)["overall"],
                                     hard=g.get("hard_failures", [])))
            print(f"  {fx['fixture_id']} grading {i+1}/{args.k}"
                  f"{' ok' if g else ' FAILED'}", file=sys.stderr)
        if len(gradings) < 2:
            per_fixture.append(dict(fixture_id=fx["fixture_id"], error="too few valid gradings"))
            continue
        overalls = [gr["overall"] for gr in gradings]
        dim_sd = {}
        for d in DIMS:
            vals = [gr["scores"].get(d) for gr in gradings if d in gr["scores"]]
            if len(vals) >= 2:
                dim_sd[d] = round(statistics.pstdev(vals), 3)
        per_fixture.append(dict(
            fixture_id=fx["fixture_id"], scenario_id=fx["scenario_id"],
            k=len(gradings),
            overall_mean=round(statistics.mean(overalls), 3),
            overall_sd=round(statistics.pstdev(overalls), 3),
            overall_swing=round(max(overalls) - min(overalls), 3),
            dim_sd=dim_sd,
            hard_failure_agreement=round(
                sum(1 for gr in gradings if bool(gr["hard"])) / len(gradings), 2),
        ))

    ok = [f for f in per_fixture if "overall_mean" in f]
    lines = ["# Grader reliability (self-consistency)\n",
             f"_K = {args.k} independent re-gradings of {len(fxdata['fixtures'])} frozen fixtures "
             f"(rubric `{fxdata.get('rubric_sha')}`). Reliability ≠ validity — see GRADER_VALIDITY.md._\n"]
    if ok:
        mean_overall_sd = statistics.mean(f["overall_sd"] for f in ok)
        worst = max(ok, key=lambda f: f["overall_sd"])
        lines += [f"- **Mean composite SD across fixtures: {mean_overall_sd:.3f}** "
                  f"(rule of thumb: < 0.15 is usable, < 0.10 is good)",
                  f"- Worst fixture: {worst['fixture_id']} SD {worst['overall_sd']:.3f}, "
                  f"swing {worst['overall_swing']:.2f}",
                  ""]
        means = [f["overall_mean"] for f in ok]
        lines += ["| Fixture | Scenario | k | mean | SD | swing | HF agree |",
                  "|---|---|--:|--:|--:|--:|--:|"]
        for f in ok:
            lines.append(f"| {f['fixture_id']} | {f['scenario_id']} | {f['k']} | "
                         f"{f['overall_mean']:.2f} | {f['overall_sd']:.3f} | "
                         f"{f['overall_swing']:.2f} | {f['hard_failure_agreement']:.2f} |")
        # noisiest dimensions
        dim_all = {d: [] for d in DIMS}
        for f in ok:
            for d, v in f["dim_sd"].items():
                dim_all[d].append(v)
        lines += ["\n## Noisiest dimensions (mean SD over fixtures)\n", "| Dim | Name | mean SD |", "|---|---|--:|"]
        for v, d in sorted(((statistics.mean(x), d) for d, x in dim_all.items() if x), reverse=True)[:6]:
            lines.append(f"| {d} | {DIM_NAMES[d]} | {v:.3f} |")
    else:
        lines.append("_No fixture produced ≥2 valid gradings._")

    OUT.write_text("\n".join(lines) + "\n")
    print(f"\nwrote {OUT.relative_to(REPO)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
