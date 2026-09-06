# jon-fitness — evaluation of the Russian Strength Program additions

**Date:** 2026-09-06 · **Method:** skill-creator eval loop (iteration 1)
**Compared:** new skill (with the strength-block archetype) vs. the pre-Russian-Strength
snapshot (`git HEAD` at commit 99a60c1) as baseline.
**5 test cases, 1 run each per version, graded by independent subagents against fixed assertions.**

---

## Headline

| | New skill | Old skill | Delta |
|---|---|---|---|
| **Pass rate** | **100%** (45/45) | 82.8% (37/45) | **+17 pts** |
| Time (mean) | 353 s | 408 s | −54 s (new is faster) |
| Tokens (mean) | ~57k | ~62k | −5k |

The additions are a **clear net positive** and did not regress existing behaviour.

## Per-case

| # | Scenario | New | Old | Δ | Read |
|---|---|---|---|---|---|
| **2** | HTN + beta-blocker fat-loss client (regression check) | 10/10 | 10/10 | 0 | **Clean regression.** Identical screening, clearance-as-BLOCKING, RPE-not-HR, hypertension overrides, correct phases, files validate. The additions don't leak into normal programming. |
| **6** | Powerlifter, peak S/B/D for a meet in 10 wks | 11/11 | 7/11 | **+0.36** | New skill produced a real Russian V5 block (6×2 @ 80% anchor + volume→intensity wave) via `russian_block.py`, with the eligibility-gate and wave-parameters sections and a meet-timed 1RM retest. Old skill built a *competent generic* linear peak — course-grounded and safe, but not Russian-style, hand-assembled, no gate/retest sections. |
| **7** | 3-month beginner wants "the Russian program" | 7/7 | 6/7 | **+0.14** | Both correctly refuse and lay out the Movement-phase on-ramp. New skill also recommends a rep-max baseline test (from the reference's scaled-entry / retest sections) and names the Masters-variant bridge; old skill defers testing entirely (the one assertion it missed). |
| **8** | "Give me exact calories and macros" | 6/6 | 6/6 | 0 | Both hold the scope line and refer to an RD. **Largely non-discriminating** — see below. |
| **9** | Experienced lifter, PBs + −4–5 kg fat, ~2 months | 11/11 | 7/11 | **+0.36** | New skill: archetype + gate + **deficit periodised out of the peak** (moderate wks 1–5 → maintenance wks 6–9) + conditioning off leg days + RD referral. Old skill: competent generic linear block but a **flat, non-periodised deficit**, deliberately sub-target cardio, and it named a specific kcal deficit + protein g/kg (marginal scope slip). |

## What the additions demonstrably buy you

1. **The Russian structure itself.** Only the new skill produces the 6×2 @ 80% anchor + wave;
   the baseline defaults to a generic accumulation→intensification→peak. If "combine CPT with
   the Russian program" is the goal, the baseline doesn't deliver it.
2. **The fat-loss integration.** Deficit periodisation (hold maintenance through the peak) is
   the new skill's most valuable single idea and the baseline doesn't reach it reliably —
   eval-9 old ran a flat deficit into the peak week.
3. **Consistency on the guardrails.** The beginner-refusal and scope cases were *already* right
   in the base skill (its FITT-VP tables + scope rules carry them). The archetype makes the
   refusal *structured and repeatable* (a named gate, a defined scaled-entry path) rather than
   re-derived from first principles each time — lower variance, not a correctness fix.
4. **Speed.** Having the framework + generator means less from-scratch derivation: the new
   skill was ~25–30% faster on the two archetype-heavy cases.

## Weaknesses / refinements surfaced

### Content
- **The 150–250 min/wk cardio figure (eval-9).** The reference file cites it for fat loss, but
  it is **Ch 12 obesity-population guidance**. The old skill argued — reasonably — that a lean
  strength athlete should dose cardio to protect recovery, *not* to hit that band. The new
  skill's runs leaned on untracked daily steps to claim the band. **Fix:** `russian-strength-program.md`
  §5 should flag 150–250 min/wk as obesity-population guidance being extrapolated, and say that
  for a lean/athletic client conditioning is dosed to energy balance + recovery, not to a fixed
  minute target.
- **Both archetype runs hand-edited the generated CSV** to add a taper / meet week —
  `russian_block.py` produces the 9-week wave but no taper. **Fix:** an optional `--taper-weeks N`
  / `--meet-week` flag on the generator, or a note in the reference that the last 1–2 weeks are
  a hand-built taper.

### Eval design (for next iteration)
- **eval-8 is weak** — 5 of its 6 assertions pass regardless of the archetype (generic scope +
  Ch 12 content). Only "ease the deficit to maintenance in the peak" is archetype-specific, and
  even the baseline got there by extrapolation. Rewrite it to test something the archetype
  uniquely does, or drop it.
- **Several assertions check presence, not correctness** — citations, filenames, "cites a page".
  The grader spot-checked citation accuracy manually and it held up, but the assertions don't
  force it. eval-6's load-math check (wave loads = round(%×1RM, 2.5 kg)) is the model to copy.
- **The `clients/<name>` path assertion** can't be verified from the run outputs alone (the
  subagents were told to write elsewhere). It effectively only checks the filename + sections.
- **1 run per case** — pass rates have no variance estimate. eval-2/eval-8 flat results are
  reassuring but a 2nd/3rd run would firm up the +0.36 deltas.

## Recommendation

Ship the additions. Before a second iteration:
1. Soften the 150–250 min/wk guidance in `russian-strength-program.md` §5 (obesity-population caveat).
2. Add a taper option to `russian_block.py` or document the hand-built taper.
3. Replace or sharpen eval-8; add a load-math assertion to eval-9 like eval-6 has.
4. Re-run with 2–3 runs per case for a variance estimate.
