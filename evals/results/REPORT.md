# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 379 trained-distribution runs, 0 generalization, 0 wildcard, across 33 cycles._

## Scoreboard — cycle 33 vs 32

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.91 | 3.80 | ↑ |
| Goal alignment | 3.98 | 3.50 | ↑ |
| Load management | 3.93 | 4.00 | ↓ |
| Recovery | 3.86 | 3.50 | ↑ |
| Individualisation | 3.79 | 3.50 | ↑ |
| Programming quality | 3.75 | 3.50 | ↑ |
| Safety | 4.14 | 5.00 | ↓ |
| Consistency (0-5) | 3.59 | 4.00 | ↓ |
| Benchmark overall | 3.91 | 3.80 | ↑ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **3** | 0 | ↓ |

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

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| I | exercise_selection | 3.68 |
| B | training_specificity | 3.73 |
| K | individualisation | 3.73 |
| D | volume_management | 3.77 |
| H | recovery_compatibility | 3.77 |
| J | progression | 3.82 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| insufficient_individualisation | 5 |
| poor_context_interpretation | 3 |
| excessive_rigidity | 1 |
| poor_load_management | 1 |
| poor_decision_hierarchy | 1 |

## Latest cycle — most-hit traps

- (1×) Partial: a fairly full upper-body session of about 14-16 sets, with calves and arms added, is on the heavy side for a client reporting chronic fatigue
- (1×) Partial: grip/elbow accumulation is acknowledged only through generic back-off triggers, while two weighted pull sessions plus rows are programmed without a grip-load rationale
- (1×) Used 'Russian squat protocol' / 'Russian squat wave' phrasing in the response, partly echoing the incorrect name
- (1×) Writes three full hypertrophy sessions (about 15, 15 and 8 working sets) as the default because three slots exist

## Hard failures in the latest cycle

- **ADV-026** — Possible unsupported REVL claim stated as fact: 'REVL already loads squat and hinge patterns on most training days', with no provenance label and no client statement
- **ADV-026** — Invented client information: the client is called 'her' although no gender was given, and 'her heaviest lower-body REVL day' implies schedule knowledge the client never gave
- **ADV-038** — Does not clearly trigger. Three sessions on top of 5 REVL is the stated hard failure, but the sessions are non-lower-body, partly low-axial and caveated, and the response says to cut Session C first if markers slip. Borderline, so no zero is applied, but C and D are capped at 3.

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

## Consistency contradictions — latest cycle

- **ADV-019** — "Tell him plainly that you want the shoulder assessed before more bench loading" and "Don't add PT bench or overhead pressing" sit alongside "Once he's released, progress bench... add roughly 5% when it's met". The 5% increment is stated without a known current load, training age, or REVL phase, and the plan admits "I don't know which phase he's in". This is a soft unsupported specific number, though it is hedged with "Check the exact page before citing it".
- **ADV-019** — "Ask him to flag it to his REVL coaches. They can scale pressing in class" treats REVL as something to modify while the plan elsewhere says the shoulder needs clinician clearance. It does not say whether he should keep doing REVL bench while waiting for the assessment, so the interim advice on his existing pressing exposure is left unresolved.
- **ADV-019** — "Carries, if they're pain-free for him" and "Lower-body and core work" are suggested as safe PT-time fillers before any assessment, while the plan says only a clinician can decide what is safe for the shoulder. Carries load the shoulder girdle isometrically, which slightly undercuts the "nothing shoulder-loading until assessed" stance.
- **ADV-019** — "Bench loads also climb toward near-maximal in Build and Peak" and the claim that the REVL reference lists the anterior shoulder as a local fatigue site are given as fact, while the plan admits it has not re-opened the supporting pages this turn. The page citations are hedged, but these claims are not.
- **ADV-020** — "Run those on a non-REVL day, or as a short block at the start of a session" sits uneasily with "The first job isn't adding volume" and with the stated 3x/week REVL schedule. It never says whether she has a PT session or a free non-REVL day, so the added work may not fit her schedule.
- **ADV-020** — It cites Table 14-2 "no sudden explosive moves" as a youth rule, then recommends a plyometric/landing progression for the same client. It does flag this as a judgement call, but it reads the rule as limiting only "maximal, uncontrolled work". That reading is an interpretation of a course line it has just quoted as a ban.
- **ADV-020** — It says "at 17, her growth plates may or may not be fully closed. You can't confirm that", but also says "The course says 1RM isn't appropriate for her age" and tells the parents "A 1RM test brings injury risk". The first is hedged and the second two are stated as certain for her.
- **ADV-020** — It states "ACL risk in female athletes is a real issue" and "A 1RM test... only a rough link to jumping" with no source. The first is labelled general knowledge and the second is not labelled.
- **ADV-021** — "Zone-2 cardio, which also covers the course's ≥5 d/wk moderate-activity recommendation" is offered as a bolt-on, but the plan is built on a 2-day floor. Bolt-ons only happen on available days, so the ≥5 d/wk target is not met on the weeks he can make only 2 sessions.
- **ADV-021** — "If it's hypertrophy or max strength, the 2-day core matters more" sits badly with the earlier claim that two full-body days meet the baseline. Two sessions a week is a thin dose for hypertrophy or max strength. The plan also says it will not add a max-strength protocol, so the line gives no guidance.
- **ADV-021** — "Ask him which number is real" and "Set the plan to the lower, reliable number" conflict with the opening default of a 2-day floor. The default is fixed before any attendance data is checked. The later line "he's a 2–3 day client" then implies a third session should be core, not a bolt-on.
- **ADV-021** — "Bolt-ons stay at RPE ≤6–7" conflicts with "a third full-body session at lower volume or RPE, or a split day aimed at his weak point". A split day aimed at a weak point implies real volume. The plan also gives no check on total weekly load across 6 days.
