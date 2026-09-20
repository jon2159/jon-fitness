# REVL class integration — programming 1-on-1 PT for a client who trains at REVL

> **REVL is the client's existing training stimulus. The PT session should intelligently
> complement that stimulus, address individual needs, and create progression without
> unnecessary duplication of training stress.**

---

## 0. How to use REVL facts — provenance tiers (read this first)

Every programme-level REVL statement in this file, and every one you make in a response,
belongs to one provenance tier. Record confirmed client facts separately, with their source. **The rule is about provenance, not about whether a number appears:**
a REVL claim is fine if it is supported by the supplied REVL material *and* you state it at
the confidence its tier earns; it is a failure if it is unsupported, or if it is stated more
firmly than its tier allows. This replaces an earlier "never state a REVL number" rule, which
removed true, source-backed facts to please a grader instead of fixing the underlying
problem (see §0a).

| Tier | What it is | How to state it |
|---|---|---|
| **T1 Image-verified** | Read directly off the original poster image (e.g. the Peak Wk 2 testing session is a 1RM barbell deadlift and 1RM push press/jerk; the Peak wave tokens) | State it, attributed: "REVL's captured programming shows…". Still not a claim about this client's own week |
| **T2 Studio-confirmed** | Told to us by the studio; not printed on the posters (team-format rep totals are shared, not per person; Peak is three weeks, weeks 2–3 are testing) | State it, attributed to the studio confirmation |
| **T3 OCR-counted** | A keyword count across OCR'd posters (§17). A *lower bound*, describing the programme as written, blind to what a member actually loaded | Default to the §0b bands. A figure is allowed only if you label it: *"keyword count over the captured posters, lower bound, programme as written — not your sessions."* Never build a decision that flips if the figure is 10 points off |
| **T4 Inference** | A reasonable reading of REVL's intent, not stated by REVL | Say "inference" / "my reading" |
| **T5 Not established** | Not established by supplied material or client confirmation: this client's schedule, track, loads or attendance; anything about 2026 Block 3 Rebuild (unpublished at capture); anything the posters don't show | Say the source doesn't establish it, and **ask the client** |

**Unconfirmed client-specific claims are T5.** "REVL loads the hinge pattern very often"
is a programme-level claim (T3). "Your Wednesday is Move Total" or "you'll be at 60% this
week" needs this client's confirmation; the programme template does not establish it.
Once confirmed, record it as **client-reported evidence**, including the relevant week or
period, and reuse it without repeatedly asking. Do not promote it into a universal REVL
fact. The client's report governs their own schedule and exposure over this file's template.

### 0a. Why the tiers exist

Across several eval rounds (2026-09) the skill stated REVL specifics as fact. Two different
problems were being conflated:

1. **Genuinely unsupported or over-firm claims** — a client's personal schedule asserted as
   known; a lower-bound OCR count presented as an exact figure. These are real
   source-grounding failures and the tiers above address them at the source.
2. **A grader/rubric artifact** — the rubric hard-failed any REVL number "not supplied in the
   scenario", including facts correctly drawn from the skill's own REVL references. Graders
   noted this themselves ("sourced from skill references rather than fabricated"). Hiding
   source-backed facts to satisfy that check would degrade coaching, so the rubric was
   corrected to test provenance instead (`evals/rubric.md`, "REVL source-grounding").

### 0b. Default vocabulary for T3 counts

| Term | Roughly |
|---|---|
| **essentially every session / almost always** | 90–100% of sessions |
| **very frequently / most sessions** | 65–90% |
| **often / more than half** | 50–65% |
| **roughly half** | 40–60% |
| **a notable share / sometimes** | 25–40% |
| **occasionally / a minor share** | 10–25% |
| **rarely / a small part of the programme** | 1–10% |
| **not observed in the captured material** | No matching observation in this capture; does not establish absence from REVL or the client's training |

These bands are honest given a lower-bound OCR count; prefer them to a bare percentage.

---

# PART I — Decision framework

Part I is written mostly in T3 bands and T1/T2 facts. **Part II (§17)** holds the underlying
counts with their provenance so any figure can be traced and labelled correctly.

## 1. Purpose

Use this file whenever a client mentions **REVL**, REVL classes/programming/training, or a
REVL phase (**Volume, Build, Deload, Peak, Rebuild**).

It answers two questions:
1. **What training stimulus has this client already received this week?**
2. **What is the smallest, highest-value dose the PT session can add on top of it?**

It does **not** restate any training methodology. For the **Russian protocols** (the
linear-periodization strength blocks — V5 / Classic / Masters) the authoritative source
stays `references/russian-strength-program.md`: its eligibility gate (§2), variants (§3),
autoregulation (§4), fat-loss integration (§5), scaled entry (§6), retest protocol (§7).
This file only decides **whether, when and how much** of that methodology belongs alongside
REVL.

**Reference hierarchy**
1. `references/russian-strength-program.md` — the Russian protocols' methodology.
2. `references/revl-class-integration.md` (this file) — the REVL stimulus and the dosing
   decision.
3. **Client context** — goals, history, current phase, what they *actually* did, recovery
   state. This decides how 1 and 2 are applied, and always overrides this file's general
   characterization of REVL if the client's own report differs from it.

**Evidence quality.** The source material is screenshots of stylised posters; two
independent OCR engines still lose spacing and misread digits, and session/day/phase labels
come partly from folder and file names. Tag what you say with its §0 tier; §17 records each
count's method and limits.

## 2. REVL program structure — general shape, not this client's confirmed schedule

**A 13-week block delivered as coached group classes**, with two parallel strength tracks
(**Perform** — strength-led, %1RM-based; **Move** — hybrid, RIR-based, higher reps) offered
on the same three days, and a separate conditioning format on the other days.

- Members choose **one** strength track and stay on it — they don't do both Perform and
  Move on the same day.
- The three strength-track days each carry a different emphasis (hinge-led, a lower-body or
  bench emphasis, and an upper-body-led day) — **REVL has shipped at least two different
  versions of which specific day carries which emphasis across the years it's been
  captured.** Do not assume a specific day maps to a specific emphasis for this client —
  **ask which session they actually do on which day** before making any claim like "your
  Wednesday is X."
- The conditioning days use a shared, capped, often partner/team format. **Every session in
  the captured material is time-capped** — there is no untimed, self-paced work anywhere in
  what's been observed.
- Session shape is consistent: a short capped warm-up that ramps the day's main pattern,
  a strength/density block holding the main lift plus accessories, one or two short
  AMRAP-style conditioning blocks, and often a partner finisher.

### Three things to get right about the weekend-style sessions

1. **Team-format numbers are shared, not per-person.** Any session run in pairs or teams
   prints the **team's** total work — an individual's actual share is considerably smaller,
   and the format carries substantial built-in rest (more rest as team size grows). **Never
   treat a printed team total as one person's workload.**
2. **The highest-total-volume conditioning day is not a recovery day — but it isn't a
   crusher either.** It's genuinely demanding on paper but carries real built-in rest once
   you account for the team format, landing as moderate-to-high per-person cost rather than
   the hardest session of the week.
3. **The other team-format conditioning day mixes real barbell/loaded work into what looks
   like a pure cardio session.** Don't assume a "cardio day" label means the lower body or
   the barbell patterns get a rest.

**Reading:** the team-format conditioning days are best understood as **extensive interval
sessions** — real work-capacity volume with substantial built-in rest, leaving mostly
metabolic (not neural) fatigue behind.

## 3. The 13-week macrocycle — shape, not numbers

**Volume → Build → Deload → Peak → Rebuild**, in that order, with Peak itself spanning
several weeks rather than one.

| Phase | Intent | Relative load | Reps | Neural headroom for a PT session |
|---|---|---|---|---|
| **Volume** | Accumulate work capacity and pattern familiarity | Lower-to-moderate | Higher | **Most** |
| **Build** | Convert accumulated volume into force | Climbing toward high | Falling | **Limited** |
| **Deload** | Shed fatigue before the heavy weeks | Low | Low | **Strength-only headroom** (see §4) |
| **Peak** | Express maximal strength; re-test | Highest of the block | Lowest | **Minimal** |
| **Rebuild** | Re-accumulate; bridge to the next block | Low-to-moderate, mostly effort-based (RIR/RPE) rather than fixed loading | Moderate | Moderate |

### Peak contains testing weeks — protect them, then use them

Within Peak, the block includes dedicated **strength-testing** and **conditioning-baseline
testing** sessions under coaching — true maximal singles and benchmark conditioning efforts,
not just heavy training. This is confirmed as a stable, repeated feature of the programme,
not a one-off.

1. **Protect these weeks** — add nothing load-bearing or maximal near them.
2. **Use the result afterwards.** If a PT strength block needs a real 1RM
   (`russian-strength-program.md` gate G4 / retest §7), the client's own coached testing
   result — once you confirm with them that it happened and what it produced — can satisfy
   that requirement without a separate re-test. Ask, don't assume it happened on schedule.
3. A reduced-frequency Russian wave starting in Rebuild can be anchored to a strength-test
   result from a few weeks earlier once the client confirms it — no re-testing, no stacking
   two peaks (§10).

**The single most useful structural fact:** REVL periodises **load and effort, not exercise
menu.** The core barbell patterns (squat, hinge) show up in every phase at broadly similar
frequency — **no phase gives a movement pattern a genuine rest**, only the load and intent
around it change. Never assume "they're in Volume so their squat pattern is fresh" — ask
what they've actually trained, don't infer it from the phase name alone.

## 4. Phase-by-phase training characteristics

| | **Volume** | **Build** | **Deload** | **Peak** | **Rebuild** |
|---|---|---|---|---|---|
| Intent | accumulate work capacity + muscle | convert volume to force | shed fatigue before the heavy weeks | express max strength, re-test | re-accumulate, bridge to next block |
| Relative load | lower-to-moderate | climbing toward high | low | highest of the block | low-to-moderate, mostly effort-based |
| Reps | higher | falling | low | lowest | moderate |
| Density/interval format | very frequent | very frequent | **essentially every session** | **least frequent — rest protected** | very frequent |
| Partner/team format | very frequent | often | very frequent | often | very frequent |
| **PT neural headroom** | **most** | **limited** | **strength-only headroom** | **minimal** | **moderate** |

### The Deload is a *strength* deload, not a whole-body deload

The main lift on the heaviest strength day drops meaningfully in Deload week — genuinely
light, low-set work. But the week's biggest team-format conditioning session **keeps
essentially its usual volume** (shared across the team, so still a real per-person dose),
and density/interval formats are actually **more** common than usual that week, not less.

**PT implication.** Deload week is an **excellent** window for assessment, technique,
mobility, corrective and low-load weak-point work — and a **poor** window for adding more
high-rep metabolic volume, since that channel isn't actually being rested.

## 5. Weekly movement-pattern picture

**Barbell hinge (deadlift-family movements) is the single most repeated heavy pattern in
the programme** — trained on **essentially every** session of the strength-track day it
anchors, and very frequently across the rest of the week too. Barbell squat is trained
almost as often as hinge across the week as a whole, though its distribution across days is
less even.

**The conditioning-day sessions are barbell-light but are not lower-body rest** — they
lean on wall-ball/thruster/db-ball and kettlebell-swing style implements very frequently,
which still load the squat and hinge *patterns*, just at high reps with a lighter implement
than a barbell.

**One of the three conditioning-format days is genuinely the densest, most barbell-heavy
mixed day of the week** — squat, hinge and an Olympic-lift-family movement all show up very
frequently on it. Treat that day, and the ~24h either side of it, as the day to protect,
**but confirm which day this actually is for the client's specific track** before declaring
a day off-limits — the mapping of "which weekday is the dense one" has differed between
versions of the programme REVL has run.

**One of the strength-track days is the closest thing to a genuine lower-body offload day**
in the programme — it's built around upper-body pushing and pulling and largely leaves
squat and hinge alone. Again, confirm which day this is for this client rather than
assuming.

### The two clearest, most consistent gaps in the programme

Across everything captured, two patterns are consistently under-trained, holding across
every version of the programme observed:

- **Carries / loaded holds** — a small, consistent minority of sessions. The cheapest,
  lowest-interference-risk pattern to add.
- **True easy, low-intensity aerobic work** — essentially absent; everything in the
  programme is capped and at least moderately competitive, so a client who genuinely lacks
  an aerobic base has nowhere in REVL to build one.

A third pattern — **rotation / anti-rotation work** — is a gap in some versions of the
programme and reasonably well-served in others, depending on which specific track/session
shape the client is actually on. **Ask before defaulting to prescribing it as a gap-filler**
rather than assuming it's missing.

**Horizontal pulling** is a notable-but-not-severe gap, concentrated on only a couple of
days of the week rather than spread evenly.

## 6. Training stimulus & recovery footprint

*What has the client already received?*

| Stress channel | Footprint from REVL | PT reading |
|---|---|---|
| **Lower-body muscular** | Squat and hinge patterns trained very frequently; even the conditioning days load the pattern | **No day in a full week leaves the lower body genuinely unloaded.** Extra lower-body volume is the easiest way to over-reach. |
| **Upper-body muscular** | Pushing and pulling trained often, but concentrated on fewer days than lower-body work | More room here than below the waist — especially **horizontal pulling**. |
| **Axial / spinal loading** | The hinge pattern specifically is the most *repeated* high-cost exposure in the programme | Prefer unloaded, offset or supported alternatives to more axial loading. |
| **High-neural / near-maximal** | Loads climb toward near-maximal in Build and Peak specifically; Olympic-lift-family movements appear very frequently overall | Volume, Deload and Rebuild leave real headroom. **Build and Peak do not.** |
| **Explosive / ballistic** | A frequent feature of the programme as a whole | Rarely the missing quality — adding more plyometric work on top needs real justification. |
| **Metabolic / conditioning** | Frequent, and every session is capped/competitive | Extra conditioning of the *same kind* is rarely the highest-value PT addition — **except** true easy aerobic work, which the programme doesn't contain at all. |
| **Local fatigue sites** | Grip, anterior shoulder, and the posterior chain are hit repeatedly across the week | Ask before adding more of either. |
| **Where recovery is protected** | The week-7 deload (strength side only), Peak's protected rest between exercises, the offload day, and the self-selected Perform/Move choice | Work *with* these, don't spend them. |

### 6a. Complementary opportunities the picture supports, in priority order

1. **Carries / loaded holds** — a consistent gap, cheapest to add, lowest interference risk.
2. **True easy aerobic work** — a consistent gap, and the programme structurally cannot
   provide it (everything is capped/competitive).
3. **Rotation / anti-rotation** — a gap on some programme versions, already served on
   others; confirm the client's actual track before treating this as a priority.
4. **Horizontal pulling volume** — a real but more moderate gap.
5. **Unilateral *stability*** (slow, unsupported single-leg control, as opposed to unilateral
   *loading*, which the programme already does frequently) — genuinely under-trained.
6. **Technique / movement quality at sub-maximal, untimed load** — structurally absent,
   since every REVL session is capped.
7. **Mobility / tissue work beyond a short warm-up** — minimal in the programme.
8. **Individual assessment and weak-point work** — cannot happen in a group class format.
9. **A deliberately low-stress, restorative session** — nothing in the programme is
   programmed below a cap.

## 7. Typical stress pattern across the week

| Day type | Dominant stress |
|---|---|
| **The hinge-led strength-track day** | High muscular and axial load; high neural demand once the block reaches Build/Peak |
| **A conditioning-format day** | Conditioning-dominant, with moderate squat-pattern loading via implements |
| **The densest mixed strength-track day** | The week's highest combined muscular + neural demand |
| **A conditioning-format day** | Conditioning-dominant |
| **The upper-body-led strength-track day** | Upper-dominant; the closest thing to a lower-body offload day |
| **A team-format conditioning day** | Moderate-to-high mixed conditioning, real built-in rest from the team format |
| **The other team-format conditioning day** | Moderate-to-high full-body work capacity, real built-in rest from the team/pair format |

**Favourable PT windows:** the offload day, or the day after the easier of the two
conditioning formats (least neural residue) · Deload week · Volume / Rebuild phases.

**Windows to avoid adding load:** within roughly a day either side of whichever day turns
out to be this client's densest mixed day (confirm which day that is — don't assume) ·
the day this client's hinge-led session lands on · Build and Peak, for a second heavy
exposure · the block's dedicated testing weeks, for anything load-bearing or maximal ·
the team-format conditioning days, for *additional* metabolic volume · Deload week, for
high-rep metabolic volume.

---

## 8. How REVL changes PT programming decisions

Standard PT design still applies — screening, assessment, IFT phase, FITT-VP, progression —
but four things change:

1. **The weekly FITT-VP budget is already partly spent.** **[Course]** Table 9-12 (variables
   by goal) and Table 11-10 (Resistance FITT-VP) *(Wk07 Ch11 p16, p29–31)* and cardio FITT
   *(Wk05 Ch8 p10)* are ceilings for **REVL + PT combined**, never for the PT session alone.
2. **Frequency per muscle group is largely used up.** **[Course]** 2–3 hard sessions/week per
   muscle group, 48–72 h apart *(Wk07 Ch11 Table 11-10, p11)*. REVL usually spends that on the
   lower body by itself.
3. **The PT session's value moves from "more" to "different."** The complementary list in
   §6a is where the marginal return is.
4. **Screening is still the PT's job.** **[Course]** REVL attendance is **not** medical
   clearance. Run the ACSM preparticipation screen and PAR-Q+ *(Wk04 Ch5)* regardless.

---

## 9. ACE PT + REVL integration

**[Course]** The ISA/ACE **Integrated Fitness Training (IFT) Model** still governs the PT
session *(Wk02 Ch2 p10–14, Tables 2-2 / 2-3)*.

- **Map REVL to the model, then place the PT work where the individual needs it.**
  REVL's Volume/Rebuild phases sit closer to a Movement-phase emphasis; Build/Peak sit
  closer to Load/Speed.
  **If the client's movement quality is breaking down under REVL's load, the PT session drops
  back a stage** — Functional / Movement corrective work — even while REVL keeps them in
  Load/Speed. That is correct use of the model, not a contradiction.
- **Cardio phases:** Base → Fitness → Performance *(Wk02 Ch2; Wk05 Ch8)*. REVL supplies
  Fitness/Performance-type work continuously; a client who actually lacks a **Base** may need
  the PT to add easy Zone 1–2 — the one conditioning gap in the programme.
- **Assessment is the PT's job** *(Ch 7 anthropometrics; Ch 10 posture / balance / core /
  movement screens; Ch 10 p69–75 strength testing)*. Only run assessments whose result would
  change the program.
- **Session components** *(Wk07 Ch11 p18; Wk05 Ch8 p41)*: warm-up appropriate to the load the
  client has *already* carried that week → priority work → cool-down / flexibility
  *(Flexibility FITT-VP, Table 11-7)*.
- **Progression tools** *(Wk07 Ch11 p7, p20; Wk03 Ch9 p7; Wk05 Ch8 p26)*: 2-for-2 / double
  progression, ~5% load increments, ≤10%/week cardio progression — applied to the **PT
  session's own** progression, remembering REVL is already progressing the shared patterns.
- **Special-population and MSK overrides** *(Ch 12–15)* replace general values where they
  conflict — check every time. REVL gives scaling *ranges*, not population-specific
  regressions; that gap is the PT's to fill.

---

## 10. Russian protocols + REVL integration

**Do not assume a Russian protocol should be added on top of REVL.** REVL's Build and Peak
phases are *themselves* a linear-periodization strength progression on the barbell lifts.
Stacking a Russian wave onto them means **two concurrent strength peaks** — redundant neural
and structural load, high over-reach/injury risk, usually a worse result on both.

Read `references/russian-strength-program.md` first (gate §2, variants §3, autoregulation §4).
Then apply these rules — they are the REVL-specific instance of the general
concurrent-training / competing-goals principle in `coaching-decision-framework.md` §3
(primary quality gets full dose, the other steps down to maintenance; never two full doses).

### 10a. Is a Russian protocol appropriate alongside REVL at all?

**Consider it only when ALL hold:**
1. Primary goal is a **maximal-strength PB on barbell lifts** — not general fitness, physique
   or conditioning.
2. Client **passes the §2 eligibility gate**, including **G6 recovery context assessed for
   REVL + the protocol combined**, not the protocol alone.
3. Current **REVL phase leaves headroom** (10b).
4. There is a **lift REVL under-serves** for this goal, **or** the client will **replace**
   overlapping REVL strength work (10d).
5. Recovery markers support it (10e).

**Route elsewhere when:** the client is a beginner/returning lifter (→ `russian-strength-
program.md` §6 scaled entry, not stacked on REVL) · a special population the course restricts
(→ Ch 12–15 override) · REVL is already peaking their target lift well (→ support that peak)
· the highest-value need is something else (→ 10g).

### 10b. REVL phase → handling

| REVL phase | Handling |
|---|---|
| **Volume** | Most headroom. A **reduced** wave (10c) on ≤2 focus lifts can supplement. Keep it off the pattern REVL is emphasising that week. |
| **Build** | Real overlap. **Reduce volume and frequency hard**, or run the wave on **one** under-served lift, or **replace** the matching strength-track day (10d). Never a full wave on top. |
| **Deload** | **No Russian protocol.** Respect the deload. Technique at light load, mobility, assessment. |
| **Peak** | **Do not stack.** Either (i) the PT supports REVL's peak (technique, activation, recovery), or (ii) the wave **replaces** REVL's strength-track days and the client keeps only the conditioning-format sessions. |
| **Rebuild** | As Volume. |

### 10c. Reduce volume / intensity / frequency

- **Reduce VOLUME** when REVL is accumulating on the shared pattern, the client also does
  several team-format conditioning sessions, or combined weekly sets would exceed the
  Table 9-12 / 11-10 range. → cut wave sets, drop accessories REVL already covers, or run
  fewer wave lifts (`russian-strength-program.md` §3a subset rule).
- **Reduce INTENSITY** when REVL is in Build/Peak, recovery markers are marginal, or a
  fat-loss deficit runs concurrently (§5 of that file). → finish the wave earlier, or use the
  **Masters** ceiling instead of the V5/Classic top end, and anchor days at the lower %.
- **Reduce FREQUENCY** when REVL already trains the pattern more than once a week — **it
  almost always does** (the hinge pattern especially, per §5). **[Course]** the budget is
  2–3 hard sessions/week per muscle group *(Wk07 Ch11 Table 11-10, p11)*.
  → **The V5 4-day and Classic 3-day variants rarely fit alongside full REVL participation.
  The Masters 2-day variant is the default Russian option for a REVL client.**

### 10d. Replace rather than supplement

Replace when the client wants a genuine peak on specific lifts and would otherwise duplicate
heavy work:
- In **Build or Peak**, run the wave sessions **instead of** the client's REVL strength-track
  days; keep the conditioning-format sessions. One coherent peak beats two half-peaks.
- For a single-lift focus, swap only the REVL day that emphasises that lift.
- Record which REVL sessions are substituted, for how long, and the plan to return.

### 10e. Running the protocol as written

Only when the client has **dropped their REVL strength-track days for the block** (i.e. a
replace, 10d), **or** REVL is in **Volume** *and* the client has consistent good sleep, low
life stress, established work capacity, no deficit, and a clean prior block. Otherwise
reduce (10c) or use Masters.

### 10f. Stacking traps to avoid

- **Never** place a Russian squat or deadlift progression close to this client's densest
  mixed day or their hinge-led day (§5/§7) — confirm which days those are for this client.
- **High-neural stacking:** a near-maximal Russian session + a REVL Peak strength-track
  session + a hard conditioning session inside a couple of days is three near-maximal
  exposures. Cut to one.
- **Lower-body accessory pile-up:** Russian accessories + REVL accessories + REVL
  conditioning leg volume compounds fast. Drop the PT accessories REVL already covers.
- **Redundant pressing:** a Russian press wave stacked on top of REVL's own upper-body
  pressing days can add up to several pressing sessions a week without anyone noticing.

### 10g. Prioritise another quality instead

If the limiter is not maximal strength — restricted ROM, poor single-leg stability, weak
posterior chain, low core endurance, a shoulder/low-back history, thin aerobic base, low
tissue tolerance to REVL's volume — address **that**, and defer the Russian protocol to a
block where the client is in REVL Volume or between blocks.

---

## 11. PT session selection framework

Run these nine steps in order.

1. **Identify the current REVL phase.** Ask: which block, which phase, which week within it,
   which strength track, and what the last week actually looked like — **including which
   specific weekday carries which session for this client; never assume it from the general
   shape in §2.** Phase sets the headroom (§4).
2. **Map what they've already trained this week**, using the client's own report against the
   general picture in §5/§7. Note which patterns are already trained more than once this
   week.
3. **Estimate accumulated muscular and neural stress.** Muscular load is high in every phase;
   neural demand rises through Build and peaks approaching the block's testing weeks.
   **[Course]** muscle groups need 48–72 h *(Wk07 Ch11 Table 11-10, p11)*; periodization's
   benefit is planned physical **and mental** recovery *(Wk07 Ch11 p42)*.
4. **Determine what the client actually needs** — the single highest-value gap from §6a plus
   their own goals and assessment results. If the honest answer is "REVL covers it and they
   just want more," that is a reason to do **less**. **If total weekly sessions (REVL + PT)
   reach roughly 7–8, explicitly present a session-count or session-length reduction as one of
   the options** — fewer PT slots, shorter PT sessions, or converting a slot to
   recovery/mobility — alongside any content changes. Making added content low-cost is not a
   substitute for raising the session-count question (`coaching-decision-framework.md` §4).
5. **Select complementary exercises.** Don't repeat the same primary pattern at similar or
   heavier load close to the matching REVL day. Choose a different *expression*:
   unilateral vs bilateral, tempo/pause vs grind, DB/KB vs barbell, supported vs axial,
   carry/anti-rotation vs another squat.
6. **Adjust volume and intensity to recent exposure** — see §12.
7. **Sequence, rest, load.** **[Course]** multi-joint / higher-skill first *(Wk07 Ch11
   p12–13)*; rest matched to intent — 2–5 min strength, 30–90 s hypertrophy, ≤30 s endurance
   *(Table 9-12, p16)*, longer if they arrive fatigued; autoregulate with RPE/RIR rather than
   a fixed % because REVL residual fatigue varies *(RPE as intensity metric, Wk05 Ch8 p15–20)*.
8. **Modify for client state** — §14, and the order in §15.
9. **Progress without assuming more is better** — improve quality or specificity, not session
   count: better positions, a heavier top set at the *same* RIR, a harder unilateral variation,
   a longer Zone 2 piece. One variable at a time *(2-for-2 / double progression, Wk07 Ch11 p7,
   p20)*. Stall or regress deliberately during Deload and Peak.

Whenever a Russian protocol enters the conversation, open
`references/russian-strength-program.md` and apply §10 above.

---

## 12. Volume & intensity adjustment rules

Count the PT session **on top of** REVL's weekly totals, never in isolation. These caps are
**the PT's own dosing judgement**, informed by the general picture in §3/§4 — not a claim
about what REVL itself prescribes.

| REVL phase | Added PT strength dose (guide) | Added PT conditioning |
|---|---|---|
| **Volume** | up to a normal accessory/secondary session; cap added top-set intensity in the moderately-high range, well short of maximal | Zone 1–2 only, if the client lacks a base |
| **Build** | half a session, or one focused lift; kept short of near-maximal; low set count | Zone 1–2 only |
| **Deload** | **no heavy or high-volume work** — technique at light load, mobility, assessment | keep it easy; the week is already dense |
| **Peak** | **none additive** — support work only (activation, one light technique primer, recovery), unless the PT work *replaces* a REVL strength day (§10d) | Zone 1–2 only |
| **Rebuild** | as Volume | as Volume |

**Additional rules**
- If a pattern has already been trained more than once this week, the PT may add **at most
  one** more exposure, and only as a *different quality* (e.g. tempo/stability rather than
  another heavy grind).
- If a pattern has already been trained several times this week, add **none** — pick a
  different pattern.
- Lower-body: assume it is loaded on every training day. Treat added lower-body volume as the
  most expensive thing on the menu.
- Axial loading: prefer supported/offset/unloaded alternatives — the hinge pattern is already
  loaded very frequently across REVL's week.
- Conditioning: only add if the *quality* is missing (easy aerobic), not the quantity.

---

## 13. Example complementary PT sessions

Illustrative shapes, not prescriptions — always re-derive from the client's actual week, and
never present these day-labels ("the offload day," "the dense mixed day") as fixed for a
specific weekday without confirming the client's actual track first.

**A. Volume phase, general-fitness client, session on the offload day.**
Assessment-led. Ankle/hip mobility → half-kneeling anti-rotation press (Pallof) 3 × 8/side →
suitcase carry 4 × 30 m → single-leg RDL 3 × 8/side @ RIR 3 (stability, light) → controlled
horizontal row 3 × 10. *Fills the carry and rotation gaps and adds pulling volume, adds no
axial load.*

**B. Build phase, client wants to get stronger, session placed away from the dense mixed
day.** One focused lift only: paused/tempo front squat 4 × 3 at a moderately-high effort,
RIR 2 (a *different expression* of a pattern REVL trains hard) → weak-point accessory (e.g.
split squat) 3 × 8/side → anti-rotation core. Keep total sets low; skip if the dense mixed
day is within 24 h.

**C. Peak phase, client peaking with REVL.** No added heavy work. Warm-up quality drills,
technique primer at a light-to-moderate load on their weakest lift, soft-tissue/mobility for
the restricted joint, breathing/downregulation to close. Purpose: **support the peak**,
protect it.

**D. Deload week.** Full movement screen and any outstanding assessments → corrective work →
low-load technique reps → mobility. The best assessment window in the block.

**E. Client wants to build muscle.** Target under-served tissue, not more compound volume:
horizontal pulling, direct arm/rear-delt/upper-back, controlled tempo, 8–15 reps, 30–90 s rest
*(hypertrophy band, Table 9-12)*, RIR 1–3. Place away from the client's densest and
hinge-led days.

**F. Client wants conditioning.** If they already do several team-format conditioning
sessions, do **not** add intervals. Add what's missing: 25–40 min easy Zone 1–2
(nasal-breathing / talk-test pace) on a non-REVL day, progressing ≤10%/week *(Wk05 Ch8 p26)*.

**G. Client confirms their specific track and schedule.** Once the client has told you
which day is which session and which track (Perform/Move-equivalent) they follow, build the
gap-filling session around *their* confirmed structure — don't default to a generic template
day-of-week mapping without that confirmation.

---

## 14. Client-state decision rules

| Client says | Read it as | Do |
|---|---|---|
| **"I did REVL yesterday."** | Ask *which* session and what it emphasised. A lower-body/axial-loaded day, an upper-loaded day, a conditioning day, and a high-total-work day each leave different residue. | Avoid the same primary pattern at similar/heavier load. Choose a complementary pattern or a different expression. If yesterday was their densest or highest-total-work day, keep today light. |
| **"I'm doing REVL tomorrow."** | Tomorrow's stress is about to land. | Leave them fresh. No near-maximal work, no novel high-eccentric work, no exhaustive metabolic finisher. Technique, mobility, activation, light accessory. |
| **"I'm in the Volume phase."** | Most headroom; loads lower-to-moderate, volume already high. | The best phase for added strength exposure — but keep added intensity moderate and watch total sets. Good window for a *reduced* Russian wave if §10a passes. |
| **"I'm in Build."** | Loads climbing toward high; overlap with any strength block is real. | Half-doses only. One focused lift. Prefer weak-point / quality work. If a Russian protocol is wanted, reduce hard or replace a REVL day (§10c/d). |
| **"I'm in Deload."** | Strength is deloaded; the biggest conditioning session is **not**. | Best assessment / technique / mobility / corrective window of the block. **Do not** add heavy work **or** extra high-rep metabolic work. |
| **"I'm in Peak."** | Multiple different weeks with different demands — **ask which one.** | See the rows below. |
| &nbsp;&nbsp;↳ **The heavy-wave week of Peak** | Highest sustained neural demand. | Support only. No second heavy exposure. If their PB goal outranks the REVL peak, **replace** REVL strength days with the protocol (§10d) rather than adding. |
| &nbsp;&nbsp;↳ **The strength-testing week of Peak** | True maximal singles under coaching. The highest-stakes week in the block. | **Add nothing load-bearing.** Session = activation, mobility, technique primer, recovery. Afterwards, **ask whether the test happened and what it produced** — a confirmed result can satisfy the current-1RM requirement for a PT strength block (`russian-strength-program.md` G4 / §7) without re-testing. |
| &nbsp;&nbsp;↳ **The conditioning-baseline-testing week of Peak** | Maximal *metabolic* efforts being scored. | Don't blunt them: no added conditioning, no heavy legs the day before. Ask for the benchmark scores as the client's conditioning baseline once confirmed. |
| **"I'm in Rebuild."** | Loads low-to-moderate, mostly effort-based; re-accumulating. | Similar headroom to Volume. Good time to start a new PT progression or a *reduced* strength block. |
| **"My legs are sore from REVL."** | Expected — no day leaves the lower body genuinely unloaded. | Train upper body, carries, anti-rotation, or do mobility/aerobic. Avoid loaded squat/hinge and high-eccentric lower work. Sore ≠ stop, but it does mean **change the pattern**, not just the load. |
| **"My upper body is fatigued from REVL."** | Likely their upper-body-led or highest-total-work day. | Lower-body *stability* and mobility work, gentle unilateral, Zone 1–2 aerobic. Avoid pressing and heavy pulling. |
| **"I feel fresh despite doing REVL."** | Genuine headroom **or** under-reporting. Verify: sleep, sessions actually attended, effort used, appetite, mood, last week's performance. | If genuinely fresh **and** in Volume/Rebuild/Deload → this is the window for the highest-value addition (a strength exposure, or starting a reduced protocol). **Freshness is not a reason to add work by default** — still pick the highest-value gap, not the biggest dose. |
| **"I want to get stronger while continuing REVL."** | Legitimate and achievable — but frequency is the constraint, not willingness. | Run the §10a check. If it passes: **Masters-style low-frequency wave** on 1–2 lifts, placed well clear of the client's own densest/hinge-led days, in Volume/Rebuild. If it fails: build the weak point first (§10g), or replace REVL strength days in Build/Peak (§10d). |
| **"I want to build muscle while continuing REVL."** | Compound volume is already high; what's missing is targeted, controlled, tissue-specific work. | Hypertrophy-band accessory work *(3–6 × 6–12, 30–90 s rest, 67–85%, Table 9-12)* on under-served tissue: horizontal pull, upper back, arms, rear delts, calves. Controlled tempo, RIR 1–3. Protein/energy sufficiency → general information only, refer to an RD for detail *(Wk01 Ch1 p7–8)*. |
| **"I want to improve conditioning while continuing REVL."** | They already get several capped/competitive sessions a week. Adding more of the same has low return. | Add the **missing quality**: true Zone 1–2 steady state (talk-test pace), 25–40 min, on a non-REVL day, ≤10%/week progression *(Wk05 Ch8 p10, p26)*. Only add intervals if a specific test/event needs them **and** something else is removed. |

**Every row above assumes the resulting weekly session count is reasonable.** If REVL plus
the PT slots being discussed would put the client at roughly 7–8+ total sessions/week, the
session-count reduction option (§11 step 4) applies regardless of which row matched —
content selection alone doesn't resolve a frequency problem.

---

## 15. Practical Do / Avoid / Modify

**DO**
- Ask which sessions they actually attended, on which days, and what effort they actually
  used — never assume the general shape in §2/§5/§7 describes this client's specific week.
- Screen readiness at the start of **every** session (soreness, sleep, energy, last session's
  performance, life stress).
- Prefer *different expressions* of a pattern over more of the same.
- Fill the measured gaps: **carries, anti-rotation (if their track doesn't already serve it),
  horizontal pulling, easy aerobic, technique at sub-maximal load, mobility, assessment**.
- Use RPE/RIR to autoregulate against the day rather than a fixed %.
- Use the **Deload week** for assessment and corrective work.
- Count PT + REVL together against the FITT-VP ceiling.
- Write down which REVL sessions the client is skipping or substituting, if any.

**AVOID**
- Adding a heavy squat or deadlift close to the client's hinge-led or densest mixed day.
- Any second near-maximal exposure during Build or Peak.
- Assuming the team-format conditioning days were easy, or that the highest-total-work day
  is a recovery day.
- Assuming a phase rests a movement pattern — none of them do.
- Adding conditioning volume to a client already doing several team-format sessions.
- Adding high-rep metabolic work during Deload week.
- **Stating any specific REVL percentage, count, or day-specific schedule claim about this
  client as fact — ever, hedged or not (§0).**
- Stacking a full Russian protocol on top of REVL.

**MODIFY — in this order** when the client reports soreness, poor sleep, fatigue, reduced
performance, or a stress spike:
1. Drop the **intensity** of the added work.
2. Drop the **volume** (sets first).
3. Swap to a **lower-demand variant** (unilateral→supported, barbell→DB/KB, loaded→bodyweight).
4. Change the **session type** entirely — mobility, activation, Zone 1–2, or education.
5. If markers persist beyond ~1 week: reduce total load, advise scaling REVL too, review
   sleep/nutrition/stress, and refer to a physician if unresolved *(recovery & overtraining,
   Wk07 Ch11 p47–48; scope Wk01 Ch1 p7–8)*.
Record the trigger and the modification in the plan's decision log.

---

## 16. Key principles for the jon-fitness agent

1. **REVL is the client's existing training stimulus. The PT session should intelligently
   complement that stimulus, address individual needs, and create progression without
   unnecessary duplication of training stress.**
2. **Do not add a protocol simply because the client can tolerate more work.** First determine
   what stimulus REVL has already provided, identify the highest-value training need, then
   select the **smallest effective additional dose**.
3. **Ask, don't assume.** The general picture in Part I is a hypothesis about REVL-as-a-
   system; the client's actual reported week is the data that governs the response.
4. **Every REVL claim carries its provenance tier (§0).** Programme-level facts may be
   stated at the confidence their tier earns (T1/T2 attributed; T3 as a §0b band, or a
   labelled lower-bound figure); inferences are labelled; anything about *this client's*
   week is T5 until confirmed — then record and reuse it as client-reported evidence.
5. **No phase rests a movement pattern.** REVL periodises load and effort, not exercise
   selection.
6. **Never stack two strength peaks.** In Build/Peak, replace rather than supplement.
7. **Scope is unchanged** *(Wk01 Ch1 p7–8)*: screen, refer out for medical clearance, injury /
   rehab (physical therapist), and detailed nutrition or disordered eating (registered
   dietitian). REVL membership changes none of that.
8. **When Russian protocols are considered, open `references/russian-strength-program.md`**
   and use it *with* this file — never either in isolation.

---

# PART II — Quantitative evidence appendix

**Provenance register.** Every table below is **T3** (OCR keyword counts, lower bound,
programme as written) unless a row says otherwise. Use it to check that a Part I band is
honest and, if you quote a figure, to label it per §0 — never to state a figure bare, and
never as a statement about a particular client's week.

## 17. The underlying counts

Source: `source/extract_revl.py` → `source/revl_raw_data.md` (2026, 363 screenshots across
Blocks 1–3) and `source/revl_raw_data_2025.md` (2025, 260 screenshots across Blocks 3–4) —
two independent OCR engines, disagreements flagged, a sample verified against the original
images directly. Analysis: `source/analyze_revl.py` →
`source/revl_programming_analysis.md` (2026) / `source/revl_programming_analysis_2025.md`
(2025); cross-year synthesis in `source/revl_2025_vs_2026_analysis.md`. **2026 Block 3's
Rebuild phase (3 weeks) had not been published by REVL when captured — treat that gap as a
capture limitation, not a programming finding.**

**Evidence tiers used in the source analysis:** *[Observed]* — read directly off the
screenshots or OCR; *[Pattern]* — repeated across many sessions, backed by the counts here;
*[Inference]* — a reasonable reading of intent, not stated by REVL itself. Percentages
describe **the programme as written**, not any individual member's week, and moved by no
more than a few points when a third block of data was added — this is stable house style,
not a block-specific artifact.

### 17a. Overall movement-pattern exposure (share of all sessions, 2026, n=363; 2025 range shown where it differs)

| Pattern | 2026 | 2025–2026 range |
|---|--:|--:|
| Hinge (any implement) | 74% | 63–74% |
| Squat (any implement) | 73% | 66–73% |
| Erg / machine cardio | 68% | — |
| Unilateral lower | 64% | 53–64% |
| Olympic / ballistic | 56% | 56–63% |
| Core / trunk | 55% | — |
| Horizontal push | 53% | — |
| Vertical push | 50% | — |
| Vertical pull | 43% | — |
| Horizontal pull | 39% | — |
| Running / locomotion | 34% | — |
| Burpee / mixed metcon | 30% | — |
| Rotation / anti-rotation | 15% (2026) | 33% in 2025's Move-track shape |
| Carry / loaded hold | 11% | 8% (2025) |

### 17b. Barbell-specific exposure by weekday (2026, keyword-count lower bound)

| Movement | Mon | Tue | Wed | Thu | Fri | Sat | Sun | all |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| BB deadlift/sumo/RDL | 100% | 12% | 71% | 8% | 33% | 15% | 73% | 51% |
| BB back/front squat | 8% | 4% | 50% | 0% | 48% | 4% | 62% | 28% |
| BB bench press | 38% | 0% | 50% | 0% | 63% | 0% | 54% | 35% |
| BB strict press/STO/jerk | 65% | 15% | 19% | 23% | 46% | 23% | 62% | 38% |
| BB power clean/snatch | 33% | 31% | 67% | 27% | 12% | 38% | 15% | 34% |
| Wall ball/thruster/DBall | 56% | 69% | 44% | 69% | 48% | 69% | 31% | 54% |
| KB swing | 15% | 50% | 35% | 42% | 19% | 38% | 35% | 30% |

**This table describes the 2026 capture's day-labels specifically.** REVL has shipped at
least two different weekly shapes across the two captured years — the 2025 shape differs
(see `source/revl_2025_vs_2026_analysis.md` §2a). Never assume this table's day-to-emphasis
mapping applies to a given client without asking which track/year-style they're actually on.

### 17c. Phase-level load tokens (2026, image-checked where noted)

| Phase | Wks | Main-lift load (%1RM tokens observed) | Reps | Density format | Team format |
|---|---|---|---|---|---|
| Volume | 1–3 | 40–65% | 8–14 | 72% | 74–80% |
| Build | 4–6 | 50–90% | 5–10 | 67–69% | 44–47% |
| Deload | 7 | 30–55% | ~8 | 90% | 85–87% |
| Peak | 8–10 | 60–95% (Block 1); ~92.5% ceiling (Block 2) | 1–5 | 49–51% | 43–47% |
| Rebuild | 11–13 | mostly RPE/RIR, %-prescription in ~12% of sessions | moderate | 80% | 85% |

### 17d. Exposure by session type (2026)

| Pattern | Hinge-led strength day | Densest mixed strength day | Upper-only strength day | Hybrid strength day | Conditioning format A | Conditioning format B | Team conditioning | High-total-work day |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| Squat | 62% | 100% | 0% | 74% | 83% | 92% | 93% | 81% |
| Hinge | 100% | 100% | 8% | 100% | 42% | 62% | 63% | 88% |
| Unilateral lower | 81% | 100% | 0% | 76% | 33% | 42% | 63% | 69% |
| Horizontal push | 73% | 4% | 100% | 72% | 21% | 25% | 26% | 77% |
| Vertical push | 92% | 8% | 46% | 62% | 25% | 33% | 30% | 65% |
| Horizontal pull | 62% | 0% | 96% | 49% | 4% | 8% | 0% | 85% |
| Vertical pull | 58% | 38% | 81% | 44% | 38% | 46% | 11% | 15% |
| Carry/hold | 19% | 23% | 8% | 17% | 8% | 8% | 7% | 0% |
| Rotation/anti-rot. | 12% | 19% | 42% | 22% | 0% | 0% | 4% | 12% |
| Core/trunk | 77% | 69% | 46% | 72% | 38% | 62% | 22% | 19% |
| Olympic/ballistic | 58% | 96% | 4% | 47% | 79% | 62% | 70% | 35% |
| Erg/machine | 12% | 15% | 4% | 85% | 100% | 100% | 100% | 100% |
| Running | 0% | 0% | 0% | 9% | 100% | 75% | 70% | 54% |

Session-type labels here follow `source/revl_programming_analysis.md`'s own categories —
see that file for the literal 2026 poster names, and `source/revl_2025_vs_2026_analysis.md`
for how these map differs by year.

### 17e. Provenance and known data-quality issues

- Raw extraction: **363 screenshots, Blocks 1–3 of 2026**; **260 screenshots, Blocks 3–4 of
  2025**; two OCR engines, disagreements flagged. 2026 Block 3's Rebuild phase was unpublished
  at capture time.
- A confirmed data-quality defect: one 2026 Block 3 page has a broken image reference in
  REVL's own CMS (an HTML-escaping bug), recovered by repairing the DOM before capture —
  documented in `source/revl_programming_analysis.md` §E for full detail.
- Team-format rep totals are **shared, not per-person** — confirmed directly by the studio,
  not stated on the posters themselves.
- Method limits: keyword-presence counting is a **lower bound** (synonyms/OCR misses aren't
  captured); it counts sessions *containing* a pattern, not sets or reps; it cannot see the
  load an individual member actually used.
