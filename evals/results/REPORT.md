# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 435 trained-distribution runs, 0 generalization, 0 wildcard, across 38 cycles._

## Scoreboard — cycle 38 vs 37

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.83 | 4.04 | ↓ |
| Goal alignment | 3.95 | 4.12 | ↓ |
| Load management | 3.78 | 4.09 | ↓ |
| Recovery | 3.69 | 4.25 | ↓ |
| Individualisation | 3.69 | 3.81 | ↓ |
| Programming quality | 3.83 | 3.88 | ↓ |
| Safety | 4.06 | 4.12 | ↓ |
| Consistency (0-5) | 3.44 | 3.50 | ↓ |
| Benchmark overall | 3.83 | 4.04 | ↓ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **2** | 0 | ↓ |

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

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| H | recovery_compatibility | 3.47 |
| K | individualisation | 3.66 |
| D | volume_management | 3.69 |
| I | exercise_selection | 3.69 |
| B | training_specificity | 3.72 |
| L | practicality | 3.72 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| insufficient_individualisation | 8 |
| poor_decision_hierarchy | 4 |
| poor_load_management | 2 |
| poor_context_interpretation | 1 |
| excessive_rigidity | 1 |
| missing_knowledge | 1 |

## Latest cycle — most-hit traps

- (1×) Partially: it prescribes a 40-45 min, 3x8-12 upper-body hypertrophy session in Peak week 1 (limited to upper body at RIR 2-3, so not a full-body session)
- (1×) Asking so many questions that nothing is actionable for tomorrow (partially: long staged question list and long branching section, though the session itself is concrete)
- (1×) Mild: stage 2 adds sets to the first three movements, although it is gated by recovery criteria and is not high volume
- (1×) Ignoring grip/elbow accumulation to a degree: two weighted pulling sessions per week at 4x3-5 each stack on 4 climbing days, and the elbow and tendon load of weighted pull-ups plus deadlifts is not directly discussed
- (1×) Partly: 'first change is the dose balance, not the structure' and 'a small, specific change' if he refuses to cut lean toward small tweaks, though the main recommendation is a block structure
- (1×) Writes three full hypertrophy sessions because three slots exist. Sessions 1 and 2 have 18–20 sets each, and session 3 has 14 sets plus a carry.
- (1×) Partially giving both the same Peak week 1 programme (support-only for both), despite opening with 'No'

## Hard failures in the latest cycle

- **ADV-038** — Prescribes about 52 sets of added volume across three sessions on top of 5 REVL sessions, with no volume count against REVL's weekly totals. This is the listed hard failure, so D scores 0–2 and H and C are penalised.
- **ADV-040** — Prescribes identical volume to both clients in Peak week 1 (support-only/no added work for both) — borderline; the response differentiates from Rebuild onward and hedges that the 47-year-old may get less

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

## Consistency contradictions — latest cycle

- **ADV-009** — The opening default says to "spend the hour on a short, upper-body-only hypertrophy session at RIR 2–3" while also saying "Peak is the wrong window for 'more muscle'" and that the dosing rule is "no additive strength work unless the PT work replaces a REVL strength day". The default is added hypertrophy volume, and the answer admits it is only "a mild stretch of the 'support only' cap" without showing that it replaces a REVL strength day.
- **ADV-009** — The headline default is "Skip it entirely in the testing weeks", yet the same answer prescribes a testing-week session of "activation, mobility, one light technique primer and recovery work", and the client has one PT hour a week. The 'skip' and the 'do something' instructions conflict.
- **ADV-009** — The answer states Peak is "three weeks, with weeks 2–3 as testing" and then offers a "heavy-wave week" as a separate third option. That leaves one non-testing week, but the plan is built as if the heavy-wave week might be any Peak week and asks the user to say which one it is.
- **ADV-009** — The progression rule "add about 5%" and the claim "expect maintenance more than visible growth" are stated without support, and the number is not labelled as general knowledge rather than course-derived. This is a mechanism or number stated as fact.
- **ADV-009** — "Peak has the least neural headroom of any phase" is stated as fact without citation, and it is the premise for the whole decision.
- **ADV-010** — "Allow some soreness in week 1 as the new routine settles" sits slightly awkwardly with the stance that soreness is not a marker, but it is framed as expected side effect, so this is minor.
- **ADV-010** — States as fact that "Her 'hard' sessions probably feel hard from novelty and fatigue, not from load" and that "When she repeats an exercise, the soreness drops even though the training is still effective" without support beyond a general-knowledge tag (the first claim has no tag at all).
- **ADV-010** — Cites specific course locations and numbers ("raise the load about 5% (Week 07 Ch 11 p7)", "Table 9-12, p16") while also admitting "I haven't opened the course pages this turn"; the sources are presented with page precision despite being unverified.
- **ADV-010** — Does not account for any existing REVL/class/concurrent training exposure before recommending to "Add sets on the lifts that are progressing" in Stage 2 (the client's concurrent training is never asked about in the open questions).
- **ADV-011** — "Start with one PT session a week... kept to roughly half a session in Build and none that is additive in Peak" conflicts with the default of "one PT session a week" and "4 sessions a week in total", since the stated default PT session is partly or fully removed in Build and Peak without saying what replaces it.
- **ADV-011** — "His own coached REVL Peak test can supply that 1RM once he confirms it happened" sits oddly beside "Testing week: Add nothing load-bearing" and the unknown phase, so the 1RM source is speculative and not yet established.
- **ADV-011** — "Novice or returning lifter: Build foundations (Movement phase)" and "Light technique work... RIR 3+" are prescribed before training age is known, while the plan itself says training age is unknown. This is a soft inconsistency that the staged branching mostly covers.
