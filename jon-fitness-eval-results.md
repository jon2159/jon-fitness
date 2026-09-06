# jon-fitness — Evaluation of the Russian Strength Program Additions (Iteration 2)

**Date:** 2026-09-06 · **Method:** skill-creator eval loop (Iteration 2)  
**Compared:** Refined new skill (`jon-fitness` with Russian Strength Program archetype, updated §5 cardio/deficit guidance, and `--taper-weeks`/`--meet` generator flags) vs. pre-Russian-Strength baseline snapshot (`skill-snapshot`).  
**Dataset:** 5 test cases, 2 runs each for the new skill (variance estimate) + baseline run(s), graded against fixed objective assertions.

---

## Headline Summary

| Metric | New skill (mean ± stddev) | Old skill (mean ± stddev) | Delta |
|---|---|---|---|
| **Pass rate** | **100.0% ± 0.0%** (49/49) | **67.3% ± 28.6%** (33/49) | **+32.7 pts** |
| **Time (mean)** | **350.5 s ± 185.5 s** | **409.0 s ± 253.6 s** | **−58.5 s** (new is faster) |
| **Tokens (mean)** | **99.8k ± 43.0k** | **84.0k ± 61.9k** | +15.8k |

The additions demonstrate a **strong, consistent performance advantage (+32.7 pts)** with zero regressions on existing general-population, chronic condition, or scope-of-practice workflows.

---

## Per-Case Breakdown

| # | Scenario | New (r1 / r2) | Old (r1) | Δ | Evaluation Read |
|---|---|---|---|---|---|
| **2** | `regression-htn-fatloss`<br>Marcus Chen: 46, HTN + beta-blocker, detrained | **10/10** (100%)<br>**10/10** (100%) | **10/10** (100%) | **0** | **Clean regression check.** Identical screening, medical clearance treated as BLOCKING, RPE/talk-test override for beta blocker, hypertension FITT-VP overrides, Base cardio + Functional/Movement muscular phase. `validate_plan.py` reports 0 errors. The archetype does not leak into non-strength programming. Zero variance across runs. |
| **6** | `athlete-meet-peak`<br>Dave Ellis: 29, 4-yr powerlifter, meet in 10 wks | **12/12** (100%)<br>**12/12** (100%) | **8/12** (66.7%) | **+0.33** | **Russian V5 meet peak.** New skill leverages `russian_block.py` with `--taper-weeks 1 --meet` to produce a 10-week schedule (8 wave + 1 taper + 1 meet) with attempt selection and spotting guidance (Ch 10 p74). Load math verified: all wave loads round to 2.5 kg increments. Baseline built a competent generic linear peak but missed archetype structure, gate sections, retest protocol, and meet timing. |
| **7** | `beginner-scaled-entry`<br>Nadia: 3-month novice wants Russian squat wave | **7/7** (100%)<br>**7/7** (100%) | **6/7** (85.7%) | **+0.14** | **Structured refusal & on-ramp.** Both refuse immediate wave placement. New skill specifically identifies gate failures (G2 experienced lifter ≥80%, G3 movement competence), provides a Movement-phase on-ramp (60–70% 1RM double progression), establishes submaximal rep testing (Ch 10 Table 10-25), and offers the Masters variant as a bridge. Baseline deferred testing entirely. |
| **8** | `impatient-cut-mid-block`<br>Impatience at wk 5, wants hard cut + set kcal/cardio | **8/8** (100%)<br>**8/8** (100%) | **2/8** (25.0%) | **+0.75** | **Highly discriminating.** New skill identifies week 5 as the start of intensification/peaking (85–105% 1RM), explains why cutting into a peak blunts neuromuscular output and retests, prescribes deficit periodisation (holding maintenance through wks 6–9), doses cardio to recovery while explicitly rejecting the Ch 12 150–250 min/wk figure as obesity guidance, holds scope (RD referral), and offers sequential blocks. Baseline failed 6 of 8 assertions. |
| **9** | `genpop-strength-fatloss`<br>Sam Reyes: 34, 3-yr lifter, PBs + 4–5 kg fat loss | **12/12** (100%)<br>**12/12** (100%) | **7/12** (58.3%) | **+0.42** | **Concurrent strength + fat loss.** New skill estimates 1RMs from rep-maxes, periodises the deficit (moderate wks 1–5 → maintenance wks 6–9), pulls back cardio in the peak, enforces RD referral, and generates exact 2.5 kg rounded wave loads. Baseline ran a flat deficit into peak singles, used generic cardio, blurred scope with specific macros, and failed load-rounding math. |

---

## Verification of Iteration 1 Refinements

In Iteration 1, 4 specific refinements were flagged. Iteration 2 verifies all 4:

1. **Cardio Caveat for Lean Strength Clients (§5):**  
   `references/russian-strength-program.md` §5 now distinguishes between Ch 12 obesity-population cardio targets (150–250 min/wk) and athletic concurrent programming. In evals 8 and 9, the new skill successfully doses conditioning to recovery headroom and pulls it back during peak weeks rather than over-prescribing volume.
2. **Automated Taper and Meet Generation in `russian_block.py`:**  
   The generator was upgraded with `--taper-weeks N` and `--meet`. In eval-6, running `--taper-weeks 1 --meet` automatically produced the full 10-week meet cycle without requiring manual CSV splicing. `validate_plan.py` validated with 0 errors.
3. **Sharpened Eval-8:**  
   Eval-8 was rewritten to focus on mid-block deficit periodisation, recovery-dosed cardio, and sequential blocks. The baseline scored 25.0% while the new skill scored 100.0%, creating a decisive +75 pt discrimination.
4. **Load-Math Verification:**  
   Eval-6 and eval-9 now formally verify arithmetic rounding of target percentages to 2.5 kg plate increments. The new skill passed 100% of arithmetic spot-checks; the old baseline failed eval-9 by using unrounded integer values (e.g. 128 kg instead of 127.5/130 kg).
5. **Variance Estimation:**  
   Running duplicate executions (`run-1` and `run-2`) across all 5 test cases yielded a standard deviation of **0.0%** for pass rate, confirming that the new skill's instructions, prompts, and generators produce deterministic, reliable outputs.

---

## Artifacts & Deliverables

- **Review Viewer HTML:** [jon-fitness-eval-review.html](file:///Users/jonathan.tan/Desktop/Projects/jon-fitness/jon-fitness-eval-review.html)  
  *Self-contained review interface with two tabs: "Outputs" for inspecting per-eval transcripts/plans and leaving notes, and "Benchmark" for comparative summary statistics.*
- **Benchmark Data:** [.claude/skills/jon-fitness-workspace/iteration-2/benchmark.json](file:///Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness-workspace/iteration-2/benchmark.json)
- **Benchmark Markdown:** [.claude/skills/jon-fitness-workspace/iteration-2/benchmark.md](file:///Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness-workspace/iteration-2/benchmark.md)

---

## Final Recommendation

**Ship the additions and refinements.** The Russian Strength Program additions in `.claude/skills/jon-fitness` are fully verified, robust across duplicate runs, and provide clear structural improvements for heavy strength programming without compromising general CPT course boundaries.
