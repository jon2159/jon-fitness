# REVL programming — reverse-engineered analysis (Step 2)

Input: `source/revl_raw_data.md` (264 screenshots, Block 1 + Block 2 2026, read by two
independent OCR engines) plus direct visual reading of a sample of the source images.
Quantitative tables produced by `source/analyze_revl.py`.

This file is the **analysis layer**. The skill-facing guidance distilled from it lives in
`.claude/skills/jon-fitness/references/revl-class-integration.md`.

## Evidence labelling

- **[Observed]** — directly supported by the screenshots / OCR of specific sessions.
- **[Pattern]** — repeated programming behaviour seen across many sessions; supported by
  the counts below.
- **[Inference]** — a reasonable reading of programming *intent*. Not stated by REVL.

**Evidence quality.** The posters are stylised type over photographs. Both OCR engines
lose word spacing and misread digits; small print is unreliable. Session/day/phase labels
come from folder and file names, not from the images. **No specific load, %, rep count,
tempo or time cap in this file should be quoted as fact** — they are indicative. Where a
number mattered, it was confirmed by opening the image directly; those are marked
*(image-checked)*.

### Two facts confirmed by the studio (2026-09-09) that govern how everything below is read

**1. Team-format rep totals are SHARED, not per person.** Any session marked *In Pairs*,
*YGIG*, or *Teams of N* lists the **team's** total reps/calories. Per-person volume is
roughly the printed number **÷ team size**, and the format carries a built-in work:rest
ratio (**1:1** in pairs, **1:2** in teams of 3, lower still in teams of 4–6). These sessions
are therefore **interval work with substantial rest**, not continuous grinds. Every rep
total quoted for *Complete* and *Sweat Team* below is a **team total** unless stated.
*(Confirmed by the studio; the posters themselves do not say so.)*

**2. Peak is three weeks, and weeks 2 and 3 are testing weeks.** **[Observed + confirmed]**
- **Peak Wk 1** (programme wk 8) — the heavy wave.
- **Peak Wk 2** (wk 9) — **1RM & 3RM strength testing.** *(image-checked: Monday Perform
  Total = `S1. 30:00 Cap — 0:00–18:00 1RM BB Deadlift; 18:00–30:00 1RM BB Push Press/Jerk`,
  with example builds `60-70-80-90-100-100+% of goal 1RM` and High/Moderate/Low volume
  paths.)*
- **Peak Wk 3** (wk 10) — **Sweat Engine and Sweat Sprint baseline testing.**
  *(file-confirmed: `tuesday sweat engine baseline`, `thursday sweat sprint baseline`.)*

3 + 3 + 1 + 3 + 3 = 13. The brief's "Peak (1 week)" refers to the peak *effort*, not the
phase length.

---

# A. Macrocycle map

## A1. Phase-level shape

| Phase | Wks | Purpose **[Inference]** | Main-lift load **[Observed]** | Volume | Complexity | Conditioning | Recovery demand |
|---|---|---|---|---|---|---|---|
| **Volume** | 1–3 | Accumulate work capacity, muscle and pattern familiarity before loads rise | %1RM tokens cluster **40–65%** (`40`, `45-50-50`, `50-50-60-60`, `50-50-60-65`, `40-40-50-50`) | Highest reps (8–14), highest density | Moderate — tempo/eccentric cues on **52%** of sessions | High (partner/team format on **80%**) | Moderate-high, mostly **metabolic + muscular** |
| **Build** | 4–6 | Convert accumulated volume into force | Tokens climb to **50–90%** (`50-60-70-75`, `55-65-75-80-85-85`, `60-70-75-80-85`, `60-70-80-85-90-90`) | Reps fall (6–10) | Tempo cues drop to **30%** — attention shifts to load | Team format drops to **44%** — more individual work | Rising **neural** demand |
| **Deload** | 7 | Shed accumulated fatigue before the heavy weeks | Tokens fall back to **30–55%** (`40-50`, `40`, `40-45-50-55`, `30-40`) | Strength sets cut (e.g. *Every 3:30 × 4*, ~8 reps) *(image-checked)* | Density work **rises to 90%** of sessions | Team format **85%** | **Strength deload only** — see A3 |
| **Peak** | 8–10 | Express maximal strength; re-test benchmarks | The single wave token is `60-70-80-90-95-95` *(image-checked, Block 1)*; Block 2 tops at `…-90-92.5%` *(image-checked)* | Lowest reps (1–5), longest rest (`:45` between exercises) | Density work **lowest (49%)** — rest is protected | Team format **43%** | Highest **neural** demand |
| **Rebuild** | 11–13 | Re-accumulate; bridge into the next block | Only `40-50` warm-up tokens legible; **%-prescription drops to 12%** of sessions | Moderate | Tempo cues back to **50%** | Team format back to **85%** | Moderate, back toward metabolic |

## A2. The variable that actually changes across the block

**[Pattern]** Movement *selection* is close to constant; **load and rep-scheme** carry the
periodisation. Barbell-pattern exposure barely moves phase to phase:

| Phase | Sessions containing BB squat | Sessions containing BB hinge |
|---|--:|--:|
| Volume | 32% | 53% |
| Build | 32% | 52% |
| Deload | 25% | 50% |
| Peak | 26% | 44% |
| Rebuild | 23% | 55% |

**[Inference]** REVL periodises *intensity*, not *exercise menu*. For a PT this matters:
you cannot assume a phase "gives the squat a rest" — the pattern is trained in every phase;
only the load changes.

## A3. The Deload is a **strength** deload, not a whole-body deload

**[Observed, image-checked]** In Deload week the Monday *Perform Total* main lift drops to
*8 × BB deadlift @40–50%, Every 3:30 × 4* — genuinely light and low-set. But the same
week's Sunday *Complete* is `In Pairs – E5MOM × 8` containing **60 × BB shoulder-to-overhead
+ 40 × BB back/front squat + 60 × BB RDL/sumo deadlift + 40 × BB Pendlay row** plus bike and
ski intervals — on the order of 200 barbell reps.

**[Inference]** The deload protects **neural / high-load** capacity while leaving muscular-
endurance and metabolic work largely intact. Density prescriptions actually *peak* in this
week (EMOM-style formats on 90% of sessions).

**PT implication.** Deload week is a **good** window for low-load technique, mobility and
corrective work, and a **poor** window for adding more high-rep metabolic volume.

## A4. Prescription-style drift

| Quality (% of that phase's sessions) | Volume | Build | Deload | Peak | Rebuild |
|---|--:|--:|--:|--:|--:|
| %1RM prescribed | 30% | 29% | 30% | 18% | 12% |
| RIR prescribed | 13% | 24% | 0% | 10% | 17% |
| RPE prescribed | 23% | 24% | 25% | 28% | 17% |
| Tempo / eccentric cue | 52% | 30% | 40% | 41% | 50% |
| EMOM / interval density | 72% | 67% | 90% | 49% | 80% |
| **AMRAP / time-capped** | **100%** | **100%** | **100%** | **100%** | **100%** |
| Partner / team format | 80% | 44% | 85% | 43% | 85% |

**[Pattern]** Three readings:
1. **Every session in every phase is time-capped.** There is no untimed, purely
   self-paced session anywhere in the 264. **[Observed]**
2. **%1RM prescription falls away in Peak and Rebuild** while RPE rises — the heaviest
   phase leans on *"build to a heavy 3"*-style autoregulation as much as on fixed
   percentages. **[Observed]** **[Inference]** this is sensible for a group setting where
   individual 1RMs are unverified.
3. **Rest is protected only in Peak** (density formats drop to 49%). Everywhere else the
   session is a density/partner format. **[Pattern]**

## A5. Week-by-week map (where the evidence allows)

| Wk | Phase | Main-lift character **[Observed]** | Dominant added stress **[Inference]** |
|---|---|---|---|
| 1–3 | Volume | 8–14 reps @ ~40–65%, 3 s eccentrics, short rest | Muscular / metabolic |
| 4–6 | Build | 5–10 reps, waves reaching ~85–90%, RIR tightens (4–5 → 2–3) *(image-checked)* | Mixed muscular + rising neural |
| 7 | Deload | ~8 reps @ 40–50%, few sets, long rest — **but Sunday keeps its volume** (shared, so ~100 barbell reps/person) | Metabolic only |
| **8** | Peak Wk 1 | The heavy wave: 1–5 reps, to ~90–95%, `:45`+ rest | Neural |
| **9** | **Peak Wk 2 — 1RM & 3RM TESTING** | *image-checked:* `30:00 Cap — 0:00–18:00 1RM BB Deadlift; 18:00–30:00 1RM BB Push Press/Jerk`; builds `60-70-80-90-100-100+%` of goal 1RM | **Maximal — the highest-stakes week in the block** |
| **10** | **Peak Wk 3 — conditioning baseline testing** | Sweat Engine and Sweat Sprint **baseline** sessions (file-confirmed); strength days return to normal loading | Maximal metabolic |
| 11–13 | Rebuild | Moderate loads, %-prescription largely replaced by RPE/RIR | Muscular / metabolic |

**[Pattern]** Both blocks follow this shape; Block 2 tops its Peak deadlift wave at ~92.5%
where Block 1 reaches ~95% *(image-checked)*. Treat the exact ceiling as block-specific.

---

# B. Movement-pattern frequency — the weekly architecture

## B1. Overall exposure (share of all 264 sessions)

| Pattern | sessions | % |
|---|--:|--:|
| Hinge (any implement) | 200 | 76% |
| Squat (any implement) | 195 | 74% |
| Erg / machine cardio | 182 | 69% |
| Unilateral lower | 162 | 61% |
| Core / trunk | 145 | 55% |
| Olympic / ballistic | 145 | 55% |
| Horizontal push | 140 | 53% |
| Vertical push | 126 | 48% |
| Vertical pull | 112 | 42% |
| Horizontal pull | 104 | 39% |
| Running / locomotion | 88 | 33% |
| Burpee / mixed metcon | 79 | 30% |
| **Rotation / anti-rotation** | **40** | **15%** |
| **Carry / loaded hold** | **33** | **12%** |

**[Pattern]** Squat and hinge are near-ubiquitous. **Carries and rotation/anti-rotation are
the two clearly under-trained patterns** — the standing PT opportunity.

## B2. Barbell-specific exposure by weekday — the load that actually matters

Keyword counts split barbell work from squat-/hinge-*pattern* conditioning implements:

| Movement | Mon | Tue | Wed | Thu | Fri | Sat | Sun | all |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| BB deadlift / sumo / RDL | **100%** | 12% | **71%** | 8% | 33% | 15% | **73%** | **51%** |
| BB back/front squat | 8% | 4% | **50%** | 0% | **48%** | 4% | **62%** | 28% |
| BB bench press | 38% | 0% | 50% | 0% | **63%** | 0% | 54% | 35% |
| BB strict press / STO / jerk | **65%** | 15% | 19% | 23% | 46% | 23% | **62%** | 38% |
| BB power clean / snatch | 33% | 31% | **67%** | 27% | 12% | 38% | 15% | 34% |
| Wall ball / thruster / DBall *(squat-pattern conditioning)* | 56% | **69%** | 44% | **69%** | 48% | **69%** | 31% | 54% |
| KB swing *(hinge conditioning)* | 15% | **50%** | 35% | 42% | 19% | 38% | 35% | 30% |

**[Pattern] Key readings:**

1. **Barbell hinge is the most repeated heavy pattern in the programme** — on 51% of all
   sessions and **100% of Mondays**, plus 71% of Wednesdays and 73% of Sundays. A member
   attending 5–6 sessions is loading the hinge on most of them.
2. **Tue / Thu / Sat are genuinely conditioning days for the barbell** (BB squat 0–4%,
   BB hinge 8–15%) — **but they are not "lower-body rest"**: wall balls / thrusters / DBall
   appear on ~69% of them and KB swings on 38–50%. The squat and hinge *patterns* are loaded,
   just with lighter implements at high rep counts.
3. **Sunday "Complete" is the highest barbell-density day after Wednesday** — BB squat 62%,
   hinge 73%, press 62%, bench 54%. It is a full-body barbell + conditioning session, **not
   a recovery day** (see C4).
4. **Wednesday is the heaviest mixed day** — BB squat 50%, BB hinge 71%, BB power clean 67%.
5. **Friday is the upper-body day** — BB bench 63%, horizontal pull 67%, and BB squat only
   in the parallel *Move Total* track.

## B3. Exposure by session type

| Pattern | Perform Total (26) | Perform Lower (26) | Perform Upper (26) | Move Total (78) | Sweat Sprint (24) | Sweat Engine (24) | Sweat Team (27) | Complete (26) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| Squat | 62% | **100%** | 0% | 74% | 83% | 92% | 93% | 81% |
| Hinge | **100%** | **100%** | 8% | **100%** | 42% | 62% | 63% | 88% |
| Unilateral lower | 81% | **100%** | 0% | 76% | 33% | 42% | 63% | 69% |
| Horizontal push | 73% | 4% | **100%** | 72% | 21% | 25% | 26% | 77% |
| Vertical push | 92% | 8% | 46% | 62% | 25% | 33% | 30% | 65% |
| Horizontal pull | 62% | 0% | 96% | 49% | 4% | 8% | 0% | **85%** |
| Vertical pull | 58% | 38% | 81% | 44% | 38% | 46% | 11% | 15% |
| Carry / hold | 19% | 23% | 8% | 17% | 8% | 8% | 7% | 0% |
| Rotation / anti-rot. | 12% | 19% | 42% | 22% | 0% | 0% | 4% | 12% |
| Core / trunk | 77% | 69% | 46% | 72% | 38% | 62% | 22% | 19% |
| Olympic / ballistic | 58% | **96%** | 4% | 47% | 79% | 62% | 70% | 35% |
| Erg / machine | 12% | 15% | 4% | 85% | **100%** | **100%** | **100%** | **100%** |
| Running | 0% | 0% | 0% | 9% | **100%** | 75% | 70% | 54% |

**[Pattern]**
- **Perform Lower is the single densest lower-body session:** squat, hinge, unilateral *and*
  Olympic/ballistic all ≥96%. *(image-checked: Volume Wk 1 = squat @45–50–50% with 3 s
  eccentrics, KB swings, box step-ups, EMOM power cleans, lunges, box jumps, DBall
  ground-to-overhead.)*
- **Perform Upper is a genuinely isolated upper day** (0% squat, 8% hinge, 0% unilateral) —
  the only session in the programme that leaves the lower body alone.
- **Move Total is a true hybrid:** 100% hinge and 85% erg in the same session.
- **Complete has the highest horizontal-pull exposure of any session type (85%).**

## B4. Recurring pairings **[Pattern]**

- Main barbell lift **+** an opposing-pattern accessory in the same EMOM/E2MOM slot
  (e.g. bench + Pendlay row; deadlift + ring plank + KB row) — antagonist pairing is the
  house style.
- Squat-pattern strength **+** hip-hinge ballistic (KB swing, power clean) on the same day.
- Erg interval **+** a loaded squat-pattern implement (wall ball / thruster / DBall) —
  the standard Sweat couplet.
- Unilateral lower **+** anti-rotation or plank as the accessory pair on Perform/Move days.

## B5. Typical set/rep structures **[Observed]**

- **S1** = the strength block: an *Every 2:15–3:30 × 4–8* density slot holding the main
  barbell lift plus 1–2 accessories.
- **S2** = 2 × 7:00–8:00 AMRAP/cap blocks, usually A + B couplets.
- **S3** = a 4:00–6:00 partner/YGIG finisher.
- Rep schemes: descending ladders (`14-12-10-10`, `10-8-6`, `12-10-8-6`), ascending ladders
  (`8-10-12…`, `2-3-4…`), and wave clusters in Peak (`6-5-4-3-2-1+1`).
- Warm-up is consistently 4:00-capped and **ramps the day's main pattern** at ~40%.

---

# C. Training stimulus & recovery footprint

Framing: *what stimulus has the client already received, and what can a PT session add
without duplicating it?* REVL is a legitimate, well-structured stimulus — this section maps
its footprint, not its faults.

## C1. Lower-body muscular load — **very high, every week**

**[Pattern]** Squat pattern on 74% of sessions, hinge on 76%, unilateral on 61%. Barbell
hinge specifically on 100% of Mondays. Even the conditioning days load the squat pattern via
wall ball / thruster / DBall (69% of Tue/Thu/Sat).
**[Inference]** There is **no day in a full REVL week where the lower body is unloaded.**
Additional lower-body volume from a PT session is the single easiest way to over-reach.

## C2. Upper-body muscular load — **high but more concentrated**

**[Pattern]** Horizontal push 53%, vertical push 48%, horizontal pull 39%, vertical pull 42%.
Friday (Perform Upper) and Sunday (Complete) carry most of it; Perform Lower is 0–4% upper.
**[Inference]** Upper-body pulling — especially **horizontal pull volume outside Friday and
Sunday** — is comparatively under-served and is a reasonable PT target.

## C3. Axial / spinal loading — **the most repeated high-cost exposure**

**[Pattern]** BB deadlift/RDL on 51% of all sessions; BB back/front squat 28%; BB
shoulder-to-overhead 38%. Mondays are 100% barbell hinge.
**[Inference]** Cumulative axial loading is the stress most likely to be *repeated* rather
than rotated. A PT session that adds more loaded spinal flexion/extension or another heavy
axial lift is duplicating the most-saturated stimulus in the programme. Unloaded, offset or
horizontally-supported alternatives complement better.

## C4. "Complete" and "Sweat Team" — high work-capacity, but **shared and interval-paced**

**[Observed, image-checked]** — remember every number here is a **team total** (see the
confirmed facts at the top):
- *Volume Wk 1 Complete* — **In Pairs YGIG**, Every 2:30 × 16 (≈40 min): 25/20/15 unbroken
  BB bench, 24/18/12 cal ski AFAP, 25/20/15 unbroken BB front squat, 20/16/12 toes-to-bar.
  **Per person ≈ half, with ~1:1 work:rest.**
- *Peak Wk 1 Complete* — **Teams of 3 (1:2)**, 40:00 cap: 120 power cleans, 140 wall balls,
  140 cal bike, 1000 m run; then a second equal block.
  **Per person ≈ 40 cleans / ~47 wall balls, working ~1/3 of the 40 min.**
- *Volume Wk 1 Sweat Team* — **Teams of 4–6**, 3 × 15:00 caps: 400/300/200 cal erg per block
  plus BB deadlifts, DB front-rack squats, DB snatches, plate overhead carries.
  **Per person ≈ 67–100 cal per block.**

**[Inference]** These are **extensive interval sessions**, not continuous grinds. The
per-person work is real but the 1:1–1:2 rest makes them **moderate-to-high**, not the biggest
sessions of the week — Wednesday (Perform Lower) and Peak-week Mondays are heavier.
The practical reading for a PT: Saturday and Sunday are **glycolytic/aerobic volume with
built-in recovery**, so they are *not* a reason to write off Monday, but they do mean the
client arrives at Monday with metabolic (not neural) fatigue.

**Do not** convert a printed team total into an individual's workload without dividing by
team size — the raw posters read far heavier than the session actually is.

## C5. High-neural / near-maximal exposure — **concentrated in Build and Peak**

**[Observed]** Waves reaching ~85–90% in Build and ~90–95% in Peak (Block 1) / ~92.5%
(Block 2). Olympic/ballistic movements on 55% of all sessions (power clean, snatch, box
jump, DBall power).
**[Inference]** Volume, Deload and Rebuild leave meaningful neural headroom. **Build and Peak
do not.** Adding a second heavy or near-maximal exposure in those phases is the classic
over-reach.

## C6. Metabolic / conditioning load — **continuous**

**[Pattern]** Erg or machine work on 69% of sessions; running on 33%; every session in every
phase is time-capped; partner/density formats on 43–85% depending on phase.
**[Inference]** Aerobic *and* glycolytic systems are already stimulated 4–6× a week. Extra
conditioning is rarely the highest-value PT addition — with one exception: **true low-
intensity Zone 1–2 aerobic work is largely absent** (everything is capped and competitive),
so a client who actually lacks an aerobic base may benefit from easy steady-state that REVL
never programmes.

## C7. Local muscular fatigue and repeated exposure

**[Pattern]** Grip (deadlifts, carries, erg, hangs, KB), anterior shoulder (press on 38% of
sessions, wall balls, burpees) and the posterior chain are hit repeatedly across days.
**[Inference]** Grip and shoulder are plausible accumulation sites; a PT should ask before
adding more of either.

## C8. Where recovery capacity appears to be protected **[Inference]**

- The **week 7 deload** cuts strength load meaningfully (A3).
- **Peak** protects rest — density formats drop to their lowest (49%) and rest cues appear
  (`:45` between exercises).
- **Perform Upper (Friday)** is a deliberate lower-body offload day.
- The **Perform / Move choice** on Mon/Wed/Fri lets a member self-select a lower-neural
  option (Move, RIR-based) instead of a %1RM one.
- Warm-ups are consistently capped and ramp the day's pattern.

## C9. Complementary PT opportunities that the counts support

| Opportunity | Why the data supports it |
|---|---|
| **Carries / loaded holds** | present on only **12%** of sessions |
| **Rotation / anti-rotation** | present on only **15%**; 0% on Sweat Sprint/Engine |
| **Horizontal pulling volume** | 39% overall and concentrated on Fri/Sun |
| **Movement quality & technique under sub-maximal load** | REVL is time-capped in 100% of sessions — no untimed technique work exists in the programme |
| **True Zone 1–2 aerobic work** | every session is capped/competitive; no easy steady-state observed |
| **Mobility / tissue work** | appears only inside 4:00 warm-ups |
| **Unilateral *stability* (as opposed to unilateral loading)** | unilateral lower is 61%, but almost always loaded and under time pressure |
| **Individual assessment & weak-point work** | group format cannot individualise; no screening in the programme |
| **Deliberate low-stress / restorative sessions** | nothing in the week is programmed below a cap |

---

# D. Weekly stress map

Dominant stress by day, for a member attending the full week. Sessions a member self-selects
(Perform vs Move) are shown together.

| Day | Session | Dominant stress **[Inference]** | Evidence **[Observed/Pattern]** |
|---|---|---|---|
| **Mon** | Perform Total / Move Total | **High muscular + high axial**; neural high in Build/Peak | BB hinge **100%**, vertical push 65%, unilateral 87% |
| **Tue** | Sweat Sprint *or* Engine | **Conditioning-dominant** (glycolytic if Sprint), moderate squat-pattern muscular | erg 100%, running 85%, wall ball/thruster 69%, BB ~0–12% |
| **Wed** | Perform Lower / Move Total | **Highest mixed day — high muscular + high neural** | BB hinge 71%, BB squat 50%, BB power clean 67%, unilateral 85% |
| **Thu** | Sweat Engine *or* Sprint | **Conditioning-dominant** (aerobic if Engine) | erg 100%, running 92%, BB squat 0% |
| **Fri** | Perform Upper / Move Total | **Upper-dominant; the lower-body offload day** (Perform track) | BB bench 63%, horiz. pull 67%, BB squat 8% on the Perform track |
| **Sat** | Sweat Team | **Moderate–high mixed conditioning**, team format with 1:3–1:5 rest | erg 100%, 3 × 15:00 caps, reps shared across teams of 4–6 |
| **Sun** | Complete | **Moderate–high full-body work capacity** — reps shared in pairs / teams of 3 (1:1–1:2 rest) | BB hinge 73%, BB squat 62%, BB press 62%, horiz. pull 85%, erg 100%, 40:00 caps |

## D1. Favourable windows for a 1-on-1 PT session **[Inference]**

| Window | Why | Best PT content |
|---|---|---|
| **Friday, or the day after Perform Upper** | lower body least loaded | lower-body technique, single-leg stability, mobility — *not* a heavy squat/deadlift |
| **The day after Sweat Engine** (aerobic, low neural residue) | least neural residue of the conditioning days | skill/technique work, moderate-load accessory |
| **Deload week (wk 7)** | strength load genuinely reduced | assessment, technique, mobility, corrective, weak-point at low load |
| **Volume or Rebuild phases** | most neural headroom (A1, C5) | the only phases where added strength work is comfortably justified |

## D2. Windows to avoid adding load **[Inference]**

| Window | Why |
|---|---|
| **Within ~24 h either side of Wednesday** | densest mixed day: BB squat + hinge + power clean |
| **Monday, for anything hinge-loaded** | BB hinge on 100% of Mondays |
| **Build and Peak phases, for a second heavy exposure** | waves already at 85–95% |
| **Peak Wk 2 — the 1RM/3RM testing week** | genuine maximal singles; protect the test, add nothing load-bearing near it |
| **Peak Wk 3 — conditioning baseline testing** | maximal metabolic efforts; don't blunt them with added conditioning |
| **Sat–Sun**, for *additional* metabolic volume | already 2 conditioning sessions, albeit interval-paced with shared reps |
| **Deload week, for high-rep metabolic volume** | Sunday keeps its volume even in the deload |

## D3. The testing weeks are an **opportunity**, not just a hazard **[Inference]**

Peak Wk 2 hands the PT something the group format usually withholds: a **current, validated
1RM** on the deadlift and an overhead lift (and 3RMs), obtained under coaching. Peak Wk 3
does the same for conditioning benchmarks.

Two practical consequences:
1. **Protect those two weeks** — no added load-bearing or maximal work.
2. **Use the numbers afterwards.** A PT strength block that needs a real 1RM
   (`russian-strength-program.md` gate G4 / retest §7) is best started in **Rebuild**, driven
   by the freshly-tested maxes, rather than testing the client again.

---

# E. Reproducing this analysis

```
python source/extract_revl.py     # -> source/revl_raw_data.md  (Step 1)
python source/analyze_revl.py     # -> the frequency tables used above
python source/analyze_revl.py --show-keys   # the exact keyword lists
```

Method limits, stated plainly: keyword presence is a **lower bound** on exposure (synonyms
and OCR misses are not captured); it counts *sessions containing* a pattern, not sets or
reps; and it cannot see load actually used by an individual member. Every percentage here
describes the **programme as written**, not any one client's week — which is why the skill
reference insists on asking the client what they actually did.
