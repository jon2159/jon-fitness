#!/usr/bin/env python3
"""Grader VALIDITY harness — does the grader agree with a human expert?

Validity is not reliability. grader_reliability.py checks the grader against
*itself*; this checks it against *Jon*. A grader that is consistent but
miscalibrated (too generous, too harsh, blind to a whole dimension) passes
reliability and fails here.

Method
------
1. Jon fills `human_scores` (A-O, 0-5) for each item in
   scenarios/gold/gold_responses.json.
2. This script grades the same responses with the real eval grader.
3. Reports, per dimension and overall:
      MAE   mean absolute error   (grader - human)
      bias  mean signed error     (>0 grader too generous, <0 too harsh)
   and lists every item/dimension where they disagree by >= 2 points.

Writes results/GRADER_VALIDITY.md.

Re-run whenever rubric.md or the grade prompt changes — a stale gold read is
worse than none. The script refuses to run if the rubric hash has moved since
the gold file was authored, unless you pass --accept-rubric-drift.

Usage
-----
    python evals/grader_validity.py
    python evals/grader_validity.py --accept-rubric-drift
"""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics
import sys
from pathlib import Path

from run_cycle import DIMS, DIM_NAMES, RUBRIC, claude, grade_prompt, extract_json, composites

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GOLD = HERE / "scenarios" / "gold" / "gold_responses.json"
OUT = HERE / "results" / "GRADER_VALIDITY.md"


def rubric_sha():
    return hashlib.sha256(RUBRIC.read_text().encode()).hexdigest()[:12]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--accept-rubric-drift", action="store_true")
    ap.add_argument("--grade-timeout", type=int, default=240)
    args = ap.parse_args()

    gold = json.loads(GOLD.read_text())
    authored = gold.get("rubric_sha_when_authored")
    if authored and authored != rubric_sha() and not args.accept_rubric_drift:
        print(f"rubric hash moved ({authored} -> {rubric_sha()}). Re-score the gold set, "
              f"update rubric_sha_when_authored, or pass --accept-rubric-drift.", file=sys.stderr)
        return 1

    items = [it for it in gold["items"] if it.get("human_scores")]
    missing = [it["gold_id"] for it in gold["items"] if not it.get("human_scores")]
    if not items:
        print("no items have human_scores yet — Jon needs to score "
              "evals/scenarios/gold/gold_responses.json first", file=sys.stderr)
        return 1
    if missing:
        print(f"note: {len(missing)} unscored item(s) skipped: {', '.join(missing)}", file=sys.stderr)

    rubric = RUBRIC.read_text()
    per_item, err_by_dim = [], {d: [] for d in DIMS}
    big_gaps = []
    for it in items:
        s = dict(it["scenario"])
        s.setdefault("expected_priorities", it["scenario"].get("expected_priorities", []))
        graw, gerr = claude(grade_prompt(s, it["response"], rubric), args.grade_timeout, REPO,
                            allowed=["Read"])
        g = extract_json(graw)
        if not g or "scores" not in g:
            per_item.append(dict(gold_id=it["gold_id"], error=gerr or "parse failed"))
            print(f"  {it['gold_id']}: grade FAILED", file=sys.stderr)
            continue
        gsc = {d: int(g["scores"].get(d, 0)) for d in DIMS if d in g.get("scores", {})}
        hsc = {d: int(it["human_scores"][d]) for d in DIMS if d in it["human_scores"]}
        diffs = {d: gsc[d] - hsc[d] for d in DIMS if d in gsc and d in hsc}
        for d, e in diffs.items():
            err_by_dim[d].append(e)
            if abs(e) >= 2:
                big_gaps.append((it["gold_id"], d, hsc[d], gsc[d]))
        per_item.append(dict(
            gold_id=it["gold_id"],
            human_overall=round(statistics.mean(hsc.values()), 2),
            grader_overall=composites(gsc)["overall"],
            mae=round(statistics.mean(abs(e) for e in diffs.values()), 2),
            bias=round(statistics.mean(diffs.values()), 2),
        ))
        print(f"  {it['gold_id']}: human {statistics.mean(hsc.values()):.2f} "
              f"grader {composites(gsc)['overall']:.2f}", file=sys.stderr)

    scored = [p for p in per_item if "mae" in p]
    lines = ["# Grader validity (agreement with Jon)\n",
             f"_{len(scored)} human-scored gold items, rubric `{rubric_sha()}`. "
             f"Validity ≠ reliability — see GRADER_RELIABILITY.md._\n"]
    if scored:
        all_abs = [abs(e) for v in err_by_dim.values() for e in v]
        all_signed = [e for v in err_by_dim.values() for e in v]
        lines += [f"- **Overall MAE: {statistics.mean(all_abs):.2f} points** "
                  f"(rule of thumb: ≤ 0.5 good, ≤ 0.8 usable, > 1.0 the grader needs work)",
                  f"- **Overall bias: {statistics.mean(all_signed):+.2f}** "
                  f"({'grader runs generous' if statistics.mean(all_signed) > 0.15 else 'grader runs harsh' if statistics.mean(all_signed) < -0.15 else 'well centred'})",
                  f"- Items where grader & human disagree by ≥2 on some dimension: {len(big_gaps)}",
                  "",
                  "| Item | Human | Grader | MAE | Bias |", "|---|--:|--:|--:|--:|"]
        for p in scored:
            lines.append(f"| {p['gold_id']} | {p['human_overall']:.2f} | {p['grader_overall']:.2f} | "
                         f"{p['mae']:.2f} | {p['bias']:+.2f} |")
        lines += ["\n## Per-dimension agreement\n", "| Dim | Name | MAE | Bias | n |", "|---|---|--:|--:|--:|"]
        for d in DIMS:
            v = err_by_dim[d]
            if v:
                lines.append(f"| {d} | {DIM_NAMES[d]} | {statistics.mean(abs(e) for e in v):.2f} | "
                             f"{statistics.mean(v):+.2f} | {len(v)} |")
        if big_gaps:
            lines += ["\n## Disagreements ≥ 2 points\n", "| Item | Dim | Human | Grader |", "|---|---|--:|--:|"]
            for gid, d, h, gg in big_gaps:
                lines.append(f"| {gid} | {d} ({DIM_NAMES[d]}) | {h} | {gg} |")
    else:
        lines.append("_No gold item graded successfully._")

    OUT.write_text("\n".join(lines) + "\n")
    print(f"\nwrote {OUT.relative_to(REPO)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
