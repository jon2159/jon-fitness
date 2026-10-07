# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 482 trained-distribution runs, 0 generalization, 0 wildcard, across 42 cycles._

## Scoreboard — cycle 42 vs 41

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.95 | 3.92 | → |
| Goal alignment | 4.00 | 4.01 | → |
| Load management | 3.90 | 3.91 | → |
| Recovery | 4.10 | 3.86 | ↑ |
| Individualisation | 3.60 | 3.66 | ↓ |
| Programming quality | 4.00 | 3.87 | ↑ |
| Safety | 4.00 | 4.23 | ↓ |
| Consistency (0-5) | 3.60 | 3.56 | ↑ |
| Benchmark overall | 3.95 | 3.92 | → |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **1** | 0 | ↓ |

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
| 18 | 20260919T094408Z | 15 | **3.82** | 4.03 | 3.98 | 3.83 | 3.53 | 3.73 | 3.67 | 3.87 | post-fix-full-cycle |
| 19 | 20260919T100446Z | 8 | **3.92** | 3.81 | 4.09 | 3.94 | 3.88 | 4.00 | 3.50 | 4.12 | revl-hard-ban-fix |
| 20 | 20260919T104717Z | 4 | **3.82** | 3.75 | 3.81 | 4.00 | 3.62 | 3.88 | 3.75 | 4.00 | revl-schedule-claim-fix |
| 21 | 20260919T144528Z | 15 | **3.78** | 3.87 | 3.98 | 3.77 | 3.67 | 3.77 | 3.47 | 3.67 | post-revert-clean-cycle |
| 22 | 20260919T163659Z | 14 | **3.80** | 3.75 | 3.88 | 4.00 | 3.57 | 3.82 | 3.64 | 3.93 | provenance-redesign |
| 23 | 20260928T070006Z | 3 | **4.27** | 4.33 | 4.50 | 4.67 | 4.33 | 3.67 | 4.67 | 3.00 | post-citation-nutrition-fix-verify |
| 24 | 20260928T070841Z | 1 | **4.67** | 5.00 | 5.00 | 4.00 | 5.00 | 4.00 | 5.00 | 5.00 | post-citation-nutrition-fix-verify |
| 25 | 20260928T161340Z | 17 | **4.25** | 4.41 | 4.25 | 4.21 | 4.24 | 4.03 | 4.18 | 4.59 | post-fix-full-benchmark |
| 26 | 20260928T211711Z | 40 | **3.82** | 3.94 | 3.92 | 3.80 | 3.61 | 3.71 | 3.73 | 4.03 | post-fix-full-benchmark |
| 27 | 20261004T115536Z | 36 | **3.87** | 4.01 | 3.90 | 3.82 | 3.79 | 3.69 | 3.92 | 4.08 | regr-poor_decision_hierarchy |
| 28 | 20261004T163443Z | 1 | **4.33** | 4.50 | 4.50 | 4.00 | 4.00 | 4.00 | 5.00 | 5.00 | probe-recheck |
| 29 | 20261004T163538Z | 12 | **3.86** | 3.96 | 3.92 | 4.04 | 3.67 | 3.83 | 3.58 | 3.83 | target-recheck |
| 30 | 20261004T165233Z | 5 | **3.95** | 4.20 | 3.95 | 3.70 | 3.80 | 4.00 | 4.00 | 4.20 | hand-individualisation |
| 31 | 20261004T165800Z | 18 | **3.83** | 4.06 | 3.86 | 3.92 | 3.69 | 3.64 | 3.89 | 3.83 | hand-individualisation-broad |
| 32 | 20261005T153457Z | 1 | **3.80** | 3.50 | 4.00 | 3.50 | 3.50 | 3.50 | 4.00 | 5.00 | probe-b |
| 33 | 20261005T153540Z | 22 | **3.91** | 3.98 | 3.93 | 3.86 | 3.80 | 3.75 | 4.05 | 4.14 | hand-individualisation-broad2 |
| 34 | 20261005T160017Z | 4 | **4.05** | 3.88 | 4.19 | 4.12 | 4.00 | 4.12 | 3.75 | 4.25 | revl-scan-targeted |
| 35 | 20261006T163911Z | 1 | **4.27** | 4.50 | 4.50 | 4.00 | 4.00 | 3.50 | 5.00 | 5.00 | probe-c |
| 36 | 20261006T164006Z | 11 | **3.91** | 4.05 | 3.95 | 3.95 | 3.82 | 3.82 | 3.73 | 4.18 | revl-scan-targeted2 |
| 37 | 20261006T165016Z | 8 | **4.04** | 4.12 | 4.09 | 4.25 | 3.81 | 3.88 | 4.25 | 4.12 | revl-scan-broad2 |
| 38 | 20261006T214840Z | 32 | **3.83** | 3.95 | 3.78 | 3.69 | 3.69 | 3.83 | 4.12 | 4.06 | revl-scan-broad3 |
| 39 | 20261007T061936Z | 6 | **4.02** | 4.25 | 4.04 | 4.00 | 3.75 | 4.08 | 3.83 | 4.33 | extra-volume-targeted |
| 40 | 20261007T080554Z | 1 | **3.73** | 4.00 | 3.75 | 3.50 | 3.50 | 4.00 | 3.00 | 4.00 | extra-volume-targeted |
| 41 | 20261007T090108Z | 35 | **3.92** | 4.01 | 3.91 | 3.86 | 3.66 | 3.87 | 4.26 | 4.23 | extra-volume-broad |
| 42 | 20261007T132527Z | 5 | **3.95** | 4.00 | 3.90 | 4.10 | 3.60 | 4.00 | 4.20 | 4.00 | extra-volume-broad2 |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.40 |
| D | volume_management | 3.60 |
| B | training_specificity | 3.80 |
| F | frequency_management | 3.80 |
| I | exercise_selection | 3.80 |
| L | practicality | 3.80 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Writes out three full hypertrophy sessions (about 45 added hard sets) because three slots exist, though C is hedged

## Hard failures in the latest cycle

- **ADV-038** — Roughly 45 added hard sets a week on top of 5 REVL sessions is close to the stated hard failure. The response admits it can't size this against REVL totals, and still defaults to it at full dose. It is partly mitigated by the upper-body focus, the conditional C, and the trim advice.

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
| 18 | 7 | 3.84 |
| 19 | 1 | 3.73 |
| 21 | 7 | 3.78 |
| 22 | 7 | 3.76 |
| 23 | 3 | 4.27 |
| 24 | 1 | 4.67 |
| 25 | 17 | 4.25 |
| 26 | 40 | 3.82 |
| 27 | 36 | 3.87 |
| 28 | 1 | 4.33 |
| 29 | 7 | 3.79 |
| 30 | 3 | 3.91 |
| 31 | 18 | 3.83 |
| 32 | 1 | 3.80 |
| 33 | 22 | 3.91 |
| 35 | 1 | 4.27 |
| 36 | 6 | 3.83 |
| 37 | 8 | 4.04 |
| 38 | 32 | 3.83 |
| 39 | 2 | 4.03 |
| 40 | 1 | 3.73 |
| 41 | 35 | 3.92 |
| 42 | 5 | 3.95 |

## Consistency contradictions — latest cycle

- **ADV-036** — Item 3 asserts "REVL probably already trains squat/hinge patterns more than once a week" and then uses that to say squatting on every rest day would break the "2–3 hard sessions per muscle group per week" budget, while also saying "I haven't confirmed this client's actual days". The central volume argument rests on an unverified assumption about REVL exposure.
- **ADV-036** — It says "Run the Masters 2-day variant ... on **one** non-REVL day". A 2-day variant is described as two sessions per week, but it is prescribed as a single session on one day. The dosing is unclear and conflicts with the 'one session' advice.
- **ADV-036** — The "Progression trigger" section says "If the anchor day sits at RPE ≤6, nudge the working 1RM up" and sets %1RM-based anchors ("~60–70%", "~5%") while the gate check lists G3 movement competence and G4 contraindications to loaded testing as "Unknown" and says "I treat Unknown as unmet". It still gives a concrete load prescription before the gate is cleared, which cancels the 'unmet' stance.
- **ADV-036** — The recommendation states "Build and Peak phases are already a barbell strength progression" and "two concurrent strength peaks" as fact, and says squatting on all rest days gives "a worse result on both". The only support is that it is the author's reading of an integration reference (§10). The claim is partly hedged but the mechanism and 'worse result' are asserted without support.
- **ADV-036** — It says to "Replace" the overlapping REVL day with the wave 'keeping REVL's conditioning-format sessions', yet the opening argues against a second strength peak and for recovery. Replacing a REVL strength day with a Russian squat wave in Build is not dose-neutral, and the plan does not account for total weekly load for the 3 remaining REVL sessions plus the wave. The statement 'Peak... replaces REVL's strength days' is also inconsistent with the earlier claim that the plan 'only applies to Build'.
- **ADV-037** — Item 2 says "Skip the planned session" and "If he can't walk comfortably, rest or walk", but also offers "Upper body or unaffected muscle groups at a normal-to-reduced load" with no check that he can do this without aggravating his gait or that upper-body work is not part of the same sore session. This is a soft inconsistency.
- **ADV-037** — The re-entry table says "Session 3 onward... roughly 90–100% of pre-holiday loads" while the text says "strength mostly holds" after 3 weeks. It also says "As heavy as before" is the cause, which is a mild tension between a 100% target and the stated cause. The ramp is labeled as the author's own judgement, so this is minor.
- **ADV-037** — It states "Soreness typically peaks around 24–72 hours... settles within about a week" and that rhabdomyolysis is "rare but real" as fact, in a response that also says it is "mostly General knowledge" and that no course page was opened. These are flagged as general knowledge, but the mechanism and timing are not supported.
- **ADV-038** — Opens with "book Sessions A and B at full dose" as the default, but the phase table says Build means "Run A and B at about half the sets" and Peak/testing is "Support work only". The "full dose" default is stated while her phase is unknown, so it is applied without checking the phase rule it later sets.
- **ADV-038** — Says "I can't size that against her REVL totals until I know her track and phase", yet it prescribes a specific ~45 added hard sets/week at "full dose" and says that is the default. That is a firm volume prescription made before the REVL exposure is accounted for.
- **ADV-038** — Session C is called "light enough to run in any phase except testing weeks", but the table says Build means "skip C" and Deload allows "Technique, assessment and mobility only". C is a 10-set hard-set session, so it contradicts both rows.
- **ADV-038** — Session B is labelled "non-axial legs" and says "Keep every session at least about 24 h away from her densest mixed day and her hinge-led day". Leg curls and calves are loaded on the hinge-pattern posterior chain, and the plan also says "lower-body volume is the most expensive thing to add". This is a soft tension, since the leg curl and calf volume is small.
