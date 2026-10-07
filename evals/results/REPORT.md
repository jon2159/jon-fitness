# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 489 trained-distribution runs, 0 generalization, 0 wildcard, across 43 cycles._

## Scoreboard — cycle 43 vs 42

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 4.02 | 3.95 | ↑ |
| Goal alignment | 4.29 | 4.00 | ↑ |
| Load management | 4.11 | 3.90 | ↑ |
| Recovery | 3.93 | 4.10 | ↓ |
| Individualisation | 3.71 | 3.60 | ↑ |
| Programming quality | 4.07 | 4.00 | ↑ |
| Safety | 4.14 | 4.00 | ↑ |
| Consistency (0-5) | 3.14 | 3.60 | ↓ |
| Benchmark overall | 4.02 | 3.95 | ↑ |
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
| 43 | 20261007T175713Z | 7 | **4.02** | 4.29 | 4.11 | 3.93 | 3.71 | 4.07 | 3.86 | 4.14 | ramp-targeted |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.57 |
| F | frequency_management | 3.71 |
| H | recovery_compatibility | 3.86 |
| L | practicality | 3.86 |
| M | long_term_coherence | 3.86 |
| O | communication | 3.86 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| insufficient_individualisation | 2 |
| poor_load_management | 1 |
| poor_context_interpretation | 1 |
| poor_decision_hierarchy | 1 |

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
| 43 | 3 | 4.02 |

## Consistency contradictions — latest cycle

- **SC-0037** — "Week 1 is a reduced-dose start with every set stopped well short of failure" conflicts with the table's week 1 prescription of about 5 hard sets at 3 RIR on a pull-up/row-heavy session. The 3 RIR is consistent with the claim, but 5 added hard sets on top of REVL 5x in the first week back from a six-week layoff isn't clearly "reduced", and nothing says what it is reduced from.
- **SC-0037** — "Those are my numbers, sized as a ramp because I can't yet measure them against their REVL week" admits the added volume (5→7→9 hard sets) is not accounted for against REVL weekly load. It still commits to a fixed progression and a specific week-3 target, and the stated trigger to "hold the ramp" if classes feel worse is only a soft guard.
- **SC-0037** — "Volume is the best phase to add to... the most headroom for added work" conflicts with the layoff logic that "Sofia's tolerance is below their two years of training history". The recommendation adds the most volume in exactly the weeks when the client is least conditioned, and it treats the Volume phase as having headroom without confirming whether Sofia has restarted REVL at Volume week 1.
- **SC-0037** — The "Progression trigger" says to add load of "about 5%" once the top of the rep range is hit for two sessions. That is a specific number stated without support. It is also at odds with the dumbbell-only constraint, since dumbbells usually come in fixed jumps, and with a once-a-week session, where "two sessions in a row" means two weeks. That would fall mostly after the three-week ramp.
- **SC-0037** — "Leave the legs alone. No REVL phase gives the lower body a real rest" is a broad claim about the programme. It is mixed with a note that the REVL schedule is unconfirmed ("Don't assume this"), so the claim is partly unsupported.
- **SC-0037** — "Avoid heavy hinge work" is justified by the captured programme's hinge load, but the same plan prescribes a bent-over DB row. That is a hinge-position, spinal-loading movement, and it sits oddly with "anything that adds spinal loading" being avoided. The alternative "supported variant" is conditional on an incline bench that the client may not have.
- **SC-0039** — Opening says "book one PT session a week for weeks 1–2" but the session is called "Session A" and the plan says "add a short second slot from week 3", while the Week 3 step-up then reads "add a 30-minute second slot" — at that point PT is described as one slot plus a second, yet the Aerobic/Zone 1–2 slot is effectively the only addition, and the "progressive strength" slot is not stated to continue clearly; minor ambiguity in slot count.
- **SC-0039** — "I can't size extra work against their REVL weekly load yet" yet the plan prescribes a specific dose of "about 8 hard sets", "3 reps in reserve" and a "+5% load or one set" progression, and states the captured REVL programming "tends to under-serve" carries, horizontal pulling and single-leg control, as though REVL's content is known.
- **SC-0039** — States "REVL tends to load those patterns [hinge/squat] in almost every phase" as the reason to avoid lower-body volume, while also prescribing goblet squats 2×8 and saying captured REVL programming is "a lower bound, not Hannah's actual weeks" — an unsupported claim about REVL content used to justify the dose (flagged as general judgement, but still asserted as fact).
- **SC-0039** — "Aerobic work is the quality REVL structurally can't give them, since everything in it is capped" is stated as fact without support, and conflicts with the plan's own admission that Hannah's actual REVL weeks are unknown.
- **SC-0039** — "Soreness mostly reflects novelty and lengthening (eccentric) work. It can be high in a session that did little for strength, and absent in one that did a lot" is a physiological mechanism stated as fact without citation (labelled general knowledge, so only a soft issue); also "Volume is the phase with the most headroom" is asserted while saying the REVL load cannot yet be sized.
- **SC-0039** — Week 3 "Build is the next phase, and the PT dose shrinks then" is given as a reason to avoid building a PT habit now, which sits oddly with the goal of getting a never-programmed client to build a consistent habit; and it uses a 3-sec eccentric goblet squat in a plan that says "Don't chase soreness. No novel high-eccentric lower-body work" — a tempo-lowering squat is mildly eccentric-emphasised novel lower-body work.
