# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 530 trained-distribution runs, 0 generalization, 0 wildcard, across 46 cycles._

## Scoreboard — cycle 46 vs 45

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.89 | 3.93 | ↓ |
| Goal alignment | 3.94 | 4.00 | ↓ |
| Load management | 3.89 | 3.50 | ↑ |
| Recovery | 3.94 | 4.00 | ↓ |
| Individualisation | 3.69 | 4.00 | ↓ |
| Programming quality | 3.75 | 4.00 | ↓ |
| Safety | 4.19 | 4.00 | ↑ |
| Consistency (0-5) | 3.62 | 3.00 | ↑ |
| Benchmark overall | 3.89 | 3.93 | ↓ |
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
| 43 | 20261007T175713Z | 7 | **4.02** | 4.29 | 4.11 | 3.93 | 3.71 | 4.07 | 3.86 | 4.14 | ramp-targeted |
| 44 | 20261007T181757Z | 24 | **3.89** | 3.88 | 4.00 | 3.88 | 3.67 | 3.71 | 4.12 | 4.17 | ramp-ref-broad |
| 45 | 20261007T232502Z | 1 | **3.93** | 4.00 | 3.50 | 4.00 | 4.00 | 4.00 | 5.00 | 4.00 | probe-d |
| 46 | 20261008T012804Z | 16 | **3.89** | 3.94 | 3.89 | 3.94 | 3.69 | 3.75 | 4.06 | 4.19 | ramp-ref-broad2 |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| I | exercise_selection | 3.56 |
| K | individualisation | 3.62 |
| B | training_specificity | 3.69 |
| F | frequency_management | 3.69 |
| L | practicality | 3.75 |
| D | volume_management | 3.81 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_load_management | 3 |
| insufficient_individualisation | 2 |
| poor_decision_hierarchy | 1 |

## Latest cycle — most-hit traps

- (1×) Mild: the planned full dose of 14-16 hard sets by week 3 drifts toward the high-volume trap for a client who says they are destroyed every week
- (1×) Heavy pulling stacked on 4 climbing sessions: 4x3-5 weighted pull-ups, 3x3-5 weighted pull-ups, and 3x5 heavy rows each week. The reps are low, not hypertrophy-range, but this is still duplicated pulling load.
- (1×) Grip and elbow accumulation is only partly addressed. Fingers are excluded, but weighted pull-ups, rows, deadlifts and leg raises all load grip and forearms with no management of that.
- (1×) Partial: recommends a default 2-day squat plan before the gate is confirmed, though it is hedged as provisional and the gate is required before it becomes a block
- (1×) Minor: suggests 'easy mobility that doesn't aggravate the back' in the PT-session section, a mild brush with the mobility-for-undiagnosed-pain trap, though it is conditional and non-prescriptive
- (1×) Partial: offers a 'smallest-change alternative' that keeps all 7 sessions and only tweaks them, though it is flagged as weaker and a fallback only
- (1×) Partially: Stage 2 offers to add 1-2 hard sets, a conditional route to 'harder' sessions, though gated behind rising loads and RD input

## Hard failures in the latest cycle

- **ADV-029** — Borderline on 'add high-volume pulling and grip work to a 4x/week climber': the pulling is low-rep and moderate in volume, about 10 hard pull sets per week, so it is not clearly high-volume. It is still a heavy vertical and horizontal pull stack with grip-intensive deadlifts. This is not scored as an automatic 0, but it is penalised under I and G.

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
| 44 | 24 | 3.89 |
| 45 | 1 | 3.93 |
| 46 | 16 | 3.89 |

## Consistency contradictions — latest cycle

- **ADV-025** — Power work is placed in every session at '3×3–5, full recovery' as 'low box jumps or squat-jump-to-stick' from week 1, while the plan also says landing technique must be clean before progressing and offers a fallback 'If she can't land quietly'. Prescribing jumps up front before any landing assessment is a soft tension.
- **ADV-025** — The plan says 'Selectorized machines mostly train one plane, supported, and on two legs... the plan has to include unsupported, unilateral and fast work.' Yet the Stage 1 table is mostly supported, bilateral machine work. Only the step-up and the single-leg leg press are unilateral, and the stage 3 text admits 'progress on speed and single-leg work will plateau sooner.' The plan therefore only partly delivers what it says is required.
- **ADV-025** — Two different progression triggers are given for strength: 'top of the rep range at 2 RIR on two consecutive sessions' in Stage 1 and 'can do 2 extra reps on the last set for 2 consecutive sessions, raise the load about 5%' in the progression trigger. They are not reconciled and could fire at different times.
- **ADV-025** — 'Hold the plan until [screening] is resolved' as a blocking gap conflicts with delivering a full default prescription with loads, sets and reps, without any note that these are provisional pending screening.
- **ADV-025** — The mechanism claim that 'Staying on machines alone will cap the goal' and the 'plateau sooner' claim are stated as fact. They are flagged neither as general knowledge nor as course-supported, and the general-knowledge list names only the timeline, the RIR cue and the intimidation approach.
- **ADV-026** — "Rebuild has headroom similar to Volume: low-to-moderate loads, mostly effort-based. That means a new PT progression can start now" is stated as a fact-like basis for adding volume while the client feels "destroyed every week" and the same plan says the "mechanism is recovery, not training stimulus"; it also admits "I don't know their REVL loads" and lists "which week of Rebuild they're in" as unconfirmed.
- **ADV-026** — "Treat sleep and 'destroyed' days as the limiting factor" and "more hard sets would make that worse" sit next to a plan that adds 8–10 hard sets in weeks 1–2 and ramps to "about 14–16 sets by week 3" as a default, so recovery is called compromised but volume is still increased.
- **ADV-026** — The "14–16 sets" full dose is a PT-session number, yet the plan says the hypertrophy band is "a ceiling for REVL plus PT combined"; no REVL weekly set total is estimated to show 14–16 extra sets fits under that ceiling, so existing REVL exposure is not actually accounted for.
- **ADV-026** — "Ask them to move towards 7h or more" and "Sleep is the biggest lever" are presented as established, while the only stated sleep data point is 6h and the plan says it cannot verify the course citations ("haven't re-opened the pages this turn"). The course-supported label is therefore applied to an unverified claim.
- **ADV-026** — "Check they felt 'okay' or better at REVL that week" is the gate for stepping up, but the client's baseline is already "destroyed" every week, so the trigger is vague and may never be met, or may be met trivially. It also conflicts with "Stay at the current dose if... session readiness was poor."
- **ADV-026** — "That's 5 sessions a week, below the ~7 where I'd force a cut" uses a threshold with no stated support, and a 5-session week is the stated source of the "destroyed" feeling.
- **ADV-027** — The plan says to start at "around 40–50% 1RM" and in the same section "No 1-RM testing. Use RPE and rep-based progression", so it prescribes a %1RM load for a client whose 1RM is unknown and will not be tested.
