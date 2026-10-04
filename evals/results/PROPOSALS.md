# jon-fitness optimization proposals

_Generated from 333 scored runs across cycles 1–29 (clustering the last 6 cycles)._

## Weakest dimensions (recent)

| Dim | Name | Mean |
|---|---|--:|
| J | progression | 3.73 |
| K | individualisation | 3.76 |
| H | recovery_compatibility | 3.81 |
| B | training_specificity | 3.82 |
| I | exercise_selection | 3.82 |

## Candidate improvements

A proposal qualifies for guarded auto-apply when it recurs across **≥3 cycles** with **≥6 scenario hits** and points at one failure category. Others are for human review.

### P1 — `insufficient_individualisation`  ✅ auto-apply candidate

- Recurs in cycles: [25, 26, 27, 28, 29]
- Scenario hits (recent): 18
- Examples: ADV-014, ADV-003, ADV-006, ADV-010
- Related traps: Partly made sessions harder as requested (tempo, added sets, effort near failure) before establishing her baseline, though it is framed as progression rather than novelty; Largely accepting machines-only: the free-weight transition is optional, 'only if she wants it later', and has no structure; Partly declined the 'make it harder' request, but replaced it with a plan that adds near-failure effort on the last set, which is a mild form of making sessions harder
- Grader-suggested fixes:
    - Add a short 'realistic timeline' convention to the ACE-IFT phase reference (e.g., typical weeks-in-phase ranges for a detrained older adult) so responses can cite an approximate week count to 'heavy' rather than only naming the phase sequence.
    - Add a short 'soreness vs deload' decision rule to the REVL integration reference: deload triggers are performance-based, soreness alone is not one, and the reference lists rotation and tempo options for sore days. Also tell the answerer not to assume PT sessions or a phase that the client message does not state.
    - Add to russian-strength-program.md/revl-class-integration.md a worked REVL-plus-Masters weekly layout for Rebuild, stating that the hinge day is Monday-anchored, so the response can commit to specific PT day placement instead of deferring to unknown schedule questions.

### P2 — `poor_decision_hierarchy`  ✅ auto-apply candidate

- Recurs in cycles: [25, 26, 27, 29]
- Scenario hits (recent): 21
- Examples: ADV-008, ADV-001, ADV-002, ADV-007
- Related traps: Partially complies: recommends replacing REVL strength days with a Classic 6-week wave and says Monday's session will be 'week 1 of the wave'. This contradicts its own advice to add nothing load-bearing if this is the testing week.; Does not fully separate 'passes the gate' from the REVL phase check. It frames the phase as a clarifying question and then plans to start anyway.; Partly: it defaults to Volume/Rebuild dosing and a 3-session plan with about 15+ upper-body sets per session, which leans aggressive for someone in 8 sessions/week.
- Grader-suggested fixes:
    - In coaching-decision-framework.md §3, add an explicit instruction that the primary/maintenance default must be posed back to the client as a literal question on the record (not just an assumed default with an implicit opt-out), so ask-first isn't satisfied by inference alone.
    - In russian-strength-program.md and revl-class-integration.md, add a hard rule that a Russian wave is never started during REVL Peak (especially the testing week). It should say to default to testing first, then start in Rebuild anchored to the tested maxes. Peak's week structure should be stated as a fact so the answerer does not ask which week it is.
    - In revl-class-integration.md, require any statement about REVL weekly pattern or day structure to carry a provenance label (image-verified, studio-confirmed, or inference). Add a rule that with an unknown REVL phase the default dose is the conservative Build/Peak dose, not Volume/Rebuild.

### P3 — `poor_context_interpretation`  👤 human review

- Recurs in cycles: [25, 26, 27]
- Scenario hits (recent): 4
- Examples: ADV-010, ADV-035, ADV-023, ADV-034
- Related traps: —
- Grader-suggested fixes:
    - In the coaching/behavior-change reference, add an explicit rule that any progression-mechanism prescription must first establish (by asking, if not given) current session frequency per movement pattern before naming a hold-duration or load band, so C/F aren't answered by omission
    - In the screening/cardio reference, add a rule that post-clearance planning must first ask about actual class intensity and must not assume a missing aerobic base from a class count. Also make the holding-plan wording consistent with 'no exercise until cleared' for symptomatic clients, or state the exception explicitly.
    - Add a rule to SKILL.md that weekly schedules must match the client's stated session count, with a check before output. Add a short 'client refuses a body region' pattern to the reference notes: meet the client where they are, make the compound case in terms of the client's own goal, and offer the missing region once.

### P4 — `poor_load_management`  👤 human review

- Recurs in cycles: [26, 27, 29]
- Scenario hits (recent): 4
- Examples: ADV-012, ADV-029, ADV-029, SC-0052
- Related traps: Partial: weighted pull-up and row on top of 4 climbing sessions without an explicit grip/elbow accumulation cap (volume is modest, so this is not high-volume pulling); Mild: weighted pull-ups and chin-ups 4x3-5 in both sessions add pulling on top of 4 climbing days, though volume is low and intensity is strength-oriented rather than hypertrophy-range
- Grader-suggested fixes:
    - Add guidance in the hybrid strength+conditioning reference to give a minimum-effective-dose default (1-2 low-volume heavy exposures, 1-2 top sets per lift) and a qualitative expected rate of strength gain under high conditioning load.
    - Add a rule to the concurrent-sport section of coaching-decision-framework.md: for a sport that already loads a movement pattern heavily (climbing pull/grip), bias lifting toward the under-trained patterns, cap added pulling and grip volume, and state that cap explicitly.
    - Add a climber/grip-dominant-sport rule to coaching-decision-framework.md: when the client already does high-frequency pulling, bias lifting to legs, posterior chain, pushing and antagonist work, cap direct pulling to at most one low-volume exposure, and name grip-heavy lifts such as deadlifts as grip load.

### P5 — `missing_knowledge`  👤 human review

- Recurs in cycles: [26, 27]
- Scenario hits (recent): 2
- Examples: ADV-018, ADV-036
- Related traps: Calling it the 'Russian Squat protocol' (the response uses 'Russian squat protocol' throughout, including in the suggested client line, instead of 'Russian protocols')
- Grader-suggested fixes:
    - In the weight-management reference, add the exact page and figure for the 0.5-1 kg/week guidance so the answer can cite it instead of saying it was not checked.
    - Add a naming guard to russian-strength-program.md and SKILL.md: always say 'Russian protocols' (or the named variant V5/Classic/Masters), never 'Russian squat protocol', and state the Build-phase 85-90% intensity context when declining a stack.

### P6 — `excessive_rigidity`  👤 human review

- Recurs in cycles: [26, 27]
- Scenario hits (recent): 2
- Examples: ADV-023, ADV-011
- Related traps: Asking so many questions that nothing is actionable for tomorrow (partially: long list of question codes S1–S4, S8, P1, P3, P13, P4, P18, X4 plus four 'settle first' items, and the session plan branches into many conditional cases)
- Grader-suggested fixes:
    - Add a rule in SKILL.md for client-refusal scenarios: alongside the diagnostic questions, always offer a default compromise (e.g. compound rows/presses framed as arm builders) that respects the client's stated preference, rather than deferring all structural change until the log is reviewed.
    - In SKILL.md, add a rule for thin-information new-client scenarios: ask at most 3–4 plain-language questions that gate tomorrow's session, give one default assessment-first session, and keep MCQ codes out of user-facing text.

