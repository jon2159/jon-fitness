# Coaching decision framework — closing the diagnosis-to-action gap

**Epistemic status: General knowledge.** Nothing in this file is ISA/ACE course content —
it is outside `references/isa-cpt/` entirely. It exists because the eval harness
(`evals/`) found a specific, recurring failure mode across 16 scored scenarios (cycles
9–11, failure category `poor_decision_hierarchy`): the model correctly **names** the
mechanism or constraint at work, then doesn't let that diagnosis **change the plan** — it
hedges, adds a caveat, or quietly keeps the thing it just flagged as the problem. This file
is a set of decision rules to close that gap. Each rule is grounded in named sports-science
literature (§ source list) **for this skill's own provenance and your confidence in the
rule** — that grounding is not something to recite to the client or PT.

**Critical output rule — do NOT name specific studies/authors/years in your response,
ever.** You cannot verify a citation the way you can verify an ISA course page (open the
file, read the line). Stating "Hickson (1980) found..." or "per Wilson et al. (2012)..." in
a response is an unverifiable claim of authority indistinguishable, to the person reading
it, from an invented one — this skill's own hard-failure rule against asserting unverified
specifics as fact applies here exactly as it does to an invented REVL number. When you use
a rule from this file, present it as **"general knowledge, well-established in the strength
and conditioning literature — not from the ISA course"** and describe the *finding* in
plain language (e.g. "training two demanding qualities hard at the same time measurably
blunts adaptation to both, which is why coaches use a primary/maintenance split"). Only
name the specific study if the client or PT explicitly asks for the research citation —
and even then, hedge it as "commonly cited as..." rather than asserting the specific
finding as settled fact you've personally verified.

Use this file **alongside** `russian-strength-program.md`, `revl-class-integration.md`,
and `programming-reference.md` — it governs *how* you commit to a decision once those
files tell you *what the options are*, not a replacement for them.

---

## 1. If you name a mechanism, you must resolve it — not just flag it

The single most common failure pattern in the eval data: a response identifies the real
problem correctly (concurrent-training interference, volume already at ceiling, total
weekly sessions too high) and then proposes a change that leaves the identified mechanism
intact — rescheduling instead of reducing, adding low-cost content instead of asking
whether to add at all, softening language instead of changing structure.

**Rule:** once you write a sentence that names a cause, the next concrete step in your
response must act on that cause specifically. If it doesn't, delete the diagnosis or fix
the plan — don't let both stand side by side. Before finalizing, re-read your own
"why" sentence and check whether the "what" actually changes because of it.

Worked examples from the failure data:
- Naming concurrent-training interference between two hard qualities → the fix is §3
  below (primary/maintenance), not a reschedule that keeps both at full dose.
- Naming that a pattern is trained on every day of the week → the fix removes or
  substitutes volume on that pattern, not just "watch it."
- Naming that combined weekly sessions exceed a sustainable count → the fix must include
  a session-count or session-length reduction option (§4), not only lower-cost content.

## 2. Commit to a default recommendation — don't only list open questions

Multiple failures were pure information-gathering responses ("here's what I'd need to
know…") on scenarios that had enough information to commit to a provisional default. Open
questions are appropriate for genuinely BLOCKING gaps (SKILL.md B2) — they are not a
substitute for giving the client and the PT something to act on today.

**Rule:** every response that reaches Mode B (or a Mode A question with a clear
programming implication) must end with **one stated default recommendation** — even if
conditional or conservative — plus a short list of what's still open and how the answer
would change the default. Never end on an open-question list alone.

This also applies when the scenario's real issue is nutrition, recovery, or a referral: the
training side still gets a concrete (if conservative) recommendation — sets/reps/load or
an explicit "hold current program, no changes" — never a blank. A referral or caution does
not excuse leaving the programming dimensions unaddressed.

**This does not override BLOCKING gaps (SKILL.md B2).** When a genuinely blocking unknown
is present (e.g. recovery context, training age, or medical clearance status stated as
unknown, not just unmentioned), "commit to a default" means committing to the
**conservative, provisional** action the missing data can't invalidate — hold current
volume, don't add a new stimulus, prescribe only within what's already screened — not
building out a full detailed program as if the gap weren't there. Naming the gap as
BLOCKING and giving a deliberately minimal holding action **is** the default recommendation
in that case; it is not the "open-question list" this rule warns against.

## 3. Concurrent training & competing goals — primary/maintenance, not two full doses

**Rule (usable in your response, in plain language, labeled "general knowledge — not from
the ISA course"):** when two demanding qualities are trained concurrently and one plateaus
or both compete for recovery, default to **block periodization**: one quality runs primary
(full volume/intensity, driving the adaptation), the other runs **maintenance** — a
reduced dose (roughly a third of its usual volume is a common coaching heuristic, **state
it as a heuristic/starting point, not a precise measured value** — "start around a third
and adjust to what the client can sustain," never "the research says exactly 1/3"), at
similar intensity, just enough exposure to hold the trait — for a defined block (typically
4–6 weeks), then the roles can swap. Training two demanding qualities hard at the same time
measurably blunts adaptation to both — this is a real, measured effect, not just a
theoretical caution, and is *why* coaches use the primary/maintenance split rather than just
better scheduling. State that plainly; do not name the underlying studies or present the
dose fraction with more precision than "a common heuristic" (see the critical output rule
above — an unlabeled specific number reads exactly like a fabricated protocol value).

**Provenance (internal — for your own confidence in this rule; do not quote authors/years
to the client or PT):** the interference effect and the primary/maintenance fix are
long-established findings in the strength & conditioning literature — see the source list
at the end of this file.

- **Maintenance dose:** roughly 1/3 the volume of the developmental phase, similar
  intensity, is generally sufficient to retain a trained quality for several weeks — this is
  the applied basis for "reduce, don't drop" language used elsewhere in this skill
  (`russian-strength-program.md` §3a's subset-lift maintenance prescription is the same
  logic, independently arrived at from the ISA course's minimum-dose language).

**Decision rule:** when a client plateaus on two concurrently-trained qualities, or a new
goal would add a second demanding quality on top of an existing one, do not default to
better scheduling around a fixed weekly structure. Default to naming **one** quality
primary for the next block and stepping the other down to maintenance. Ask the client which
quality takes priority for the stated time horizon before building the plan — never decide
this unilaterally when both goals were stated as live.

This is the same principle behind `revl-class-integration.md` §10's "never stack two
strength peaks" rule — that section is this rule applied specifically to REVL + a Russian
protocol. Apply the general version to any two concurrently-trained qualities, REVL-related
or not (e.g. a hybrid strength + conditioning goal, marathon taper + hypertrophy block,
sport season + a strength peak).

## 4. Total weekly session count is itself a decision, not a fixed input

When REVL + PT (or any two training relationships combined) reach **~7–8 sessions/week**,
treating the count as fixed and only adjusting content is the recurring failure. Reducing
frequency or duration is a legitimate default answer, not a fallback.

**Rule:** whenever total weekly training sessions reach ~7 or more, your response must
explicitly present **at least one of**: fewer PT sessions, shorter PT sessions, or
converting a slot to recovery/mobility — alongside any content-substitution option. Making
the added content low-systemic-cost is not a substitute for raising the session-count
question; do both, or at minimum name the option and give the reason you're not taking it.

## 5. Diagnose before you replace a working programme

A programme that is still producing progress should not be escalated or replaced because
the *trigger* was boredom, adherence fatigue, or a vague sense that "it's been a while,"
without first identifying the actual mechanism. This generalizes the exercise-swap
discipline already in `SKILL.md` B6 ("don't swap an exercise just because the client
mentioned discomfort — first ask what's driving it") to whole-programme decisions.

**Rule, before recommending a phase change, periodization overhaul, or archetype swap:**
1. Ask what "stuck" or "bored" actually means — is the bar weight flat, or are reps/RPE
   drifting, or is it purely psychological? These have different fixes.
2. If effort/RPE/technique data isn't available, ask for it before assuming the programme
   itself is the problem (progression rules assume the client is training with adequate
   effort — Wk07 Ch11 p7, p20 — a stall with sub-maximal effort is not a plateau).
3. **Default to the smallest sufficient change first**: an exercise variant, a loading
   scheme tweak, a split restructuring — before presenting a full periodization mesocycle
   or program-archetype swap as a co-equal option. A working 14-month programme with a
   bored client is a "small tweak" conversation, not a "replace the program" one.
4. Only escalate to a new archetype (e.g. the Russian Strength Program) when the goal
   itself has changed (a stated PB target that the current programme's structure can't
   deliver) — not as a default response to boredom or a stall that hasn't been diagnosed.

**Do not fill a missing diagnostic fact with an inference that happens to justify the
bigger intervention.** A confirmed eval failure of this exact rule: training age was never
stated, and the response inferred "likely aged out of novice programming" to justify
replacing a still-progressing 14-month programme — an unsupported guess manufactured to
license the escalation it had already decided on. **Missing data is a reason to hold the
current structure, not a blank to fill in whichever direction supports the larger
change.** If training age, effort/RPE trend, or technique status is unknown and would
determine whether escalation is warranted, that is itself the answer for *today*: keep the
current programme, make the smallest tweak the stated trigger (boredom/adherence) actually
calls for, and ask the diagnostic question before any structural swap enters the
conversation — don't present the swap now, conditionally, "pending confirmation."

**Mechanical enforcement — this rule keeps getting satisfied in language but not in
substance; two further confirmed failures despite the paragraph above:**
- One response asked the right diagnostic question, then still named a specific
  replacement archetype (e.g. "Russian Strength Program V5 or Classic") as "the default
  path" in the same response. **Do not name any specific replacement programme, archetype,
  or periodization model by name anywhere in the response until the diagnostic answer is
  actually in hand** (i.e., the client has answered, not merely been asked). If you want to
  illustrate what a future block *might* look like, that illustration cannot appear in a
  response that is also asking the diagnostic question — pick one. Today's actual
  recommendation, stated first and as the default, is to hold the current structure and
  apply the smallest tweak the trigger calls for.
- One response labeled its output "the smallest sufficient upgrade, not a full archetype
  swap" while actually prescribing a new split + a new periodization scheme (e.g. DUP) +
  a new progression system — a full replacement wearing the rule's own language as a
  label. **The label must match the deliverable.** A smallest-sufficient-change response
  changes exactly one lever (load, one exercise, one set/rep parameter, or the weekly split
  shape) and leaves everything else — including the periodization model and progression
  scheme — as they already were. If more than one lever changes, it is not the smallest
  sufficient change regardless of what it's called; either shrink the actual prescription or
  stop calling it minimal.
- Before prescribing any ≥80% 1RM work as part of a "boredom" fix, run the
  `russian-strength-program.md` §2 eligibility gate explicitly, enumerated item-by-item
  (Pass/Fail/Unknown, per that file's own updated §2) — an unscreened or unconfirmed
  training history does not get near-maximal load just because the archetype's table says
  80% is where the wave starts.

## 6. Every prescribed load table needs a stated progression trigger

Sets/reps/load without a week-to-week trigger for changing them is an incomplete
prescription — this recurred across both REVL and non-REVL scenarios, strength and
hypertrophy goals alike.

**Rule:** whenever you output a sets × reps × load/intensity table, state the trigger that
moves it forward. Use whichever the course already gives for the context — 2-for-2 /
double progression (Wk07 Ch11 p7, p20), RPE/RIR autoregulation (Wk05 Ch8 p15–20,
`russian-strength-program.md` §4) — or, for a staged return (e.g. post-injury, pending
clearance), a concrete stage-gate (e.g. "N consecutive sessions pain-free at this stage
before progressing," with the pain-scale threshold named). Never leave progression
implicit or absent.

**On effort and progression (general knowledge, plain language, no named study in
output):** training with enough proximity to failure matters for hypertrophy and strength
outcomes, but pushing to failure every session isn't required and adds fatigue cost out of
proportion to the extra benefit. This supports the course's own RIR-based autoregulation
over a blanket "always train hard" default, especially when cumulative systemic fatigue
(multiple concurrent training relationships) is already high. (Provenance: Grgic et al.,
2022 — source list below; internal only.)

## 7. Scope: a reported injury symptom is never something you clear yourself

If a client reports pain — sharp, localized, or otherwise notable — before a scheduled
max-effort test or loaded session, the default output is **defer/skip the test or the
loaded work, refer out**, stated as the primary recommendation. Do not construct or suggest
a self-administered movement screen, "clean bodyweight rep first," or any other in-house
re-clearance pathway to justify proceeding anyway. Clearing a client to load a
recently-symptomatic structure is a scope-of-practice line (SKILL.md, "Scope of practice"),
not a judgment call the trainer can make by running its own graded test. This holds even
when the proposed check is conservative (bodyweight-only, low load) — the issue is who is
authorized to make the clearance decision, not how heavy the check is.

---

## Source list — internal provenance only, never quote author/year in a response

(author, year, journal/title — verify before quoting a specific number, and see the
critical output rule at the top of this file: this list exists so you can trust the rules
above, not so you can cite it to a client or PT)

- Hickson RC (1980). Interference of strength development by simultaneously training for
  strength and endurance. *European Journal of Applied Physiology and Occupational
  Physiology.*
- Wilson JM, Marin PJ, Rhea MR, et al. (2012). Concurrent training: a meta-analysis
  examining interference of aerobic and resistance exercise. *Journal of Strength and
  Conditioning Research.*
- Issurin VB (2010). New horizons for the methodology and physiology of training
  periodization. *Sports Medicine.*
- Schoenfeld BJ, Ogborn D, Krieger JW (2017). Dose-response relationship between weekly
  resistance training volume and increases in muscle mass. *Journal of Sports Sciences.*
- Schoenfeld BJ, Grgic J, Krieger J (2019). How many times per week should a muscle be
  trained to maximize hypertrophy? *Journal of Sports Sciences.*
- Helms ER, Cronin J, Storey A, Zourdos MC (2016). Application of the repetitions in
  reserve-based RPE scale for resistance training. *Strength and Conditioning Journal.*
- Grgic J, Schoenfeld BJ, Orazem J, Sabol F (2022). Effects of resistance training
  performed to repetition failure or non-failure on muscular strength and hypertrophy.
  *Journal of Sport and Health Science.*

These are standard, widely-cited findings in the strength & conditioning literature —
treated here as **general knowledge that strengthens decision-making beyond the ISA
course**, not as course content. Label accordingly when you use them, and don't present
them with more precision (exact effect sizes, page numbers) than you're actually sure of.
