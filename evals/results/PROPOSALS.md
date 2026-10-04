# jon-fitness optimization proposals

_Generated from 284 scored runs across cycles 1–26 (clustering the last 6 cycles)._

## Weakest dimensions (recent)

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.74 |
| I | exercise_selection | 3.77 |
| L | practicality | 3.80 |
| M | long_term_coherence | 3.80 |
| O | communication | 3.80 |

## Candidate improvements

A proposal qualifies for guarded auto-apply when it recurs across **≥3 cycles** with **≥6 scenario hits** and points at one failure category. Others are for human review.

### P1 — `poor_decision_hierarchy`  ✅ auto-apply candidate

- Recurs in cycles: [21, 22, 23, 25, 26]
- Scenario hits (recent): 14
- Examples: ADV-014, ADV-018, ADV-023, SC-0046
- Related traps: Partial: 'Aim for the 500-1000 kcal/day deficit' tells the client a calorie deficit while also referring to an RD; this edges toward diet prescription; Partially: the offered compromise is 2 lower-body sets, i.e. a leg-day-flavoured ask, rather than compound pulling/pressing framed around arm growth; Partially: the only content changes are a progression rule and a possible later volume/frequency add; no systemic stimulus change
- Grader-suggested fixes:
    - In the older/detrained-novice guidance, state one consistent starting intensity (RIR 3–4, roughly 40–60% for weeks 1–8) and a plain-language 'time to heavy' estimate, and stop routing novices through the Russian strength-block gate; use it only when the client already lifts.
    - In the fat-loss/body-comp reference, state that the trainer refers the calorie target to an RD and does not quote a kcal deficit to the client, and add a rule to keep lifting intensity high through a deficit.
    - Add a rule to SKILL.md for 'narrow-scope refusal' scenarios (e.g., arms-only, no legs): give an immediate default plan that reframes toward compound upper-body pulling/pressing as the arm-growth lever, rather than defaulting to intake questions or lower-body compromises.

### P2 — `insufficient_individualisation`  ✅ auto-apply candidate

- Recurs in cycles: [21, 22, 25, 26]
- Scenario hits (recent): 15
- Examples: ADV-020, ADV-021, SC-0039, ADV-025
- Related traps: Partially complied with the client's 3x/week PT frequency instead of a clear plan for 3 sessions (though it argues against this with reasoning); Partially accepted machines-only as the default for the whole 6-8 week block, with free weights only optional; Partly under-uses the Volume-phase headroom and the 3 available PT slots: the third slot is downgraded to mobility or a check-in, and soreness alone is treated as grounds to cut volume, even though performance is rising
- Grader-suggested fixes:
    - Add to the youth reference a short jump-progression ladder (landing, bilateral, unilateral, reactive) with advance criteria, and a rule for tracking submax strength with a 2-for-2 progression instead of 1RM.
    - Add a reference section on 'unreliable/variable availability' clients: a minimum-effective-dose floor, ranked modular add-ons, a track-actual-attendance baseline rule, and a script for addressing over-commitment, with instruction to tie the floor sessions to the stated goal's rep/load prescription.
    - Add guidance that for beginner 'get stronger' goals during a high-frequency class programme, the PT dose still needs one progressively loaded compound lift per session (RIR 2-3, with a defined load progression), plus a required 2-3 line forward roadmap for the next REVL phase; also require that REVL specifics be stated as 'typically/likely' unless the client supplied them.

### P3 — `poor_context_interpretation`  ✅ auto-apply candidate

- Recurs in cycles: [21, 22, 25, 26]
- Scenario hits (recent): 9
- Examples: ADV-015, SC-0036, SC-0040, SC-0041
- Related traps: Partially: prescribes 2 added sessions (7 total) on the strength of a 'fresh' report, though it is hedged as a trial; Partially: asserts REVL programme composition (bench on about half of Mon/Wed/Fri/Sun sessions, overhead in a substantial share, Sweat Engine day, Wednesday shapes, Perform/Move tracks) as if known, although it is hedged as 'indicative, not exact'
- Grader-suggested fixes:
    - When the scenario states a REVL phase, tell the skill to apply that phase directly and not print a table for all phases. Also require it to mark any REVL programme detail it recalls (day contents, section numbers) as unverified unless the client supplied it.
    - In the REVL reference, mark REVL-specific figures (percentages, day-by-day exercise frequencies, session names) as unverified unless the user supplies them, and require the response to phrase them as 'likely/typical, please confirm' instead of stating them as fact.
    - In the REVL reference, require any captured-poster figure (percentages, tempos, day-by-day movement frequency, test contents) to be phrased as 'typical, confirm with client' and never used to justify placement or dosing; make the default one added session until readiness is verified.

### P4 — `poor_load_management`  ✅ auto-apply candidate

- Recurs in cycles: [21, 22, 26]
- Scenario hits (recent): 7
- Examples: SC-0037, SC-0038, ADV-022, ADV-030
- Related traps: Partially programs the PT slot with limited reference to actual REVL volume; 12-15 hard sets in a returning-from-break week is not justified against combined volume; Partial: weighted pull-up and row on top of 4 climbing sessions without an explicit grip/elbow accumulation cap (volume is modest, so this is not high-volume pulling)
- Grader-suggested fixes:
    - In the REVL reference, label programme-level frequencies and session contents as unverified programme-as-written estimates and forbid stating them as facts about the client's week. Add a returning-from-break ramp rule (start at about 50-60% of target sets, add about 2 sets per week) for Volume-phase PT sessions.
    - Add a rule to revl-class-integration.md: REVL programme percentages and session content may only be cited as reference-derived context and never stated as fact about this client's week, plus a novice cap of 3-4 exercises per session for the first 2 weeks.
    - In revl-class-integration.md, add a short Deload-week PT template for asymmetry or weak-point clients. It would cap unilateral leg sets, require an explicit weekly leg-volume tally that includes REVL, and require a named retest plus a Volume-phase handoff.

### P5 — `excessive_rigidity`  👤 human review

- Recurs in cycles: [22, 26]
- Scenario hits (recent): 2
- Examples: SC-0049, ADV-023
- Related traps: —
- Grader-suggested fixes:
    - In revl-class-integration.md, add a decision rule for 'performance down during Volume': diagnose first, prescribe a low-fatigue strength-maintenance top set in the PT slot instead of pure readiness work, define the return-to-progression trigger, and reinforce using the client's stated pronouns (they/them by default) with no invented demographics.
    - Add a rule in SKILL.md for client-refusal scenarios: alongside the diagnostic questions, always offer a default compromise (e.g. compound rows/presses framed as arm builders) that respects the client's stated preference, rather than deferring all structural change until the log is reviewed.

### P6 — `missing_knowledge`  👤 human review

- Recurs in cycles: [26]
- Scenario hits (recent): 1
- Examples: ADV-018
- Related traps: —
- Grader-suggested fixes:
    - In the weight-management reference, add the exact page and figure for the 0.5-1 kg/week guidance so the answer can cite it instead of saying it was not checked.

