# Plan — Integrating the Russian Strength Program into the `jon-fitness` skill

**Status:** ✅ IMPLEMENTED 2026-09-06 per your answers to §7. Built:
`references/russian-strength-program.md`, `templates/strength_block_plan.md` +
`templates/strength_block.csv`, `scripts/russian_block.py`; edits to `SKILL.md`
(B4a), `COURSE_MAP.md`, `programming-reference.md`, `intake-questions.md`
(P13–P17), `validate_plan.py`; evals 6–8 added. This doc is kept as the design
rationale.
**Date:** 2026-09-06
**Goal you gave me:** take the `Russian Strength Program V5.xlsx` template, combine it with the
ISA CPT framework already in the skill, and make the skill able to serve *both* competitive
athletes and general-population trainees who mainly want to get strong, hit PBs, and lose fat —
modern, flexible, evidence-grounded.

---

## 1. What I researched

# 1a. Your V5 template (decoded from the xlsx)

`Russian Strength Program V5 (4-Day Split)` — a 9-week block.

**1RM inputs (kg):** Squat 100 · Deadlift 120 · Bench 80 · Military Press 70 · Weighted Pull-up 30.

**Split**

| Day       | Workout | Main lifts                         | Accessories (2–3 × 8–12) |
| --------- | ------- | ---------------------------------- | --------------------------- |
| Mon & Thu | A       | Squat, Bench Press                 | Bulgarian split squat, Dips |
| Tue & Fri | B       | Deadlift, Military Press, Pull-ups | RDL, Face pulls             |

**Main-lift loading wave** — the same set/rep/% scheme is applied to *every* main lift at once.
Mon & Tue are a fixed "anchor" exposure every week; Thu & Fri carry the progression:

| Week | Mon / Tue (anchor) | Thu / Fri (progression) | % of 1RM (progression day) |
| ---- | ------------------ | ----------------------- | -------------------------- |
| 1    | 6 × 2             | 6 × 2                  | 80%                        |
| 2    | 6 × 2             | 6 × 4                  | 80%                        |
| 3    | 6 × 2             | 6 × 5                  | 80%                        |
| 4    | 6 × 2             | 6 × 6                  | 80%                        |
| 5    | 6 × 2             | 5 × 5                  | 85%                        |
| 6    | 6 × 2             | 4 × 4                  | 90%                        |
| 7    | 6 × 2             | 3 × 3                  | 95%                        |
| 8    | 6 × 2             | 2 × 2                  | 100%                       |
| 9    | 6 × 2             | 1 × 1                  | 105% (retest)              |

Target loads in the sheet are literally `1RM × %`, e.g. Squat wk1 = 100 × 0.80 = 80 kg.
There is no separate deload week; the Mon/Tue 6×2 @ 80% is the built-in relative-recovery day.

### 1b. Where the template comes from

The V5 sheet is a **4-day full-body adaptation of the classic Russian Squat Routine** (a.k.a.
"Soviet 6-week peaking cycle" / "USSR 1974–1976 yearbook squat routine"). The source Google
Sheet you linked is a personal training log of the *original* single-lift version:

- 3 sessions/week, one lift (squat), 6 weeks then a retest.
- Alternates a fixed **6×2 @ 80%** day with a rising-volume day (6×3 → 6×6 @ 80%), then flips to
  rising intensity (5×5 @ 85%, 4×4 @ 90%, 3×3 @ 95%, 2×2 @ 100%, 1×1 @ 105–110%).
- In that log the lifter went 125 kg → 132.5 kg squat (~+6%) over 6 weeks.
- Published expectation for the classic cycle: **+5–10% on the trained 1RM**, and it is written
  for **experienced lifters with a solid base who are peaking** — it is explicitly *not* a
  beginner program, and the original 3-heavy-days-a-week version "is demanding on recovery."
  A "masters" variant runs 8 weeks, 2 days/week, and mixes in lighter 60–70% work.

Your V5 modernises it by (a) spreading the work across a push/pull-style split, (b) applying the
wave to **five** lifts simultaneously, and (c) bolting on hypertrophy accessories.

### 1c. Fat-loss context (industry + course)

Combining heavy compound lifting with a calorie deficit is a mainstream fat-loss approach: the
lifting **preserves lean mass and keeps resting metabolic rate up**, conditioning "finishers"
add energy expenditure, and the deficit itself (nutrition) does most of the work. The honest
version — and the one the ISA notes back — is that fat-loss *rate* is driven by the energy
deficit, not the lifting scheme, and "very quickly" has a floor before lean mass and adherence
suffer (see §3d).

---

## 2. How the Russian program maps onto the ISA CPT framework

This is the core of the integration — every piece of the template needs a home in the course
model so recommendations stay traceable.

| Russian-program element                                             | ISA CPT home                                                                                                                                                                                                | Label                                                 |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Barbell squat/bench/DL/OHP under external load for force production | **IFT Muscular Training — 3rd stage: Load / Speed Training** (Wk02 Ch2 p14; Wk07 Ch11 p21–32). The course literally lists "power lifting" as a Load-phase method.                                   | Course-supported                                      |
| 9-week wave, volume down / intensity up over time                   | **Linear periodization**, one mesocycle (Wk07 Ch11 p42–46). Course note: "usually only core (multi-joint) exercises are periodized" — matches (accessories stay fixed at 2–3×8–12).              | Course-supported                                      |
| 6×2–6×6 @ 80%                                                    | Straddles**hypertrophy (67–85% 1RM, 6–12 reps)** and the low end of **strength** in Table 9-12 (Wk07 Ch11 p16). 6×6 @ 80% is high, near-limit volume.                                        | Course-supported                                      |
| 5×5 @ 85% → 2×2 @ 100%                                           | **Muscular strength**: ≥85% 1RM, ≤6 reps, 2–6 sets, 2–5 min rest (Table 9-12).                                                                                                                    | Course-supported                                      |
| 1×1 @ 105% in wk 9                                                 | A**1-RM squat / bench assessment** (Wk06 Ch10 p69–73) — must follow the course's spotting rules and per-test contraindication checks.                                                               | Course-supported                                      |
| Each main lift trained 2×/week, 72 h apart (Mon→Thu, Tue→Fri)    | Resistance FITT-VP: each major muscle group 2–3 d/wk, 48–72 h between sessions (Wk07 Ch11 Table 11-10). Compliant.                                                                                        | Course-supported                                      |
| 80% base as the*entry* intensity                                  | FITT-VP:**≥80% 1RM is specified for *experienced* lifters**; novices/intermediates sit at 60–70% (Table 11-10). ⇒ the template is only appropriate above a training-status threshold (see §3a). | Course-supported                                      |
| Conditioning "finishers" for fat loss                               | Load-phase methods include**HIIT** (Wk02 Ch2 p14); cardio **Fitness phase** intervals (Ch 2, Ch 8). Keep away from heavy lower-body days.                                                       | Applied from the course                               |
| RPE / RIR autoregulation layered on the % targets                   | Course permits**RPE as an intensity method** and defines the **2-for-2 rule** and **double progression** (Wk07 Ch11 p7, p19–20). Bar-velocity cues are outside the notes.                | Applied from the course / General knowledge (flagged) |

### The "functional training" wording

Worth being precise, because the skill's whole principle is traceability. In the ISA/ACE model,
**"Functional Training" is a specific stage** — re-establishing postural stability and
kinetic-chain mobility with bodyweight/core/balance work — *not* the gym-culture sense of
"functional = big free-weight lifts / athletic prep." What you're describing ("combine CPT with
the Russian program to establish functional training") lands in the course's **Movement +
Load/Speed stages**, plus **SAQ / power drills** for athletes (Wk02 Ch2 p126). The skill should
name this distinction so it doesn't cite "Functional Training" for barbell strength work. I'll
use a label like **"functional-strength track"** in the skill and map each component to its real
course stage.

---

## 3. What needs to be true before the skill hands someone this program

The template is powerful but narrow. The skill must gate it. Proposed **BLOCKING** pre-checks
(recorded in the plan's Screening / Program Strategy sections):

### 3a. Eligibility gate

1. **Medically cleared** per the ACSM preparticipation algorithm (Wk04 Ch5). Any CVD/metabolic/
   renal disease, or signs/symptoms, or risk factors + intent to train vigorously ⇒ medical
   clearance first. Heavy near-maximal lifting is vigorous intensity.
2. **Training status = experienced** (≥~1 yr consistent barbell training; can state recent
   working loads). Novices/early-intermediates ⇒ scaled path (§3c), not this template.
3. **Movement competence** — pass the course movement screens (bend-and-lift/squat, push, pull,
   single-leg, rotation; Wk06 Ch10) and the McGill torso-endurance battery / Thomas / shoulder-
   mobility tests as relevant. Compensations ⇒ a Movement-phase block first.
4. **Equipment** — barbell, rack, plates, bench, pull-up bar available. Otherwise the skill
   offers a DB/KB strength variant, not this one.
5. **Recovery context** — sleep, stress, weekly workload, life demands realistic for 4 hard
   sessions/week (Stage-2/3 intake).

If any gate fails: don't refuse the *goal*, refuse the *template* — route to the scaled path.

### 3b. Athlete vs general-population branching

|          | **Athlete**                                                                                    | **General population / physique / fat-loss**                                                     |
| -------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Emphasis | In-season maintenance vs off-season peak; sport-specific transfer                                    | Look/feel, PBs as motivation, fat loss                                                                 |
| Add-ons  | SAQ + plyometrics (Table 11-12 intensity factors), jump retest, sport calendar drives the macrocycle | Conditioning finishers for energy expenditure, higher accessory volume, Zone 1–2 cardio               |
| % wave   | As written; can run one focus lift + maintain others                                                 | Often better to run**one or two focus lifts** on the wave, others in the 6–12 range             |
| Retest   | Timed to competition / testing date                                                                  | Timed to end of block; can convert to rep-max estimate to avoid true 1RM if unclear on form under load |
| Deficit  | Usually only in a fat-loss phase, held out of the peak                                               | Central; periodised (§3c)                                                                             |

### 3c. Scaled entry for people who aren't ready for the template

For general-pop beginners / failed gates, the skill should offer a **course-native strength
progression** instead: Movement-phase pattern work → Load/Speed with 60–70% 1RM, 8–12 reps, 2–4
sets, double progression / 2-for-2, ~5% increments (Table 9-12, Table 11-10). Re-assess at
8–12 weeks; graduate to the Russian wave when the gates pass. This keeps "I want to get strong
and lose fat" answerable for everyone, not just trained lifters.

### 3d. Fat loss — honest, course-grounded, in-scope

- **Rate:** ISA/ACE weight-loss guidance = calorie deficit **500–1000 kcal/day → 1–2 lb/week**,
  split roughly **−250 kcal intake / +250 kcal expenditure** (Wk09 Ch12 p29–31). The skill
  should set this expectation rather than promise "very quickly."
- **Scope:** the trainer may give **general, non-medical** nutrition information only — no meal
  plans, no macros-as-prescription, no MNT. Detailed nutrition / disordered eating ⇒ **refer to
  a registered dietitian** (Wk01 Ch1; Wk09 Ch6 p5). The skill already enforces this; the
  fat-loss overlay must not weaken it.
- **Cardio for fat loss (Ch12 p32):** ≥5 d/wk, moderate (< VT1 / RPE 3–4), 30–60 min/day,
  building to **150–250 min/week**, low-impact. Resistance (Ch12 p33): 2–3 d/wk, 8–12 reps,
  2–4 sets, adequate protein to preserve lean tissue.
- **The recovery conflict:** a hard Russian peak (weeks 6–9: 90–105%) in an aggressive deficit
  degrades recovery and the retest. Two ways the skill can resolve it:
  1. **Periodise the deficit within the block** — moderate deficit (−250 to −500) during
     accumulation (wk 1–5), move to **maintenance** for intensification/peak (wk 6–9).
  2. **Sequence blocks** — run a dedicated 6–8 week fat-loss block first (denser accessory
     circuits, more Zone 1–2 cardio, larger deficit), then eat at maintenance and run the
     Russian wave for the strength peak.
     The skill should present both and pick based on the client's priority and timeline.

---

## 4. Proposed changes to the skill — file by file

### New files

| File                                       | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `references/russian-strength-program.md` | The cited digest. Decoded template (V5 4-day + classic 3-day + 2-day/8-week "masters" variant); the week-by-week wave table; the §2 mapping to IFT Load/Speed + linear periodization + Table 9-12; the §3a eligibility gates; the retest protocol (Ch 10 spotting + contraindications); the "accessories are not periodised" rule; the RPE/e1RM autoregulation layer (labelled); the fat-loss integration (§3d) with Ch 12 citations; explicit "when NOT to use / scale down" section. Every claim tagged Course-supported / Applied / General knowledge. |
| `templates/strength_block.csv`           | The 9-week wave expressed in the skill's existing CSV schema (`week,day,session,block,exercise,sets,reps,intensity,rest,tempo,duration,progression,notes`), with course-compliant warm-up (Movement-phase) and cool-down (Flexibility FITT-VP) rows and optional conditioning rows already placed on non-lower-body days. Serves as a worked example.                                                                                                                                                                                                      |
| `templates/strength_block_plan.md`       | Markdown fragment: the extra sections a strength-block plan needs — Eligibility Gate checklist, Wave Parameters (1RMs / e1RMs, units, focus lifts), Deficit Periodisation, Retest Plan, Autoregulation Rules. Slots into the existing`client_fitness_plan.md` structure.                                                                                                                                                                                                                                                                                  |
| `scripts/russian_block.py`               | Generator. Input: main-lift 1RMs (or RPE-anchored top sets → estimated 1RM), days/week (4/3/2), focus lifts, deficit mode. Output: CSV rows for the whole block with target loads =`round(%×1RM, 2.5)` (mirrors the xlsx formula), plus injected warm-up/cool-down/conditioning rows. Keeps the human reasoning in the `.md`.                                                                                                                                                                                                                          |

### Edited files

| File                                                               | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SKILL.md`                                                       | Mode B gains a**"Program archetypes"** note: after B4 step 1 (Program strategy), if the goal is strength/PBs and the client is Load/Speed-ready, consider the strength-block archetype; run the §3a eligibility gate; branch athlete vs general-pop (§3b); if not ready, use the scaled path (§3c). Add a **fat-loss overlay** sub-step to B4 (deficit periodisation, conditioning placement, protein, scope guardrail). Add the new reference to the file table.                                                                |
| `references/COURSE_MAP.md`                                       | New routing rows: "client wants a strength peak / powerlifting cycle / Russian program / to hit PBs / to test maxes" →`russian-strength-program.md` + Ch 11 periodization (p42–46) + Ch 9/11 Table 9-12 (p16) + Ch 10 1-RM assessment (p69–73). "Athlete / sport performance" → + SAQ/plyometrics (Ch 11 p33–41, Table 11-12) + Ch 2 p126.                                                                                                                                                                                               |
| `references/intake-questions.md`                                 | Stage-2 additions: population type (competitive athlete + sport/season / general fitness / physique-fat-loss); training age; current estimated 1RMs or recent top sets on squat/bench/DL/OHP; self-reported barbell competence (still verified by screen); barbell equipment access (BLOCKING for the template); days/week available (selects the 4/3/2-day variant); units (kg/lb). Fat-loss sub-block: current bodyweight trend, target rate, willingness to self-monitor intake (general info only), any history that should route to an RD. |
| `references/programming-reference.md`                            | New short subsection "Strength-peaking / linear-periodization block" cross-referencing`russian-strength-program.md`; a one-line reminder that ≥80% 1RM is an *experienced-lifter* value.                                                                                                                                                                                                                                                                                                                                                   |
| `scripts/validate_plan.py`                                       | If the plan uses the strength archetype: assert the Eligibility Gate section exists and every gate is marked pass/needs-clearance; a Retest Plan with a date exists; accessories in the CSV are not on the % wave; deficit mode and peak weeks aren't both "aggressive"; units are stated. Warn if the % wave is applied to >2 lifts for a general-pop client.                                                                                                                                                                                  |
| `evals/evals.json`                                               | New cases: (a) trained athlete wants to peak squat for a meet → strength block, retest timed to date; (b) 3-months-training beginner asks for "the Russian program" → skill declines the template, offers the scaled path, explains why (FITT-VP experience threshold); (c) "get strong + lose fat fast" → skill sets the 1–2 lb/wk expectation, periodises the deficit, stays in scope (no meal plan); (d) scope probe: client asks for macros → refer to RD.                                                                             |
| memory (`MEMORY.md` + a new `russian-strength-integration.md`) | Record that the skill now has a strength-block archetype and where it lives.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

## 5. The "modernise / make it flexible" layer

All of this stays inside what the course permits (RPE, 2-for-2, double progression,
periodization) — bar-speed cues are the only piece flagged as general knowledge.

- **Autoregulation:** target loads come from `% × 1RM`, but the skill adjusts them by a top-set
  RPE check on the day (e.g. if the prescribed load hits RPE ≥ 9 on the progression day two
  sessions running, hold or drop 5%; if the anchor day is ≤ RPE 6, nudge up). Estimated 1RM
  refreshed from rep-max data rather than requiring true maxes mid-block.
- **Schedule variants:** 4-day (V5), 3-day (classic), 2-day/8-week (masters, with 60–70% filler
  days) — chosen from the intake "days available" answer.
- **Focus-lift selection:** general-pop clients run 1–2 lifts on the wave and the rest in an
  8–12 hypertrophy range — running true peaking on squat+bench+DL+OHP simultaneously (as V5
  does) is a lot of near-maximal stress in one block.
- **Auto-deload:** insert a low week when 2-for-2 fails or RPE drifts up across a week.
- **Fat-loss mode toggle** on the generator: adds conditioning rows, shifts accessories toward
  circuit/superset density, and annotates the deficit periodisation.
- **Units:** kg/lb switch, loads rounded to the nearest 2.5 kg / 5 lb.

---

## 6. Caveats / things I want to flag

1. **The template is not for beginners.** Its 80% entry intensity is a course-defined
   experienced-lifter value. The scaled path (§3c) is what makes the skill usable for "anyone
   who wants to train."
2. **Simultaneous peaking of 5 lifts + a fat-loss deficit is aggressive.** The skill should
   default general-pop clients to fewer focus lifts and a periodised (not constant) deficit.
3. **"Lose fat very quickly"** — I'd have the skill hold the course line (1–2 lb/wk, deficit
   500–1000 kcal/day) and explain the lean-mass / adherence trade-off, rather than optimise for
   speed. Tell me if you want a different stance.
4. **1RM retest** in week 9 is a formal assessment — spotting, contraindication screen, and a
   medical-clearance check have to precede it.
5. **Scope of practice on nutrition is unchanged** — general info only, RD referral for
   anything detailed. The fat-loss overlay must not become a meal plan.
6. **This is a design plan, not a client program.** No `clients/` files are created until you
   point the skill at a real person.

---

## 7. Open questions for you

1. **Primary audience** — build for competitive athletes first, general-population fat-loss
   first, or genuinely both with equal weight?
2. **Wave scope** — keep V5's "all 5 lifts on the wave at once," or default to 1–2 focus lifts
   with the rest on hypertrophy work (classic Russian style)?
3. **Which variants** — just the 9-week V5 wave, or also the classic 6-week and a longer
   masters/2-day version?
4. **Generation** — do you want `scripts/russian_block.py` to auto-build the CSV from entered
   1RMs, or keep the CSV hand-written each time?
5. **Fat-loss messaging** — hold the course's 1–2 lb/week line, or do you want a more
   aggressive-but-flagged option?
6. **Units default** — kg or lb?
7. **Retesting** — always a true 1RM in week 9, or default to an estimated 1RM from a rep-max
   for general-pop clients?

---

## Appendix — sources

- Lift Vault — *Russian Squat Routine* (structure, origin, "+5–10%", experienced-lifter framing,
  recovery demand, masters variant): [https://liftvault.com/programs/powerlifting/russian-squat-routine-spreadsheet/](https://liftvault.com/programs/powerlifting/russian-squat-routine-spreadsheet/)
- Lift Vault — *Extended Russian Power Routine*: [https://liftvault.com/programs/powerlifting/extended-russian-power-routine-spreadsheet/](https://liftvault.com/programs/powerlifting/extended-russian-power-routine-spreadsheet/)
- Norma Athletics — *Russian Squat Program: 6-Week Cycle Explained*: [https://www.norma-athletics.at/guides/russian-squat-cycle/](https://www.norma-athletics.at/guides/russian-squat-cycle/)
- Cast Iron Strength — *The Russian Squat Routine*: [https://www.castironstrength.com/russian-squat-routine/](https://www.castironstrength.com/russian-squat-routine/)
- Your source log — published Google Sheet (classic single-lift cycle, 125→132.5 kg squat)
- Syatt Fitness — *Powerlifting for Fat Loss*: [https://www.syattfitness.com/powerlifting-for-fat-loss/powerlifting-for-fat-loss-3-training-and-nutrition-tips-to-build-your-strongest-leanest-body/](https://www.syattfitness.com/powerlifting-for-fat-loss/powerlifting-for-fat-loss-3-training-and-nutrition-tips-to-build-your-strongest-leanest-body/)
- PowerliftingTechnique — *Powerlifting For Fat Loss*: [https://powerliftingtechnique.com/powerlifting-fat-loss/](https://powerliftingtechnique.com/powerlifting-fat-loss/)
- ISA CPT course notes (in-repo): Wk02 Ch2 (IFT model / Load-Speed stage), Wk06 Ch10 (movement
  screens, 1-RM assessment), Wk07 Ch10–11 (Table 9-12, FITT-VP Table 11-10, periodization
  p42–46, plyometrics Table 11-12, SAQ), Wk04 Ch5 (ACSM screening), Wk09 Ch6 & Ch12 (nutrition
  scope, weight-loss FITT).
