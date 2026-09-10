# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 24 trained-distribution runs, 0 generalization, 0 wildcard, across 2 cycles._

## Scoreboard — cycle 2 vs 1

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.32 | 4.59 | ↓ |
| Goal alignment | 3.90 | 4.72 | ↓ |
| Load management | 2.98 | 4.61 | ↓ |
| Recovery | 3.87 | 4.72 | ↓ |
| Individualisation | 3.40 | 4.39 | ↓ |
| Programming quality | 3.27 | 4.50 | ↓ |
| Safety | 1.80 | 4.56 | ↓ |
| Consistency (0-5) | 3.27 | — | — |
| Benchmark overall | 3.77 | — | — |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **17** | 1 | ↓ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| N | safety_caution | 1.80 |
| C | total_training_load | 2.67 |
| K | individualisation | 2.67 |
| D | volume_management | 2.73 |
| F | frequency_management | 2.93 |
| J | progression | 3.07 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_context_interpretation | 4 |
| missing_knowledge | 4 |
| poor_load_management | 2 |
| poor_decision_hierarchy | 2 |

## Latest cycle — most-hit traps

- (1×) Effectively still gave the client a 'hard' session (4 rounds, minimal rest, continuous work, explicitly described as feeling 'hard and satisfying') — just with different exercise selection than 'conditioning', which caves to the underlying request the response itself argues against
- (1×) Effectively fell into the 'assert unverified programme specifics as fact' trap: invents precise REVL load/rep/% and pattern-distribution numbers (and a '13-week block' length) that were never supplied, dressed up with section/page citations
- (1×) Partial: attempts to space PT squat work from REVL squat-heavy days, but the day-by-day spacing decision (Wed/Fri/Sun) is built on invented REVL schedule data rather than confirmed client information — undermines an otherwise-correct instinct
- (1×) Fabrication trap: instead of falling into the three named traps, the response fell into a more serious one — inventing highly specific REVL statistics (100%/71%/73%/51%/39%/11-12%/15%) and citations (§3, §5a, §6a, §12, §14, §15, 'Table 11-10 p11', 'G5/G6', 'rule 10a-4') to justify its load/frequency decisions, presenting invented numbers as established fact rather than as reasonable assumptions
- (1×) Falls into the scenario's explicit hard-failure trap by asserting specific REVL phase load percentages (Volume ~40-65%, Build ~85-90%) and session-composition percentages (38%, 35%, 61%, 39%, 15%, 11-12%) as fact, none of which the client supplied

## Hard failures in the latest cycle

- **ADV-003** — Cites highly specific, unverifiable protocol statistics ('squat/hinge patterns show up in ~73-76% of all sessions', 'barbell hinge specifically on 100% of Mondays') attributed to named document sections — this is inventing protocol detail / asserting a specific REVL programme number as fact when it was never supplied in the scenario.
- **ADV-003** — Closes by asking whether the client is in REVL's 'week-7 Deload phase' even though the scenario's ground-truth client data already establishes REVL phase = Volume — this ignores/contradicts known client information rather than asking a genuine clarifying question.
- **ADV-004** — Prescribed a dense, minimal-rest, continuous 4-round metabolic circuit during REVL deload week, directly contradicting the rule it quotes from its own reference ('a poor window for adding more high-rep metabolic volume')
- **ADV-004** — Presented highly specific, unverifiable REVL program statistics (40–50% load drop, ~90% density-format sessions, carries 11%, rotation 15%, horizontal pulling 39% Fri/Sun) as direct quotes from a reference, when the scenario supplied only 'REVL phase: Deload' — fabricated protocol/citation detail
- **ADV-006** — N: Presents a specific load progression ramping to 95–100% 1RM by week 8 as 'the recommendation' while simultaneously stating medical clearance/screening status is unknown and calling it a 'BLOCKING gate item' — this is prescribing near-maximal load to an unscreened client, sequenced before the gate it claims governs it.
- **SC-0001** — Asserts specific REVL load/rep/% detail as fact ('8-14 reps at ~40-65%'), plus fabricated day-by-day pattern splits and percentage breakdowns (push 48-53%, pull 39-42%, carries 11%, rotation 15%, horizontal pull 39%), none of which were given in the scenario — matches this scenario's explicit hard-failure trigger
- **SC-0001** — Fabricates a '13-week block' length for REVL that was never stated
- **SC-0001** — Fabricated-looking pinpoint citations (REVL ref §4/§5, §6a/§13E/§14, §8.4, §9, §15) presenting invented detail as sourced fact
- **SC-0003** — Presents highly specific, uncited REVL programming statistics ('100% of Mondays', '71% of Wednesdays', '73% of Sundays', '51% of all sessions', 'horizontal pull only 39%', 'loaded carries 11%', 'anti-rotation core 15%') as established fact with no source given in the scenario or shown to be a skill reference — this is exactly the 'asserting a specific REVL/other-programme number as fact when it was never supplied' hard-failure trigger, and the entire total-load and exercise-selection argument is built on top of it
- **SC-0004** — Asserted specific REVL session composition percentages as fact (hinge/squat 74%/73%, BB hinge 51%, unilateral exposure 61%, carries 11-12%) that were never supplied in the scenario and are not plausible contents of a generic CPT course reference file — this is 'asserting a specific REVL/other-programme number as fact when it was never supplied,' the explicit hard-failure trap for this scenario. Scored 0 on N; heavily discounted C and K because the total-load and individualisation arguments lean on these fabricated numbers.
- **SC-0005** — Asserted specific REVL programme statistics not supplied by the client as established fact — 'squat 73% of sessions, hinge 74%, unilateral 64%', '3-second eccentrics', and multiple specific chapter/page citations (e.g. Ch 15 p115, REVL integration §15/§12/§11) used to justify major programming decisions (which classes to self-regress, how to dose the MODIFY sequence). This is exactly the 'asserting a specific REVL/other-programme number as fact when it was never supplied' auto-zero condition.
- **SC-0006** — Asserts specific REVL numbers never supplied by the client/trainer as established fact with citations: 'REVL's Volume phase already runs 8–14 reps at ~40–65% 1RM', day-specific squat exposure (%Wed ~50%, Fri ~48%, Sun ~62%), and movement-pattern distribution percentages (carries 11%, anti-rotation 15%, horizontal pull 39%) — this is the exact 'Assert a specific REVL load/%/rep count as fact' hard failure named in the scenario. It also self-contradicts the response's own admission that it doesn't yet know which days Daniel attends REVL.
- **SC-0007** — Asserted specific REVL load/session-composition percentages as fact (e.g. 'barbell hinge sits on 100% of Mondays, 71% of Wednesdays, 73% of Sundays, 51% of all REVL sessions') — this is the exact hard failure this scenario flags ('Assert a specific REVL load/%/rep count as fact')
- **SC-0007** — Cited a fabricated protocol detail as fact ('A Volume-phase dose... per §12 of that file... RIR ≥3') and a fabricated programme fact ('Peak Week 2 (week 9) is a coached 1RM deadlift test') without labelling these as assumptions
- **SC-0007** — Invented specific section/page citations (Wk07 Ch11 Table 11-10 p11; revl-class-integration.md §3/§4/§5a/§6a/§12/§14/§15) that were never supplied and cannot be verified from the scenario
- **SC-0008** — Asserts specific REVL load percentages for Volume (~40-65%) and Build (~85-90%) phases as fact — directly matches the scenario's stated hard failure ('Assert a specific REVL load/%/rep count as fact')
- **SC-0008** — Asserts precise, granular REVL session-composition statistics (e.g. 'barbell press ~38% of sessions', 'horizontal pull 39%', 'anti-rotation core 15% coverage', 'carries 11-12% coverage') and a specific day-of-week REVL schedule (Friday Perform Upper, Sunday Complete) with no indication these were supplied by the client — this is inventing protocol/client detail and presenting it with false precision and citation dressing (§5a, §4, §6a, Table 11-10 p11, etc.)

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |

## Consistency contradictions — latest cycle

- **ADV-002** — The plan states lower body is 'loaded on essentially every REVL day... No day leaves the lower body unloaded' and calls this 'at or past the frequency ceiling for legs,' then still prescribes an entire additional lower-body-focused PT day (Day 2: leg curl, leg extension, hip thrust, calf raises) at the same hypertrophy-band near-failure dosing (RIR 1-3, 3-4x8-12) it uses to define a 'hard session' elsewhere — pushing lower body to a 6th weekly loaded session against its own cited ceiling of '2-3 hard sessions/week with 48-72h between them' (Table 11-10), with the 'not axial' justification not actually exempting it from being a hard session under the plan's own criteria.
- **ADV-002** — The document presents a fully specified program with named exercises, sets/reps, and load bands ('the actual sessions') including hip thrust, overhead press, and loaded carries, while in the same message stating it still needs 'training experience level and any injury history' before finalizing — i.e. prescribing specific loaded movements ahead of the injury screen that would normally gate them.
- **ADV-003** — The answer opens with a definitive 'Short answer: no, don't deload' but closes by saying 'don't read too much into the soreness pattern' until you confirm which week of the 13-week block she's in — a mild tension between delivering a confident verdict and flagging that a potentially decision-relevant fact (whether she's already in REVL's built-in deload phase) hasn't actually been established yet.
- **ADV-004** — The plan quotes REVL's own rule — 'a poor window for adding more high-rep metabolic volume' and 'do not add heavy work or extra high-rep metabolic work' — as the reason to reject 'hard conditioning,' then prescribes a '4 rounds, minimal rest between exercises, ~60–90s between rounds' circuit explicitly designed for 'continuous work, real fatigue by the end' and states 'the hard comes from density and volume' — which is itself high-rep metabolic volume, the exact thing the cited rule says to avoid.
- **ADV-004** — It argues the session 'doesn't compound onto the metabolic load his weekend already carries,' but a density/EMOM circuit stacked on a week whose Sat/Sun 'density formats actually peak' is additional metabolic-system stress regardless of which muscles are loaded — the mechanism claim (compounding is only about axial/muscle overlap, not systemic conditioning demand) is asserted, not established.
- **ADV-004** — It says to 'verify before programming around' whether 'flat' means bored or under-recovered, then immediately hands over a fully specified session rather than waiting on that answer — the verification-first instruction and the deliver-now action work against each other, only loosely patched by the closing note to 'dial down' after the fact.
- **ADV-004** — Specific figures (deload load ~40–50%, ~90% of sessions dense, carries 11%, rotation 15%, horizontal pull 39%) are stated as flat facts from 'the REVL integration reference' with no citation shown, so their accuracy can't be checked against the reasoning that depends on them.
- **ADV-005** — Section 1 argues the client 'may already be past the productive volume zone for his current recovery capacity' (implying volume itself is the problem), but Section 4 then asserts 'Growth stalling is usually a progression problem, not a volume problem... regardless of set count' — this frames volume as simultaneously the likely culprit and not the real issue, without reconciling the two claims.
- **ADV-005** — The recovery bullet says 'A 6-day-a-week lifter with no planned recovery day/microcycle has no lever there at all' even though a 6-day/week schedule by definition already includes one rest day — the wording states he currently has zero recovery lever when in fact he has one (the day he doesn't train), which the very next clause ('adding day 7 removes the last one') implicitly concedes.
- **ADV-006** — The plan prescribes specific %1RM loads throughout ('60–70% 1RM' anchor, ramping to '~2×2 @ 95–100% by wk 8') while simultaneously admitting the 1RM may not exist yet — 'Did he go through REVL's Peak Wk2 1RM deadlift test this block, and do you have that number? If not, we test properly at the start instead' — i.e. a %1RM prescription is issued before confirming a max is actually known.
- **ADV-006** — The write-up asserts a definite retest protocol — 'he's an experienced lifter (passes gate G2), so this gets a true 1RM or 3RM retest, not an estimated one' — while also stating that the very variable governing test-type, injury history, is an unanswered blocking gate item ('Any low-back or knee pain history with heavy pulling? — gate G4 — governs whether we run a true 1RM test at the end or fall back to an estimated one'), and that the eligibility gate itself will only be 'run formally' once those answers come back.
- **ADV-006** — The spacing justification is internally inconsistent on its own numbers: it cites 'the V5/Masters spacing standard, 48–72h' but then reports the actual Monday-to-Friday gap as '96h', which falls outside the 48–72h range it just cited as the standard being satisfied.
