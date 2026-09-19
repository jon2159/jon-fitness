# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 167 trained-distribution runs, 0 generalization, 0 wildcard, across 17 cycles._

## Scoreboard — cycle 17 vs 16

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.95 | 3.85 | ↑ |
| Goal alignment | 4.40 | 4.00 | ↑ |
| Load management | 3.90 | 3.97 | ↓ |
| Recovery | 3.60 | 3.75 | ↓ |
| Individualisation | 3.90 | 3.81 | ↑ |
| Programming quality | 4.20 | 3.44 | ↑ |
| Safety | 4.00 | 3.75 | ↑ |
| Consistency (0-5) | 2.80 | 4.12 | ↓ |
| Benchmark overall | 3.93 | 3.85 | ↑ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **0** | 1 | ↑ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |
| 3 | 20260910T223924Z | 15 | **3.53** | 3.87 | 3.22 | 3.93 | 3.80 | 3.23 | 3.80 | 2.93 | nightly |
| 4 | 20260911T144031Z | 15 | **3.41** | 3.83 | 2.98 | 3.40 | 3.63 | 3.70 | 3.73 | 2.67 | nightly |
| 5 | 20260917T055910Z | 10 | **3.95** | 4.20 | 3.95 | 3.85 | 4.00 | 3.85 | 3.40 | 3.90 |  |
| 6 | 20260917T062347Z | 2 | **3.67** | 4.25 | 3.12 | 3.00 | 4.00 | 4.50 | 4.50 | 2.50 |  |
| 7 | 20260917T062841Z | 1 | **4.13** | 3.50 | 4.50 | 4.00 | 4.50 | 2.50 | 5.00 | 5.00 |  |
| 8 | 20260917T065334Z | 1 | **4.87** | 5.00 | 5.00 | 5.00 | 4.00 | 5.00 | 5.00 | 5.00 | cmd-runner-smoke |
| 9 | 20260917T065718Z | 24 | **4.59** | 4.79 | 4.66 | 4.48 | 4.54 | 4.19 | 4.54 | 4.92 | cmd-benchmark-smoke |
| 10 | 20260918T030036Z | 32 | **3.75** | 4.12 | 3.72 | 3.28 | 3.80 | 3.56 | 3.66 | 4.16 |  |
| 11 | 20260918T083400Z | 8 | **3.49** | 3.81 | 3.34 | 3.19 | 3.50 | 3.12 | 3.50 | 4.38 |  |
| 12 | 20260918T155912Z | 8 | **3.77** | 4.19 | 3.75 | 3.50 | 3.56 | 3.75 | 4.12 | 3.38 | post-decision-framework-fix |
| 13 | 20260918T162015Z | 8 | **3.67** | 3.69 | 3.59 | 3.38 | 3.44 | 3.75 | 4.12 | 4.25 | post-decision-framework-fix-v2 |
| 14 | 20260918T164301Z | 3 | **3.02** | 3.17 | 2.83 | 2.83 | 2.83 | 3.17 | 3.67 | 2.33 | post-plateau-loophole-fix |
| 15 | 20260919T012341Z | 3 | **3.53** | 3.67 | 3.17 | 3.17 | 3.67 | 3.83 | 3.33 | 4.33 | post-mechanical-enforcement-fix |
| 16 | 20260919T013011Z | 8 | **3.85** | 4.00 | 3.97 | 3.75 | 3.81 | 3.44 | 3.88 | 3.75 | final-validation |
| 17 | 20260919T093359Z | 5 | **3.95** | 4.40 | 3.90 | 3.60 | 3.90 | 4.20 | 3.60 | 4.00 | revl-labeling-fix |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| H | recovery_compatibility | 3.40 |
| F | frequency_management | 3.60 |
| M | long_term_coherence | 3.60 |
| G | fatigue_management | 3.80 |
| L | practicality | 3.80 |
| O | communication | 3.80 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_load_management | 2 |
| poor_decision_hierarchy | 1 |
| insufficient_individualisation | 1 |

## Latest cycle — most-hit traps

- (1×) Effectively writes a leg hypertrophy programme for the run build (mitigated because running load is explicitly addressed)
- (1×) Partially ignores grip/elbow accumulation: weighted pull-ups/chin-ups 4x3-5 in both sessions, plus deadlift, RDL and Nordics, all load grip and elbows, with no grip-management cap beyond a tendon-irritation deload trigger

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |
| 3 | 7 | 3.89 |
| 4 | 7 | 3.16 |
| 5 | 7 | 3.98 |
| 6 | 1 | 3.73 |
| 7 | 1 | 4.13 |
| 9 | 24 | 4.59 |
| 10 | 32 | 3.75 |
| 11 | 8 | 3.49 |
| 12 | 8 | 3.77 |
| 13 | 8 | 3.67 |
| 14 | 3 | 3.02 |
| 15 | 3 | 3.53 |
| 16 | 8 | 3.85 |
| 17 | 4 | 3.93 |

## Consistency contradictions — latest cycle

- **SC-0025** — Says the Volume phase has 'the most headroom' and caps added intensity at 80%/RIR ≥3, yet Slot A prescribes DB bench at RIR 2–3 and the progression baseline is 'the load Ivy can press for 8 reps at RIR 2', which exceeds the stated RIR ≥3 cap.
- **SC-0025** — Cites 'foundational Load/Speed at 60–70% 1RM' as the novice entry and also says 'Don't run a true 1RM test on a novice', so the %1RM prescriptions (60–70%, ≤85%, ~80%) have no way to be applied without a known 1RM.
- **SC-0025** — Says 'Seven sessions a week is a real load' and recommends considering dropping to 2 PT slots, but the default still runs three PT slots plus a Slot C that adds Zone 1–2 aerobic work, so the plan adds to the load it flags as risky.
- **SC-0025** — Says to 'Keep any lower-body loading light, since REVL doesn't rest the lower body on any day', yet Slot B prescribes single-leg RDL 3×8/side and loaded suitcase carries, which add lower-body and posterior chain load.
- **SC-0025** — Opens with 'only two of them loaded' but Slot C includes light pressing, and the plan then recommends 'add at most one PT press slot' or 'none' depending on REVL exposure. The default plan puts a press slot in A regardless of the unanswered REVL question.
- **SC-0025** — States 'REVL never programs' Zone 1–2 aerobic work and that REVL 'doesn't rest the lower body on any day' as fact, while elsewhere admitting the REVL push frequency ('roughly half of sessions') is unverified for Ivy.
- **ADV-008** — Says "Drop REVL from 4 to 3 ... That leaves about 9 sessions" and frames the goal as cutting sessions, yet the PT sessions are kept at 2 for weeks 1–5, so the count is 4 runs + 3 REVL + 2 PT = 9, still high; and the fallback "make one PT slot a 25-minute mini-session" is inconsistent with the headline claim that the fix is cutting sessions.
- **ADV-008** — "Double up hard days. Put a PT leg session on the same day as a quality run, or after it" — stacking heavy leg work with a hard run on one day contradicts the stated interference concern ("compete for recovery") and the "Skip heavy… avoid delayed soreness" logic. It also conflicts with "Keep PT off ... within about 24 h either side of REVL's heaviest lower/hinge days" whenever those days coincide.
- **ADV-008** — Recommends "Keep running at 40 km" and the ≤10%/week cap while also saying running is primary and hypertrophy is a "small add-on", but then prescribes 10–12 hard sets of leg work twice weekly for 5 weeks (weeks 1–5) on top of 40 km and 3 REVL sessions, which is not a 'small' dose given its own overreach warning. The "Drop REVL" advice also treats REVL as something to reduce by default, before knowing block phase or the class type, which it lists as open question 1.
- **ADV-008** — Says the dose sits "at its low end" of the Table 9-12 band, but 3 sets per exercise across 5 exercises (~14–15 sets, with 3 × 8–12 sets and 60–90 s rest) is stated as "roughly 10–12 hard sets" — the table sums to 14–15 sets (3+3+3+2–3+3), so the set count contradicts the table.
- **ADV-008** — Prescribes a specific 5% load increase and a 'race taper' cutoff of ~7–10 days as if firm, and states 'hip thrust... without axial load' and 'hamstrings without adding hinge load' for a hip thrust, which is a hip-extension/hinge-pattern movement, contradicting the stated goal of avoiding hinge load.
- **ADV-010** — Item 4 of the plan says "Stop the last set of each exercise about 1–2 reps short of failure", while the 2-for-2 rule requires "2 or more reps beyond the target on the last set". Those two only fit together if the rep target is set well below her capacity, which the plan never states.
