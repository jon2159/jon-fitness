#!/usr/bin/env python3
"""jon-fitness skill optimization loop — analyse the evaluation history, and
(optionally, guarded) apply and regression-test one targeted improvement.

The philosophy (evals/README.md): never optimise on one scenario. A change is
only kept if it improves a *recurring* weakness across a meaningful set of
scenarios AND does not regress the permanent benchmark suite.

Modes
-----
  analyse   (default) — read results/history.jsonl, cluster failures, write
                        results/PROPOSALS.md. Changes nothing. Safe to run nightly.

  apply     — take the single highest-confidence proposal that meets the bar
              (recurring >= --min-cycles cycles, >= --min-hits scenario hits,
              one clear failure_category, one named target file), ask a fresh
              Claude to draft the minimal edit, apply it, then:
                1. run  run_cycle.py --benchmark-only   (regression baseline vs. last)
                2. run  run_cycle.py --n <sample> on scenarios in the affected
                   family/category (targeted improvement check)
              Keep the edit only if benchmark overall does not drop by > --tol
              AND the targeted sample improves by >= --gain. Otherwise git-revert
              the edit. Always commit the results; commit the skill edit only if kept.

Usage
-----
    python evals/optimize.py                       # analyse only
    python evals/optimize.py --apply               # guarded apply + regression
    python evals/optimize.py --apply --dry-run     # show what apply would do
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
HISTORY = HERE / "results" / "history.jsonl"
PROPOSALS = HERE / "results" / "PROPOSALS.md"
CYCLES = HERE / "results" / "cycles"

DIM_NAMES = {
    "A": "goal_alignment", "B": "training_specificity", "C": "total_training_load",
    "D": "volume_management", "E": "intensity_management", "F": "frequency_management",
    "G": "fatigue_management", "H": "recovery_compatibility", "I": "exercise_selection",
    "J": "progression", "K": "individualisation", "L": "practicality",
    "M": "long_term_coherence", "N": "safety_caution", "O": "communication",
}
TARGET_FILES = [
    ".claude/skills/jon-fitness/SKILL.md",
    ".claude/skills/jon-fitness/references/COURSE_MAP.md",
    ".claude/skills/jon-fitness/references/programming-reference.md",
    ".claude/skills/jon-fitness/references/intake-questions.md",
    ".claude/skills/jon-fitness/references/revl-class-integration.md",
    ".claude/skills/jon-fitness/references/russian-strength-program.md",
]


def rows():
    if not HISTORY.exists():
        return []
    return [json.loads(l) for l in HISTORY.read_text().splitlines() if l.strip() and '"overall"' in l]


def claude(prompt, timeout=300, allowed=None):
    cmd = ["claude", "-p", prompt, "--permission-mode", "bypassPermissions"]
    if allowed:
        cmd += ["--allowed-tools", ",".join(allowed)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=str(REPO))
    return (r.stdout.strip(), "" if r.returncode == 0 else r.stderr.strip()[:300])


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=str(REPO))


# ---------------------------------------------------------------- analysis

def analyse():
    R = rows()
    if len(R) < 8:
        PROPOSALS.write_text(f"# jon-fitness optimization proposals\n\n"
                             f"_Only {len(R)} scored runs so far — need at least ~8 before "
                             f"clustering failures. Run more cycles._\n")
        print(f"only {len(R)} runs; nothing to propose yet")
        return []

    cycles = sorted({r["cycle"] for r in R})
    recent = [r for r in R if r["cycle"] >= cycles[-min(6, len(cycles))]]

    # weakest dimensions in recent data
    dim = {d: [] for d in DIM_NAMES}
    for r in recent:
        for d, v in r.get("scores", {}).items():
            dim[d].append(v)
    weak = sorted(((statistics.mean(v), d) for d, v in dim.items() if v))[:5]

    # failure categories, weighted by how many cycles they appear in
    cat_cycles = defaultdict(set)
    cat_hits = Counter()
    cat_examples = defaultdict(list)
    for r in recent:
        fc = r.get("failure_category")
        if fc and fc != "none":
            cat_cycles[fc].add(r["cycle"])
            cat_hits[fc] += 1
            if len(cat_examples[fc]) < 4:
                cat_examples[fc].append(r["scenario_id"])

    trap = Counter(t for r in recent for t in r.get("traps_fallen_into", []))
    recs = Counter(r.get("recommended_improvement", "").strip()
                   for r in recent
                   if r.get("recommended_improvement", "").strip().lower() not in ("", "none"))

    # which target file each failing scenario family points at
    fam_cat = Counter((r.get("family"), r.get("failure_category")) for r in recent
                      if r.get("failure_category") not in (None, "none"))

    proposals = []
    for fc, cyset in sorted(cat_cycles.items(), key=lambda kv: (-len(kv[1]), -cat_hits[kv[0]])):
        proposals.append(dict(
            failure_category=fc,
            recurring_cycles=sorted(cyset),
            scenario_hits=cat_hits[fc],
            example_scenarios=cat_examples[fc],
            related_traps=[t for t, _ in trap.most_common(20)
                           if any(t in r.get("traps_fallen_into", []) for r in recent
                                  if r.get("failure_category") == fc)][:3],
            grader_suggestions=[s for s, _ in recs.most_common(50)][:3],
        ))

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    L = [f"# jon-fitness optimization proposals\n",
         f"_Generated {ts} from {len(R)} scored runs across cycles {cycles[0]}–{cycles[-1]} "
         f"(clustering the last {len(set(r['cycle'] for r in recent))} cycles)._\n",
         "## Weakest dimensions (recent)\n", "| Dim | Name | Mean |", "|---|---|--:|"]
    for mean, d in weak:
        L.append(f"| {d} | {DIM_NAMES[d]} | {mean:.2f} |")

    L += ["\n## Candidate improvements\n",
          "A proposal qualifies for guarded auto-apply when it recurs across **≥3 cycles** "
          "with **≥6 scenario hits** and points at one failure category. Others are for human review.\n"]
    for i, p in enumerate(proposals, 1):
        qualifies = len(p["recurring_cycles"]) >= 3 and p["scenario_hits"] >= 6
        L += [f"### P{i} — `{p['failure_category']}`  "
              f"{'✅ auto-apply candidate' if qualifies else '👤 human review'}\n",
              f"- Recurs in cycles: {p['recurring_cycles']}",
              f"- Scenario hits (recent): {p['scenario_hits']}",
              f"- Examples: {', '.join(p['example_scenarios'])}",
              f"- Related traps: " + ("; ".join(p['related_traps']) or "—"),
              "- Grader-suggested fixes:"]
        for g in p["grader_suggestions"]:
            L.append(f"    - {g}")
        L.append("")

    PROPOSALS.write_text("\n".join(L) + "\n")
    print(f"wrote {PROPOSALS.relative_to(REPO)} — {len(proposals)} candidate(s)")
    return proposals


# ---------------------------------------------------------------- guarded apply

def apply(min_cycles, min_hits, sample, gain, tol, dry):
    props = analyse()
    cand = [p for p in props
            if len(p["recurring_cycles"]) >= min_cycles and p["scenario_hits"] >= min_hits]
    if not cand:
        print("no proposal meets the auto-apply bar; analyse-only output written")
        return 0
    p = cand[0]
    print(f"auto-apply candidate: {p['failure_category']} "
          f"(cycles {p['recurring_cycles']}, {p['scenario_hits']} hits)")

    if git("diff", "--quiet").returncode != 0 or git("diff", "--cached", "--quiet").returncode != 0:
        print("working tree dirty — refusing to auto-apply. Commit or stash first.")
        return 1

    edit_prompt = f"""You maintain the `jon-fitness` skill. Its nightly evaluation shows a RECURRING
weakness, failure category **{p['failure_category']}**, across cycles {p['recurring_cycles']}
({p['scenario_hits']} scenario hits recently).

Related traps the skill fell into:
{chr(10).join('- ' + t for t in p['related_traps']) or '- (none captured)'}

Grader-suggested fixes:
{chr(10).join('- ' + g for g in p['grader_suggestions']) or '- (none)'}

Make the SMALLEST targeted edit to ONE of these files that would address this category:
{chr(10).join('- ' + f for f in TARGET_FILES)}

Rules:
- One file. A few lines. Do not restructure.
- Do not weaken any existing safety, scope, or evidence-labelling instruction.
- Do not touch russian-strength-program.md unless the failure is specifically about the
  Russian protocols' own methodology.
- After editing, print exactly one line: `EDITED <path> — <one-sentence rationale>`

If no small edit would help (the failure is in the scenarios or the grader, not the skill),
change nothing and print `NO-EDIT — <why>`.
"""
    if dry:
        print("--- would send this edit prompt to Claude ---")
        print(edit_prompt)
        return 0

    out, err = claude(edit_prompt, timeout=600, allowed=["Read", "Edit", "Grep", "Glob"])
    print(out[-500:])
    m = re.search(r"EDITED\s+(\S+)", out)
    if not m:
        print("no edit made")
        return 0
    edited = m.group(1)

    # regression: benchmark before was the previous benchmark-only cycle; run a fresh one
    print("running benchmark regression ...")
    before = _benchmark_mean()
    subprocess.run([sys.executable, str(HERE / "run_cycle.py"),
                    "--benchmark-only", "--label", f"regr-{p['failure_category']}"],
                   cwd=str(REPO))
    after = _benchmark_mean()
    # targeted improvement sample
    print("running targeted sample ...")
    subprocess.run([sys.executable, str(HERE / "run_cycle.py"), "--n", str(sample),
                    "--label", f"target-{p['failure_category']}"], cwd=str(REPO))
    tgt_delta = _category_delta(p["failure_category"])

    keep = (after is not None and before is not None
            and after >= before - tol
            and (tgt_delta is None or tgt_delta >= gain))
    print(f"benchmark {before} -> {after}  |  targeted category delta {tgt_delta}  "
          f"|  {'KEEP' if keep else 'REVERT'}")

    git("add", "evals/results")
    git("commit", "-m",
        f"eval: {'apply' if keep else 'trial (reverted)'} fix for {p['failure_category']}\n\n"
        f"benchmark {before}->{after}, targeted delta {tgt_delta}\n\n"
        "Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\n"
        f"Claude-Session: https://claude.ai/code/session_01FHeBbPq2DUV8b9bysbJqwJ")
    if keep:
        git("add", edited)
        git("commit", "-m",
            f"skill: address recurring eval weakness ({p['failure_category']})\n\n"
            f"Targeted edit to {edited}. Benchmark {before}->{after} (tol {tol}), "
            f"targeted category improved by {tgt_delta}.\n\n"
            "Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>\n"
            f"Claude-Session: https://claude.ai/code/session_01FHeBbPq2DUV8b9bysbJqwJ")
    else:
        git("checkout", "--", edited)
        print("edit reverted")
    return 0


def _benchmark_mean():
    R = [r for r in rows() if r.get("benchmark")]
    if not R:
        return None
    last = max(r["cycle"] for r in R)
    v = [r["overall"] for r in R if r["cycle"] == last]
    return round(statistics.mean(v), 3) if v else None


def _category_delta(cat):
    R = rows()
    cyc = sorted({r["cycle"] for r in R})
    if len(cyc) < 2:
        return None
    old = [r["overall"] for r in R if r["cycle"] in cyc[:-2] and r.get("failure_category") == cat]
    new = [r["overall"] for r in R if r["cycle"] in cyc[-2:] and r.get("failure_category") == cat]
    if not old or not new:
        return None
    return round(statistics.mean(new) - statistics.mean(old), 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-cycles", type=int, default=3)
    ap.add_argument("--min-hits", type=int, default=6)
    ap.add_argument("--sample", type=int, default=12)
    ap.add_argument("--gain", type=float, default=0.15)
    ap.add_argument("--tol", type=float, default=0.05)
    args = ap.parse_args()
    if args.apply:
        return apply(args.min_cycles, args.min_hits, args.sample, args.gain, args.tol, args.dry_run)
    analyse()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
