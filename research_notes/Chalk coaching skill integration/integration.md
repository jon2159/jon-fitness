# Existing coaching architecture and reusable Chalk integration prompt

## What architecture and evidence constraints already exist?

### Takeaway
**Post-audit update:** The user explicitly authorized fixing the discovered conflicts. Canonical SKILL.md and Russian/REVL references were minimally corrected, and only those three files were synchronized into the active `.agents/skills/jon-fitness` copy. Existing edits were preserved; archived snapshots untouched. Byte equality and targeted stale-rule checks passed. The observed conflicts listed below describe the pre-fix state. No Chalk integration has been installed, and no paid evals or commits were run.

Corrections: unconfirmed client claims remain unknown until recorded as client-reported evidence; non-observation does not establish absence; SKILL.md routes REVL assertions through provenance rather than repeating unconditional OCR figures; Russian reference explicitly distinguishes documented 6/8/9-week variants from an unestablished nine-month source. These are source/consistency corrections, not demonstrated coaching-score improvements.

Extend the existing `jon-fitness` skill with a supplemental Chalk reference and a coherent integration decision process. Avoid a competing standalone coaching persona and do not treat a marketing description as a complete programming method.

### Cited Findings
- Canonical skill routes via COURSE_MAP, separates course-supported/applied/general knowledge, blocks unsafe prescriptions, uses staged intake, and maintains canonical Markdown plus derived CSV client plans. [SKILL.md](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:90), [intake](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:246), [traceability](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:435)
- Source routing points specifically to screening Ch5, assessment Ch10, resistance variables Ch11, cardio Ch8 and special-population overrides. A map is navigation, not sufficient verification for load-bearing quantitative claims. [COURSE_MAP](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/COURSE_MAP.md)
- Russian reference defines V5 as **9 weeks**, Classic as six weeks, Masters as eight weeks. Design history also explicitly calls the supplied V5 template a nine-week block. None of these inspected files establishes a nine-month source protocol. [Russian reference](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/russian-strength-program.md:81), [design history](/Users/jonathan.tan/Desktop/Projects/jon-fitness/docs/russian-strength-integration-plan.md:19)
- Canonical REVL reference currently has T1 image-verified, T2 studio-confirmed, T3 OCR-counted, T4 inference, T5 not established; it explicitly differentiates programme descriptions from client schedules. [REVL provenance](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/revl-class-integration.md:9)
- It still equates “not observed in captured material” with “not something the programme trains,” an invalid leap from missing observation to universal absence. Its blanket statement “Client-specific claims are always T5” also needs qualification: client-confirmed facts should become recorded client evidence, not remain unknown forever. [REVL vocabulary](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/revl-class-integration.md:27), [absence claim](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/revl-class-integration.md:58)
- The main SKILL.md still repeats strong numeric/generalized REVL claims, independently of the provenance redesign; reviewing only the REVL reference would miss those. [SKILL.md assertions](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:373)
- Filesystem comparison during this audit: `.claude` and `.agents` SKILL.md, Russian reference, and COURSE_MAP have identical SHA256 hashes, but REVL reference differs. The `.agents` version still contains the older number ban; canonical `.claude` version contains new tiers. These are separate directories, not symlinks. [Canonical REVL](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/references/revl-class-integration.md), [mirror REVL](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.agents/skills/jon-fitness/references/revl-class-integration.md)
- Held-out generalization and wildcard scenarios must remain outside optimizer input; grader reliability and human calibration are distinct checks. [Harness integration](/Users/jonathan.tan/Desktop/Projects/jon-fitness/evals/HARNESS_INTEGRATION.md)

### Inferences
- Integration should first resolve which skill copy each runtime loads and which copy evaluation measures. Otherwise a valid redesign may never reach the assistant answering clients.
- Use separate dimensions for source origin and confidence. An official Chalk marketing statement can verify what Chalk claims but does not verify physiological efficacy; scientific evidence can justify a coach adaptation without making it a Chalk fact.
- Client feasibility and safety are constraints on all source application, not the lowest-priority item in a hierarchy.

### Gaps
- No original Russian workbook was opened in this audit; the nine-week finding is directly established by reference and design history, not a new workbook examination. A distinct nine-month source may exist elsewhere; ask for it or locate it before attributing that duration.
- REVL image-level facts were not re-verified in this subtask; tier claims must not be promoted into newly verified evidence by this report.
- The initial audit did not establish current run completion or cycle scores. A later explicitly authorized reconciliation checked local processes and found no matching run_cycle.py, regrade, optimize.py, nightly.sh, or claude -p process. No clients were read; no rubric/result files changed; no paid evaluations run.

## What minimal integration and validation design should the prompt require?

### Takeaway
Use one coaching system with three supplied foundations plus an explicitly bounded Chalk design reference. Optimize individual outcome, recoverability, adherence, and provenance—not the number of included methods or a benchmark average.

### Cited Findings
- Existing B4 already asks for strategy before variables/exercises and requires progression and reassessment. Existing REVL archetype requires mapping actual training and selecting the smallest useful complement. [B4](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:284), [REVL archetype](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.claude/skills/jon-fitness/SKILL.md:343)
- Existing skill-creator recommends a lean SKILL.md and references loaded only when relevant, with generalization rather than narrow patches. [skill-creator](/Users/jonathan.tan/Desktop/Projects/jon-fitness/.agents/skills/skill-creator/SKILL.md)

### Inferences
Recommended minimal architecture:
1. Small routing and scope addition in existing `SKILL.md`, preserving its name and identity.
2. `references/chalk-design-reference.md`: dated official sources, track-specific observations, claim register, limitations, permitted adaptations, explicit nonclaims.
3. `references/integrated-performance-programming.md`: needs analysis, source-gap matrix, quality priorities, weekly dose allocation, split choice, progression, periodization and practical output requirements.
4. Minimal COURSE_MAP/reference-index and intake updates only where needed; reuse existing client templates and validator. Do not introduce scripts unless repetitive calculation or validation requires them.
5. Small new methodological eval cases in the existing skill eval set; preserve current tests and held-out isolation. Keep the source review independent of score optimization.

Recommended provenance register fields: claim ID; exact bounded claim; source family and source type; URL/path plus page/section/image locator; publication/access date; track/block/sample scope; direct observation versus provider claim versus research finding versus inference; confidence/limitations; permissible coaching use; known contradictions. Research findings also record population, intervention, comparator, outcomes, and relevant limitations.

A four-day target means four total planned training days by default, with REVL or Chalk participation counted inside the workload. Ask if the user means four independent PT days in addition to classes. Do not silently add classes, optional hard sessions, or every physical quality to each day.

Validation order: freeze versions and settings; audit contested source claims; regrade unchanged saved answers to estimate rubric effect; compare unchanged scenarios with old/new skill under one corrected rubric/model configuration; inspect blind qualitative differences; report confirmed failures separately from uncertain claims; monitor preserved safety and held-out performance. Changes to a rubric mean a different baseline, not an automatic coaching gain. Do not edit files used by a running evaluation.

### Gaps
Public Chalk pages cannot establish proprietary full-cycle loading, deloads, daily sessions, or algorithmic personalization unless those are actually shown. This limits Chalk-specific claims, but does not block a supplemental public-source design reference.

## What complete reusable prompt should the user give the implementing agent?

### Takeaway
The following prompt is intended for a future implementation turn; it does not claim the skill has already been installed or validated.

### Cited Findings
This prompt operationalizes the existing source routing, screening, traceability and skill-editing rules cited above. Chalk factual findings must come from the accompanying verified research report and official pages, not this architecture audit.

### Inferences

```text
TASK: Extend my existing jon-fitness coaching skill with a verified Chalk Performance Training design reference. Build one coherent individualized coaching methodology combining my supplied ISA CPT/ACE-based foundation, Russian Strength Program, and REVL material, informed by suitable exercise-science research. Chalk is a supplemental program-design and delivery reference; do not replace the three foundations or copy a proprietary program.

ROLE AND SUCCESS CRITERIA
Act with the analytical rigor of a sports and exercise scientist and experienced S&C coach. Do not claim real professional credentials. Optimize meaningful strength, relevant conditioning/work capacity, movement and athletic qualities, recoverability, feasibility, and adherence for the individual. Explain tradeoffs. “Optimized” means justified choices with a monitoring and adjustment process, not proven globally optimal or higher benchmark scores.

START WITH THE WORKSPACE
Read AGENTS.md and applicable jon-fitness and skill-creator instructions. Inspect git status and preserve existing changes. Identify canonical .claude/skills/jon-fitness and the runtime-loaded .agents copy; compare relevant files and establish deliberate synchronization. Do not overwrite snapshots or unrelated work. Keep skill identity and existing scope, screening, course routing, client privacy, and Markdown/CSV synchronization rules. Do not read unrelated client files. Do not change skill/rubric/scenario files currently used by an active evaluation; prepare a separate draft until its input snapshot is safe to change. Never invent historical changes.

SOURCE AUDIT
Use the accompanying research report as an index, then verify load-bearing claims against original sources. Begin Chalk research at https://www.chalkperformancetraining.com/pages/chalk-app-lp and inspect relevant official track pages, help material, and publicly available samples. Record retrieval date, URL, exact track/version, what was observed, and limitations. Avoid laundering testimonials, marketing claims, or provider credentials into evidence of efficacy. Different tracks are different offerings; do not manufacture one universal Chalk template from their combined features. Public descriptions support a bounded design reference, not reconstruction of paid programming. If paid details are unavailable, mark them unknown and proceed with supported supplemental principles; request source material only when a consequential decision requires it.

Verify the three supplied foundations independently through their original artifacts and navigational maps. Route ISA CPT claims through COURSE_MAP and verify cited lesson pages. Check the Russian source duration: current reference/design history says V5 nine weeks, Classic six weeks, Masters eight weeks. Do not call that nine months. If a separate approximately nine-month source exists, identify and inspect it; otherwise treat a nine-month plan as a new coach-designed horizon, explicitly labeled. REVL thirteen-week structure must be tied to the captured block/version or studio confirmation, not assumed universal or applied to an unconfirmed client calendar. Never convert OCR non-detection into proof that a quality is absent.

EVIDENCE MODEL
Separate source origin from strength of evidence. Distinguish: source observation; official provider description/claim; studio confirmation; OCR-derived observation; scientific finding; inference; professional programming decision; client-reported fact; unknown. Preserve existing course-supported/applied labels and REVL provenance without forcing all evidence into one ranking. Every major claim needs a retrievable locator and appropriate scope. Client-confirmed details can be recorded as known client facts; unreported details remain unknown. A reference asserting “verified” is not sufficient verification when disputed.

ANALYSE BEFORE INTEGRATING
For ACE/ISA, Russian, REVL, and Chalk separately, describe documented objective, programming structure, progression, developed qualities, applicability, limits, and evidence gaps. Distinguish a system’s actual contents from the adaptations we propose. Produce a source-to-gap matrix: desired client outcome, already supplied stimulus, missing or redundant stimulus, uncertainty, evidence needed, proposed response. Do not invent deficiencies to justify adding Chalk. Keep useful decision commitment only when the mechanism actually changes the recommendation; do not hard-code block periodization, more volume, or one split for every concurrent-training problem.

RESEARCH AND ADAPTATION
Use relevant systematic reviews/meta-analyses and primary peer-reviewed studies to address genuine gaps or consequential adaptations. Record population, training status, outcomes, uncertainty, and applicability. Do not invent universal interference rules, fixed separation windows, exact minimum doses, or optimal percentages from research that did not establish them. For each major change document:
CLIENT FACT → SOURCE PRINCIPLE → GAP/CONFLICT → RELEVANT EVIDENCE → COACH INTERPRETATION → PROGRAM DECISION → PROGRESSION/MONITORING → SCHEDULE ROW.
Safety, eligibility and individual feasibility constrain all source applications. Preserve source identity while explaining justified deviations.

INDIVIDUALIZATION AND FOUR-DAY DESIGN
Before prescribing a client plan, complete existing staged screening/intake. Establish primary/secondary goals, time horizon, current training/strength/conditioning, exercise competence, actual classes and sports, schedule, equipment, session duration, recovery, limitations, and preferences. Do not fabricate missing values or unscreened maximums. With no named screened client, deliver the reusable methodology and clearly conditional architecture, not a personalized load prescription.
Treat four days as total planned training days unless the client explicitly means four additional PT days. Count REVL/Chalk participation and sport in total weekly demand; replace or omit redundant work before adding it. Compare suitable split structures and select one from the client’s priorities, recovery and time. Establish priority qualities and weekly stimulus before choosing exercises. Retain stable measurable strength anchors; use purposeful variation where it helps accessory work, conditioning, movement practice or adherence. Include power, unilateral work, carries, bracing, hypertrophy and aerobic/anaerobic work only where they have a justified role and dose. Do not append a hard finisher to every session by default.
Create one coherent progression model, with emphasis and maintenance decisions, fatigue adjustments, deload/reassessment logic, and long-term phases. Use Russian strength principles and observed REVL block logic intelligently; do not stack independent calendars or concurrent peaks. Label any nine-month macrocycle as our design unless directly established by supplied sources. Integrate conditioning with strength priorities and specify measurement: mode, duration, intensity method and scale, work/rest when relevant, progression, and fatigue response. Distinguish the course’s zone terminology from other zone systems.
For a sufficiently screened client, output weekly structure; session time budget; exercises; sets/reps; %1RM basis where appropriate; RPE/RIR scale and caps; rests; warm-up; conditioning; progression; substitutions; recovery/adjustment rules; testing and reassessment. Do not guarantee strength gains. Preserve the existing canonical Markdown and derived CSV, changing CSV only when prescription changes and running validate_plan.py.

MINIMAL SKILL CHANGES
Prefer two new references—chalk-design-reference.md and integrated-performance-programming.md—with small routing additions to SKILL.md and relevant intake/index updates. Reuse existing templates/scripts. Keep provider facts separate from our integration rules. Audit duplicated assertions in SKILL.md and other references so corrected provenance is not contradicted elsewhere. Maintain a clear source of truth across .claude and .agents without rewriting historical snapshots.

VALIDATION
Do source auditing before score interpretation. Freeze skill, scenarios, rubric, model/settings, and source snapshot. Preserve existing eval guardrails and independent answer/grade turns. Keep generalization and wildcard data out of optimizer proposals. Regrading unchanged old answers estimates grader effects; matched old/new answers on identical scenarios under one rubric estimate coaching differences, subject to grader variability. Review disputed claims and actual decisions, distinguish confirmed failures from unknowns, and inspect safety, fatigue, specificity, progression, practical timing and source fidelity. Include methodological cases for an experienced four-day standalone trainee, a REVL participant with four total days, limited recovery/time, insufficient screening, and missing paid Chalk details. These are diagnostic probes, not special-case wording targets. Do not launch paid or lengthy evaluation runs without an explicit run instruction. Report validation not performed honestly.

DELIVER
Provide: (1) source and gap audit; (2) documented Chalk contribution and nonclaims; (3) minimal reviewable skill/reference edits with mirror strategy; (4) integration methodology and client-output contract; (5) proposed validation cases and any authorized results; (6) remaining source uncertainties and precise changes made. Do not commit, push, publish client data, purchase Chalk access, or claim installation/testing before it occurs.
```

### Gaps
The final report writer should insert the verified Chalk findings and exercise-science source list from adjacent research into the accompanying report. The prompt intentionally does not hard-code unpublished program details or unsupported research thresholds.
