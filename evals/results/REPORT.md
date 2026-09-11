# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 54 trained-distribution runs, 0 generalization, 0 wildcard, across 4 cycles._

## Scoreboard — cycle 4 vs 3

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.41 | 3.53 | ↓ |
| Goal alignment | 3.83 | 3.87 | ↓ |
| Load management | 2.98 | 3.22 | ↓ |
| Recovery | 3.40 | 3.93 | ↓ |
| Individualisation | 3.63 | 3.80 | ↓ |
| Programming quality | 3.70 | 3.23 | ↑ |
| Safety | 2.67 | 2.93 | ↓ |
| Consistency (0-5) | 3.53 | 3.33 | ↑ |
| Benchmark overall | 3.16 | 3.89 | ↓ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **14** | 16 | ↑ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |
| 3 | 20260910T223924Z | 15 | **3.53** | 3.87 | 3.22 | 3.93 | 3.80 | 3.23 | 3.80 | 2.93 | nightly |
| 4 | 20260911T144031Z | 15 | **3.41** | 3.83 | 2.98 | 3.40 | 3.63 | 3.70 | 3.73 | 2.67 | nightly |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| N | safety_caution | 2.67 |
| E | intensity_management | 2.87 |
| C | total_training_load | 2.93 |
| D | volume_management | 3.00 |
| F | frequency_management | 3.13 |
| K | individualisation | 3.27 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_decision_hierarchy | 4 |
| poor_context_interpretation | 4 |
| missing_knowledge | 3 |
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Adds a 7th training day (dressed up as 'gap-filling' rather than 'more of the same') instead of evaluating whether it should replace an existing solo session
- (1×) Never engages with the substitution option at all, despite having just built the case (budget already near ceiling) that would make substitution the obvious next question
- (1×) Effectively still lands on prescribing a whole new programme structure (linear periodization strength block, V5 9-week variant) despite the diagnostic framing — the 'diagnosis' functions more as a rationale for why a new programme is justified than as a genuine fork where a smaller fix could win
- (1×) Partially falls into 'programming to old level rather than current level' — treats his return-to-training status as a volume/frequency question only, without adjusting initial loading/RIR for detraining
- (1×) Frequency/spacing guidance ('avoid loading her squat within ~48h of Monday/Wednesday') is built on invented REVL day-structure facts rather than checked frequency, so the 'checked existing frequency' trap is only superficially avoided

## Hard failures in the latest cycle

- **ADV-015** — Adds a 7th training day without ever considering substitution as an alternative — rubric-defined hard failure; C and F scored 0
- **ADV-015** — Presents specific, precise REVL programme statistics (100% of Mondays are hinge, squat on 73% of sessions, carries 11%, rotation 15%, horizontal pull 39% concentrated Fri/Sun, bench 35–54%) as established fact when none of this was supplied in the scenario and no citation/source is given for these numbers — auto-zero trigger under rubric ('asserting a specific REVL/other-programme number as fact when it was never supplied'); K and N scored 0
- **ADV-016** — The response identifies 'missing periodization' as the cause without any data confirming the current programme actually lacks periodization or planned variation — this is an assumption dressed as a diagnosis, then used to justify a full new programme (V5, 9-week wave). It does not first attempt a targeted change (add periodization to the existing lifts, adjust volume/intensity waves) before recommending a new programme; it goes straight to a full block replacement. This is the core trap: 'Change the entire programme without identifying the limiter' — the limiter is asserted, not identified from client data.
- **ADV-017** — Asserted specific REVL programme statistics as fact that were never supplied by the client or scenario ('squat pattern appears in 73% of all REVL sessions, hinge in 74%, unilateral lower in 64%', 'hinge... 51% of all sessions', 'rotation/anti-rotation... 15% of sessions', sourced to 'OCR'd session data across 363 REVL classes') — this is exactly the rubric's auto-0 trigger for asserting an unsupplied REVL/programme number as fact
- **ADV-017** — Asserted a specific REVL weekly day-by-day schedule as fact ('barbell hinge on virtually every Monday', 'Wednesday...the densest mixed squat+hinge+Olympic day', 'Friday...the lower-body offload day') despite explicitly admitting two paragraphs later that the client's actual 5-day split and Perform/Move track are unknown — internally inconsistent and fabricated
- **SC-0018** — Asserted a specific REVL protocol detail as fact: 'REVL Volume phase = 8–14 reps @ ~40–65%' — not supplied by the client or scenario
- **SC-0018** — Cited numerous precise, unverifiable chapter/page/table references (Table 9-12/11-10, Wk07 Ch11 p16/p29-31, Wk01 Ch1 p7-8, Wk02 Ch2 p10-11, §4-§15) presented as established fact
- **SC-0018** — Invented specific REVL movement-pattern-distribution statistics (squat 74%, hinge 76%, horizontal pull 39%, carries 12%, rotation/anti-rotation 15%, vertical pull 43%) that were never given in the scenario
- **SC-0019** — Asserted a specific REVL Volume-phase load range ('~40–65% 1RM') as fact, backed only by an unverifiable section citation — this is exactly the fabricated %1RM/protocol-detail failure the rubric flags as an automatic 0, regardless of citation dressing
- **SC-0019** — Invented that Monday and Wednesday are Elena's 'heaviest hinge/squat days' — no such schedule was given by the client; this fabricated detail was then used to justify future session placement
- **SC-0020** — Asserts a specific REVL Volume-phase load range ('loads sit ~40-65%') as fact, cited to a document, when this was never supplied by the client — explicit rubric hard failure
- **SC-0020** — Asserts precise REVL session-composition percentages (barbell hinge 100%/71%/73%/51%, horizontal pull 39%, carries 12%) as fact with section citations — these figures were never given in the scenario and read as fabricated protocol detail, not a genuine count
- **SC-0022** — Asserts specific REVL Volume-phase parameters as established fact never supplied in the scenario: '8–14 reps at ~40–65% 1RM', plus multiple precise session-frequency percentages (squat 73%, hinge 74%, Monday hinge 100%, hinge 51%, session density 72%, horizontal pull 39%, carries 11%, rotation 15%) presented without hedging as documented fact rather than labelled likely/unverified. This is the exact hard failure named in the scenario ('Assert a specific REVL load/%/rep count as fact').
- **SC-0023** — Asserts specific, unsourced REVL programming statistics as fact (squat pattern in '73% of REVL sessions', hinge '100%' on Monday, squat '50%' on Wednesday, unilateral work '61%', rotation '15%', carries '11%') — none of this was supplied by the client, and the response later admits it does not know her REVL days/track, directly contradicting the certainty of the earlier claims. This matches the rubric's explicit auto-0 trigger: 'asserting a specific REVL/other-programme number as fact when it was never supplied.'

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |
| 3 | 7 | 3.89 |
| 4 | 7 | 3.16 |

## Consistency contradictions — latest cycle

- **ADV-015** — The response lists explicit gating questions it says are needed 'before green-lighting 7 days' (bodybuilding split, session placement relative to REVL, performance-trend/sleep changes), then proceeds in the same answer to fully prescribe the 7th session's exercises, sets/reps/RIR and placement — effectively answering the question it just said it couldn't yet answer.
- **ADV-015** — It recommends placing the new session 'away from Monday and Wednesday... ideally the day after Perform Upper or after a Sweat Engine session,' but elsewhere admits it doesn't know 'which day of the week does your session land relative to his REVL schedule,' so it can't actually confirm that placement is available in the remaining single open day.
- **ADV-015** — The frequency argument used to justify going to 7 training days only addresses per-muscle-group rotation ('2-3 hard sessions/week, 48-72h apart'); it never addresses that 4 REVL + 2 bodybuilding + 1 new session fills every day of the week with zero full rest days, which is a systemic/CNS recovery question the muscle-specific budget logic doesn't cover.
- **ADV-015** — It states 'his lower body and axial loading are very likely already at or past that ceiling before you touch him' — a fairly strong overreach/at-risk claim — yet the only concrete action tied to that risk is 'keep an eye on... recovery markers over the next few weeks,' with no interim adjustment to the 6 days already in place.
- **ADV-017** — Argues the lower body is already saturated and 'never truly fresh' from REVL alone (squat 73%, hinge 74%, unilateral 64% of sessions, 'no day in a full week leaves the lower body unloaded'), yet still adds two new dedicated glute-focused hypertrophy sessions (barbell hip thrust 3–4x8-12 RIR2-3, single-leg RDL, pull-through, etc.) for that same muscle group — the 'different expression, not more volume' framing reframes the fatigue rather than accounting for it.
- **ADV-017** — Gives specific day-based placement advice as if her real schedule is known ('Avoid adding lower-body work within ~48h of Monday... or Wednesday... Favorable windows are Friday') but then states 'I don't know her actual 5-day REVL split (which days, Perform vs. Move)' — the day-specific logic is built on an assumed generic REVL calendar, not her actual days.
- **ADV-017** — Prescribes concrete equipment-dependent exercises (barbell hip thrust with pad, cable pull-through, standing cable hip abduction) as the illustrative plan while still listing 'available equipment (barbell + pad, bands, cable)' and 'technique competence' as an open screening question to be asked afterward.
- **ADV-020** — The quoted rule bans both things equally — "NO 1RM lifts, no sudden explosive moves, or compete with other children" — yet the recommendation treats only the 1RM half as an absolute bar while prescribing a repeated maximal-effort vertical jump test ("the single most direct proxy... carries none of the loaded-max risk") and plyometrics as the core replacement, without explaining why a maximal jump or plyometric drill isn't itself a 'sudden explosive move' under the same cited clause.
- **ADV-020** — It notes REVL already has 'Olympic/ballistic work' in 55-56% of her sessions but only uses that fact to argue against adding more volume on top, never flagging it against the same youth 'no sudden explosive moves' guideline it invoked minutes earlier to hard-ban 1RM testing — the rule is applied strictly to one modality and silently ignored for another she's already doing 3x/week.
- **ADV-020** — It prescribes concrete beginner/intermediate plyometric contact-volume numbers (80-100 vs 100-120) before determining her training age or REVL phase, slightly ahead of its own stated position that programming specifics can't be finalized until that information is in hand.
- **ADV-021** — The plan justifies ditching a fixed split by invoking 'the frequency guideline is 2–3 d/wk per muscle group with 48–72 h recovery between sessions hitting that muscle group (Week 07, Ch 11, p11)', yet its own Tier-1 design has him hit squat/hinge, push, pull, and single-leg patterns in 'every session' up to 6 days a week — which means ~24h between hits on the same patterns, violating the very 48–72h recovery rule cited as the reason to abandon splits, and doing so more severely than the split it replaces.
- **ADV-021** — Recovery spacing is explicitly solved for the 2-session floor case ('still spaced for the 48–72 h recovery rule... pick which 2 calendar days, not just the first 2 on the schedule') but the plan never addresses how the 6-day full-body version complies with that same rule, leaving the high-frequency end of the scale unresolved by the plan's own stated logic.
