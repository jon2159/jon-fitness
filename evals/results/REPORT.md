# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 162 trained-distribution runs, 0 generalization, 0 wildcard, across 16 cycles._

## Scoreboard — cycle 16 vs 15

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.85 | 3.53 | ↑ |
| Goal alignment | 4.00 | 3.67 | ↑ |
| Load management | 3.97 | 3.17 | ↑ |
| Recovery | 3.75 | 3.17 | ↑ |
| Individualisation | 3.81 | 3.67 | ↑ |
| Programming quality | 3.44 | 3.83 | ↓ |
| Safety | 3.75 | 4.33 | ↓ |
| Consistency (0-5) | 4.12 | 4.00 | ↑ |
| Benchmark overall | 3.85 | 3.53 | ↑ |
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

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| I | exercise_selection | 3.38 |
| J | progression | 3.50 |
| H | recovery_compatibility | 3.62 |
| B | training_specificity | 3.75 |
| K | individualisation | 3.75 |
| N | safety_caution | 3.75 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_decision_hierarchy | 2 |
| insufficient_individualisation | 2 |
| missing_knowledge | 1 |
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Partially: 'Don't touch the lifting structure' and 'about 1 class a week or 3 lower-effort classes' hedge toward small tweaks; the lifting load (4 full-volume heavy days) is left untouched even though structure is part of the problem

## Hard failures in the latest cycle

- **ADV-008** — Cited specific REVL session-pattern statistics ('squat patterns ~73%, hinge ~74%, unilateral ~64%' labelled '(REVL data)') presented as fact — these precise figures were never supplied in the scenario and read as a fabricated/unverifiable protocol detail dressed up with a citation, triggering the rubric's automatic-0 rule for asserting a specific REVL number as fact when it was never supplied

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

## Consistency contradictions — latest cycle

- **ADV-002** — The plan states 'the usual first-line answer at this volume is to reduce session count or shorten a session, not add more' and identifies PT as the only available flex point, but the default plan still prescribes 3 full, unshortened PT sessions and only holds the reduction option in reserve for if fatigue markers appear — the acknowledged best-practice response isn't actually applied by default, only offered as a reactive fallback.
- **ADV-002** — The claim that hip thrusts involve 'no spinal loading' is stated as settled fact to justify treating them as a distinct pattern from barbell hinge, but a loaded hip thrust still transmits substantial compressive/shear force through the lumbar spine via the loaded pelvis/trunk position — this is an overstated physiological claim used to license additional posterior-chain volume.
- **ADV-005** — Cites a specific numeric claim ('25 sets/week is already at the upper end of what most trained lifters can productively recover from') as general knowledge without a concrete source, which is a soft, self-flagged instance of contradiction #10 even though it's explicitly labeled as non-ISA general knowledge.
- **ADV-005** — The recommendation says the current split composition is 'still open' and unknown, yet earlier states as a near-certainty that adding a 7th day is 'very likely the wrong lever' and 'none of them point toward add a day' — slightly overclaiming the conclusion given the acknowledged missing data on how muscle groups are distributed across the 6 days.
- **ADV-008** — Closes by saying 'Training age / injury history / medical clearance status — none of this is screened yet, and it should be before anything goes on paper as a program' — yet the same message already puts a specific program on paper (exercise selection, 2-3 sets x 8-15 reps, RIR 3-4, 30-90s rest, placement rules, load exclusions) under 'Default recommendation.'
- **ADV-008** — Frames the prescribed dose as deliberately kept sub-maximal 'which is the lever that keeps this maintenance rather than a real overload stimulus,' then in the same breath prescribes a 'Progression trigger: double progression within the rep range week to week' — progressive overload logic sitting awkwardly against the 'maintenance, not overload' framing, even though RIR 3-4 + double progression is a defensible combination.
- **ADV-016** — "the course's own progression logic only works if effort is adequate... Right now I don't know that" is asserted with page citations (Wk07, Ch11, p7, p19–20) while the same message labels its framework as "general knowledge, not course content", a mild mixing of sourced and unsourced claims.
- **ADV-016** — "At 3 years' training age, a stalled squat is very often technical... rather than a programming problem" is stated as a fact/frequency with no support, and it slightly undercuts the stated position that the cause is unknown until diagnosed.
- **ADV-016** — "Hold the current programme" as the default is at mild tension with the claim that the programme itself may be the constraint ("I can't tell whether the program is the constraint"), and with a client who has been stuck 4 months on it; the recommendation to keep running it is not justified beyond the short diagnostic window.
- **ADV-031** — It says "Keep sets, reps, weekly frequency and rest exactly as they are" and "keep 3×8", yet also says to reset new variants to "about 8 reps with 2–3 reps in reserve" and to "drop the load 5–10%". These are load adjustments, not changes to sets or reps, so the tension is mild. Still, it calls this "change one thing" while swapping variants in four patterns at once, and it says a stall means "drop the load 5–10%" without saying whether that applies to the variant swap.
- **ADV-031** — It states "add about 5% (Week 09, Ch 9, p7)" and "2 reps or more in reserve" as a course-cited trigger, yet earlier says the recommendation is "applied from the course, plus general-knowledge coaching judgement". It does not separate which numbers (5% jump, 5–10% drop, 4–6 week rotation, 2 consecutive stalled sessions) come from the course and which are its own. This is unsupported mechanism or number stated as fact (item 10).
- **ADV-031** — It says the client is "not stalled" and that boredom "is not a sign it has stopped working", yet its first requested item asks whether "the bar weight [is] still rising, or are reps and RPE drifting". It has already concluded the programme is working before checking that data. This is a soft internal tension, though it is framed as a default pending confirmation.
