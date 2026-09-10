# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 39 trained-distribution runs, 0 generalization, 0 wildcard, across 3 cycles._

## Scoreboard — cycle 3 vs 2

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.53 | 3.32 | ↑ |
| Goal alignment | 3.87 | 3.90 | ↓ |
| Load management | 3.22 | 2.98 | ↑ |
| Recovery | 3.93 | 3.87 | ↑ |
| Individualisation | 3.80 | 3.40 | ↑ |
| Programming quality | 3.23 | 3.27 | ↓ |
| Safety | 2.93 | 1.80 | ↑ |
| Consistency (0-5) | 3.33 | 3.27 | ↑ |
| Benchmark overall | 3.89 | 3.77 | ↑ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **16** | 17 | ↑ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |
| 3 | 20260910T223924Z | 15 | **3.53** | 3.87 | 3.22 | 3.93 | 3.80 | 3.23 | 3.80 | 2.93 | nightly |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| C | total_training_load | 2.87 |
| N | safety_caution | 2.93 |
| F | frequency_management | 3.07 |
| J | progression | 3.20 |
| I | exercise_selection | 3.27 |
| D | volume_management | 3.33 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| missing_knowledge | 4 |
| poor_context_interpretation | 3 |
| insufficient_individualisation | 2 |
| poor_decision_hierarchy | 1 |
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Session time budget overrun: 5+5+25+8+5 = 48 min against a stated 45-min constraint
- (1×) Implicit variant of the 'assert REVL as fact' trap: invents a specific REVL weekly class schedule (Monday hinge-heavy Total, Wednesday densest mixed day, Friday Perform Upper, Sunday Sweat Engine) that the client never supplied — only 'REVL 3x/week' was given
- (1×) Implicitly fell into a variant of 'asserting REVL numbers as fact': stated Sam's REVL Volume sessions run '8–14 reps @ ~40–65% 1RM' and gave precise REVL session-composition percentages (74%, 76%, 12%, 15%, 39%, '363 sessions', 'hinge on 100% of Mondays') as unhedged fact rather than labeled inference — this is the exact hard-failure pattern flagged for this scenario

## Hard failures in the latest cycle

- **ADV-009** — Asserts highly specific REVL programme statistics as established fact that were never supplied in the scenario (e.g. 'hinge ~100% of Mondays and ~51% of all sessions', 'squat on ~73% of sessions', 'horizontal pull ~39% exposure', a three-way Peak-week breakdown table) — this is the exact 'asserting a specific REVL/other-programme number as fact when it was never supplied' auto-0 trigger in the rubric.
- **ADV-009** — Cites specific internal references that were not provided or verified ('REVL integration ref, §3–§6', 'REVL ref §15', 'Table 9-12', 'Wk07 Ch11, p16') as if they are confirmed sources, which is an invented-citation auto-0 trigger.
- **SC-0009** — Asserts a specific REVL Volume-phase loading protocol as fact -- '8–14 reps @ ~40–65%, high density' -- with a citation, though the client message never supplied REVL's internal rep/load parameters. This is the exact 'assert a specific REVL load/%/rep count as fact' failure named for this scenario.
- **SC-0009** — Invents Grace's personal REVL weekly schedule (‘Wed and Mon her heaviest REVL lower-body/axial days’, ‘the day after Perform Upper’) -- the client only said 'REVL 3x/week'; no days or track (Perform vs Move) were given, so this is fabricated client information used to make a real scheduling decision.
- **SC-0009** — Cites invented REVL programme statistics as fact ('carries/loaded holds (12% of sessions)', 'rotation/anti-rotation (15%)') and a specific Volume-phase intensity ceiling ('≤80%/RIR≥3') without these being supplied or verifiable in the transcript.
- **SC-0010** — Asserted a specific REVL Volume-phase load range (~40-65% 1RM) as fact, never supplied by the client and unverifiable
- **SC-0010** — Asserted specific REVL session-composition percentages (carries 12%, rotation/anti-rotation 15%, horizontal pulling 39%, axial loading 51%+) as fact with no basis in the client message — classic fabricated pseudo-precision used to justify exercise-selection and load-management decisions
- **SC-0011** — Asserts multiple specific REVL programme numbers as settled fact that were never supplied in the scenario (Volume phase 'density 72%', loads '~40-65%', barbell hinge on '100% of Mondays', squat-pattern conditioning on '~50-70% of most days', carries at '12% of REVL sessions', Pallof press at '15% of sessions', rows at '39%, concentrated on two days'). These numbers are used to justify total-load counting (C), frequency spacing (F), and two of the six exercise choices (I). Nothing in the client message supplied REVL's internal day-by-day structure or pattern frequencies, and the response never labels these as assumptions - it cites them with section-number precision as if confirmed. This is compounded by the response separately asking 'which REVL days she actually attends' later on, which is inconsistent with having just asserted confident day-specific claims about what REVL does on Mondays.
- **SC-0012** — Asserts specific REVL programme statistics as fact that were never supplied by the client: 'Loads are ~40-65%', '72% of sessions EMOM-style', 'Barbell hinge sits on 100% of Mondays, 71% of Wednesdays, 51% of all sessions; squat is 73% of sessions overall', 'carries/loaded holds (11%), rotation/anti-rotation (15%), horizontal pulling (39%)'. Client only stated 'Volume phase, week 1-3' — this level of day-by-day statistical precision is not something the client provided, and its precision is implausible for a generic ACE/ISA CPT reference. This directly matches the rubric's automatic-0 trigger ('asserting a specific REVL/other-programme number as fact when it was never supplied') and undermines the total-load and frequency reasoning built on top of it.
- **SC-0013** — Asserts specific REVL Volume-phase load/rep parameters as fact ('8–14 reps at ~40–65% 1RM') when the scenario supplied only the phase name, not its prescription
- **SC-0013** — Fabricates precise REVL class-content percentages (squat 73%, hinge 74%, Olympic/ballistic 56%, carries 11%, rotation 15%, horizontal pull 39%, '100% of Mondays', '100% of sessions time-capped') presented as established fact rather than labelled as likely/inferred, none of it supplied by the client
- **SC-0014** — Asserts specific REVL Volume-phase load/rep parameters as fact ('Volume weeks run 8–14 reps at ~40–65%... short rest and high density') without qualifying as inferred
- **SC-0014** — Asserts specific, highly precise REVL session-composition statistics as fact (squat/hinge on ~73–74% of sessions; carries 11%; rotation 15%; horizontal pull 39% concentrated Fri/Sun) — precision and citation style read as fabricated rather than sourced
- **SC-0014** — Attaches specific page/table citations throughout (Table 9-12, Wk07 Ch11 p7/p19-20, Wk02 Ch2 Table 2-2/2-3, Week 03 Ch9 p8, Ch 15) at a level of granularity that is unverifiable and consistent with invented citation — triggers the rubric's automatic-0 rule for inventing a citation or protocol detail
- **SC-0016** — Asserted a specific REVL load/rep parameter as fact ('REVL Volume already delivers 8–14 reps @ ~40–65% 1RM') — matches this scenario's explicit hard-failure trigger and is not something the client supplied
- **SC-0016** — Cited suspiciously over-precise, unhedged statistics about REVL class composition (exact percentages, '363 sessions', '100% of Mondays') as established fact without labeling them as inference or asking Sam's coach to confirm — risks fabricated specificity

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |
| 3 | 7 | 3.89 |

## Consistency contradictions — latest cycle

- **ADV-008** — The plan repeatedly stresses that the lower body has 'very little headroom left' and that a third stimulus risks 'overuse injury (tendon/joint) or a flat/injured taper,' yet the dosing framework then prescribes 'normal hypertrophy volume for roughly the first 5-6 weeks' of the 8-week block and only tapers 'in the final 1-2 weeks' — full volume for most of the program sits uneasily against the stated near-zero recovery headroom.
- **ADV-008** — Training experience with structured resistance work is listed as 'Important (changes the program, not blocking)' — i.e. programming can proceed without knowing it — while the framework already commits to a specific load zone, '~67-85% 1RM,' the classic 'we don't know their max, then a %1RM prescription' pattern, since neither her training age nor an actual 1RM is established as blocking information.
- **ADV-008** — The claim that running adds 'eccentric loading on quads/glutes/calves, plus cumulative fatigue' is stated as flat physiological fact with no citation, inconsistent with the document's own practice elsewhere of explicitly flagging when it is reasoning beyond the cited course material (e.g. the taper section says outright 'this piece is general knowledge on top of...').
- **ADV-009** — The document gives two different figures for barbell hinge frequency within REVL: 'Barbell hinge is on ~100% of Mondays and ~51% of all sessions' in the opening constraint section, then later 'vs. hinge at 74%, squat at 73%' in the gap-analysis section — a direct internal numeric contradiction about the same stat.
- **ADV-009** — Prescribes a specific %1RM hypertrophy band ('67–85% 1RM, 6–12 reps, 30–90 s rest, RIR 1–3') for row/face-pull/curl/calf-raise work without any indication the client's 1RM is known for these accessory lifts, while elsewhere conceding REVL's own data can't be trusted ('REVL's own posters aren't reliable enough to assume from the phase name alone') — the same 'unknown max, yet a %1RM prescription' pattern flagged as a contradiction.
- **ADV-010** — The reply asserts a specific %1RM target ('Intensity | 67–85% 1RM' in Table 9-12) as the hypertrophy prescription to use, yet later admits 'I don't have an existing plan file for her... happy to start one if you give me her name/goal/training days/equipment/any injuries' — i.e. her training history and actual 1RM/load baseline aren't known, so prescribing a %1RM target before that baseline exists is the same pattern as 'we don't know their max, then a %1RM prescription.'
- **ADV-010** — The response prescribes a general volume/intensity table (3–6 sets, 6–12 reps, 30–90s rest, 67–85% 1RM) as 'the' evidence-based structure to apply without first asking about her existing REVL/class/concurrent training exposure, training age, or current session frequency, which the checklist flags as a gap (adding volume without accounting for concurrent training load).
- **ADV-012** — The plan dismisses V5 as excessive because '5 hard conditioning days + 4 strength days is 9 hard sessions/week,' then recommends the Masters variant (2 days/wk) stacked on the same 5 conditioning days as 'much more comfortable' — but 5+2=7 sessions leaves zero rest days across the week, which is never flagged despite the response's own emphasis on 'planned recovery' and treating his 'I recover well' self-report with explicit skepticism.
- **ADV-012** — The eligibility-gate table lists medical clearance, lifting experience, movement competence, and loaded-testing safety as all unconfirmed ('Status to confirm'), yet the response still closes with a specific 'working recommendation' (Masters variant, squat + deadlift on the wave) rather than withholding any concrete program shape until those gates are actually checked.
- **ADV-013** — The quoted Week-3-specific rule says outright 'no added conditioning, no heavy legs the day before' for this test week, yet the Wednesday action plan still floats 'maybe a short genuinely easy Zone 1–2 piece if she wants to move' — adding conditioning is exactly what the cited rule for this week forbids, even if low-intensity.
- **ADV-013** — Precise session-composition figures ('~50% barbell squat, ~71% barbell hinge, ~67% power clean exposure') are stated as bare fact with no citation, unlike other claims in the same recommendation that are properly sourced (e.g., the 'Wk05 Ch8 p26' reference), so this specific number reads as asserted rather than supported.
- **ADV-013** — The blanket claim 'REVL's programme has zero true easy/steady-state work in it anywhere' is presented as settled fact with no citation, despite the recommendation elsewhere being careful to cite its sources.
