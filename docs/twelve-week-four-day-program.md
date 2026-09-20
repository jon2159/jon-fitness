# 12-week, 4-day integrated program — reference build

Status: **illustrative, not for a real client until intake and the eligibility gate are complete.** Draft 2026-09-20.
It applies the skill's three foundations (ISA CPT, Russian V5, REVL logic) plus the research reviewed for Chalk's
methods (`references/chalk-design-reference.md` §6). Every decision below follows
**source principle → gap → evidence → decision**, and the evidence is graded honestly.

## 0. What Chalk does and doesn't say about "4-day, 12 weeks"
- Chalk's **Upper/Lower** plan is "a focused 4-day training plan … in just 12 weeks" (its sample page).
- Chalk's **full-body** tracks are **5-day** (FBA) and **3-day / 8-week**; neither is 4-day.
- The V5 wave is 4-day with **every day pairing a lower-body and an upper-body lift** (A = squat + bench, B = deadlift
  + press + pull-up), so it *is* a four-day full-body-per-session split. The 12-week horizon here is **our design**
  (9-week wave + test week + 2 rebuild weeks), not something Chalk or the Russian source prescribes.

**Generator:** `scripts/hybrid_block.py` writes this block as skill-schema CSV (`--cap-100` when G4 has not been passed).

## 1. Reference profile (assumed, not a client)
Experienced, medically cleared lifter passing G1–G7; barbell, rack, bench, pull-up bar, bike; **primary goal maximal
strength on squat / bench / deadlift, secondary work capacity**; 60–75 min per lifting session; not attending REVL
classes; **four total planned training days** (intake P19). Loads use `round(pct × 1RM, 2.5 kg)`. If G4 fails, use
an estimated 1RM and **cap the wave at 100%** (no 105% single).

## 2. Decisions and their evidence

| # | Decision | Source principle | Evidence (grade) |
|---|---|---|---|
| 1 | 4 days, each lower + upper; each lift 2×/wk, ~72 h apart | V5 A/B layout; ISA 48–72 h spacing (Wk07 Ch11) | Ramos-Campo 2024 (14 studies, 392 adults, **abstract read**): split vs full-body no difference in strength or hypertrophy when volume is equated. Frequency is a scheduling choice (Schoenfeld 2019; Grgic/Ralston 2018 — summaries) |
| 2 | Keep V5's linear wave **and** its fixed anchor day | V5 | Moesgaard 2022 (35 studies, **abstract read**): periodized > non-periodized for 1RM (ES 0.31); undulating > linear for 1RM (ES 0.31), larger in trained lifters (ES 0.61, CI 0.00–1.22, borderline); no hypertrophy difference. The anchor/progression pairing adds weekly undulation to a linear wave — **my inference**, not a source claim |
| 3 | **Conditioning is a separate session from lifting** (Fri PM, ≥ 3 h after lifting) | REVL logic: conditioning falls as strength intensity rises | Petré 2021 (27 studies, **abstract read**): concurrent training lowered lower-body 1RM in **trained** people (ES −0.35), more so **same-session**; advises trained lifters separate endurance from lifting when maximal strength is the priority. Schumann 2022: explosive-strength loss same-session, not with ≥ 3 h between (subgroup; abstract via note) |
| 4 | Conditioning = **short bike sprint intervals** | REVL supplies conditioning; V5 supplies none | Ferraro-Farro 2026 (9 RCTs, 177 healthy adults, **abstract read**): sprint-interval + resistance training vs resistance alone — no significant difference in lower/upper strength, jump or sprint; VO₂max higher (SMD 0.78); short sprints (≤ 10 s) gave greater jump gains (sensitivity analysis). Vechin 2021 (model paper, **abstract read**): very intense HIIT minimises interference; HIIT *before* lifting with no rest can interfere. **Limits:** small trials, healthy adults, training status unclear |
| 5 | Bike by default (low impact, easy to standardise) — **judgement, not evidence-proven** | — | Wilson 2012 (endurance training generally): running worse. **Sabag 2018 (HIIT, abstract read): cycling trended worse for lower-body strength (ES −0.377, ns) than running (−0.176, ns)**. Modality is unresolved; spacing the modes is better supported |
| 6 | Box-jump primer, low dose | REVL Olympic/ballistic exposure | de Villarreal 2009 (summary): benefits need ~> 40 jumps/session and > 15 sessions; ours is 20 contacts, so it is **maintenance/technique, not a power block**. Not a potentiation protocol (Seitz & Haff 2016) |
| 7 | Press + weighted pull-up at maintenance; accessories 2–3 × 8–12 | V5 subset rule; V5 accessories | Heavy loads favour 1RM strength, hypertrophy similar across loads near failure (Schoenfeld 2017; Lopez 2021 — summaries). Effort near failure only on accessories, not on wave sets |
| 8 | Week 10 = test / reassess with **reduced load, not complete rest** | V5 has no deload; ISA planned recovery | Coleman 2024 (RCT, **resistance-trained**, abstract read): a full week off did not help and lower-body strength improved more with continuous training; hypertrophy, power and endurance unaffected. Bell 2023 (Delphi consensus) is expert practice |
| 9 | Priority lifts fixed; only accessories rotate | Chalk's "hidden overload" through variation | Fonseca 2014 (untrained) favoured variation; Baz-Valle 2019 (trained) similar strength (summaries). Mixed |
| 10 | Log every session; weekly review | ISA progression / reassessment | Michie 2009 (122 evaluations): self-monitoring + ≥ 1 other technique → larger effect (0.42 vs 0.26). Behaviour-change evidence, not strength-specific |

## 3. The week (weeks 1–9, the V5 wave)

| Day | Session |
|---|---|
| **Mon — A anchor** | Primer: box jumps 4×5 (wk 1–6; 3×3 wk 7–9), full recovery. **Squat 6×2 @ 80%**, rest 3 min. **Bench 6×2 @ 80%**, 2–3 min. Bulgarian split squat 2–3 × 8–12/side, RIR 2–3. Weighted pull-up 3 × 6–8 @ ~70% (maintenance) |
| **Tue — B anchor** | **Deadlift 6×2 @ 80%**, 3 min. Military press 3 × 6–8 @ ~70%. Farmer carry 4 × 30 m. Face pulls 2–3 × 8–12 |
| **Wed** | Off training. Easy aerobic 30–40 min, below the first ventilatory threshold (talk test) |
| **Thu — A progression** | Primer as Mon (wk 1–6). Squat then bench per the wave table below. Dips 2–3 × 8–12 |
| **Fri — B progression** | Deadlift per the wave table. Military press and weighted pull-up stay at 3 × 6–8 @ ~70%. **PM, ≥ 3 h later:** sprint-interval session (§4) |
| **Sat / Sun** | Off. One easy aerobic 30–45 min session; mobility and walking |

**Wave table (source: V5 workbook rows 16–51):**

| Wk | Anchor Mon/Tue | Progression Thu/Fri | Load |
|---|---|---|---|
| 1 | 6×2 | 6×3 | 80% |
| 2 | 6×2 | 6×4 | 80% |
| 3 | 6×2 | 6×5 | 80% |
| 4 | 6×2 | 6×6 | 80% |
| 5 | 6×2 | 5×5 | 85% |
| 6 | 6×2 | 4×4 | 90% |
| 7 | 6×2 | 3×3 | 95% |
| 8 | 6×2 | 2×2 | 100% |
| 9 | 6×2 | 1×1 | 105% (test, only if G4 passes) |

**Rest:** 2–5 min on sets ≥ 85% (ISA Table 9-12, strength row); 3 min on the 80% sets (Judgement — no table row covers
80% × 2–6); 60–90 s on accessories. **Warm-up:** 5 min easy cardio, ankle/hip/thoracic mobility, ramp sets to the first
work load.

## 4. Conditioning by phase (Judgement, built on §2 decisions 3–5)
| Weeks | Friday PM sprint session (bike, 5-min easy warm-up first) | Easy aerobic |
|---|---|---|
| 1 | Baseline: a repeatable 12-min bike or row distance test, record it | Wed + weekend |
| 2–4 | 6–8 × 8–10 s all-out, 90 s easy between (~12 min) | Wed + weekend |
| 5–8 | 4–6 × 8 s all-out, 90 s easy | Wed + weekend |
| 9 | None | Wed only |
| 10 | Repeat the week-1 distance test | Wed |
| 11–12 | Rebuild to 6–8 × 8–10 s; optional 10–12 min low-skill mixed-modal on bike/row/ski | Wed + weekend |

**Placement is chosen from the client's answers** (options A–D, ordered rules in `references/program-library.md` §2b; `--placement auto` in the generator). The text below describes option A and its fallbacks.

If the sprint session cannot be ≥ 3 h from lifting, do it **after** lifting and accept the same-session cost
(Petré 2021), or move it to a non-lifting day and count it as a fifth training day. Do not do intervals **before**
lifting (Vechin 2021).
The sprint doses are **Judgement** anchored on the ≤ 10 s subgroup finding; no trial specifies this exact dose.

## 5. Weeks 10–12
- **Week 10 — test / reassess (reduced load):** re-run the gate (G1–G7), record 1RMs (or estimated), repeat the
  conditioning test, review the log, decide next cycle's wave lifts. Lifting: two light technique sessions
  (~60–70%, 3 × 3–5 per lift), no maximal work.
- **Weeks 11–12 — rebuild (RPE-based):** choose two of the wave lifts, run 3–4 × 5–8 @ RPE 7–8 (2–3 RIR), add
  hypertrophy accessories at 2–3 × 8–15 near failure (Powerbuilding-style higher-rep work; effort near failure only
  on accessories), rotate accessory variations, keep the priority lifts unchanged. Conditioning as §4.

## 6. Progression, fatigue and monitoring
- **Hold or drop ~5%** if the progression-day load hits RPE ≥ 9 twice running. **Nudge the working 1RM up** if an
  anchor day sits ≤ RPE 6 (source: `russian-strength-program.md` §4; the RPE rules there are general knowledge).
- **Auto-deload trigger:** failed 2-for-2, or RPE drifting up on the anchor day → anchor-only week or −10% loads.
  Remove the sprint session first if freshness slips for ~1 week.
- **Log every session:** loads, reps, RPE, sleep hours, session RPE; review weekly (decision 10).
- **Deficit running:** apply `russian-strength-program.md` §5 (maintenance calories in weeks 6–9).

## 7. What is source, what is judgement
- **Source:** the V5 wave, anchor structure, A/B split, gate, accessories' rep range, ISA Table 9-12 rest ranges.
- **Judgement:** the 12-week frame, week 10, sprint doses, primer dose, rest for 80% sets, carries, accessory
  rotation, weeks 11–12.
- **Not covered by any research checked:** carries, the exact sprint dose, the week-10 design, the 3-hour separation as
  a rule (a subgroup finding only).

## 8. Limits
- Abstracts of the papers marked **abstract read** were retrieved from Europe PMC; the full papers were not opened,
  and search-summary items were not verified beyond that.
- Most concurrent-training trials use healthy, mostly non-elite adults; the evidence does not cover highly
  strength-trained lifters, and no study tested this exact program.
- No client has run this. It should be adjusted after the first block from the log, not treated as optimal.

## 9. Fit to the trained-population dose-response data
Weekly heavy sets per wave lift (anchor 6 + progression sets): wk 1–4 = 12, wk 5 = 11, wk 6 = 10, wk 7 = 9, wk 8 = 8, wk 9 = 7,
each lift 2×/week at 80% then 85–105%. Against the trained-lifter data in `references/trained-population-evidence.md`:
- **Frequency and intensity match:** 2 d/wk and ~80% (Rhea 2003, trained), ≥ 85% in weeks 5–9 (Peterson 2004, athletes).
- **Volume is above the meta-analytic means** (4 sets, Rhea; 8 sets, Peterson). Those are effect-size peaks, not caps, and
  Ralston 2017 found higher weekly sets gave slightly more strength (ES 0.18), so this is defensible — but it is a recovery
  cost, hence the RPE triggers in §6 and the rule to drop the sprint session first.
- **Size goals** need 12–20 weekly sets per muscle from accessories plus the wave (Baz-Valle 2022, young trained men).
- **Not covered by any study:** the combination itself, and highly strength-trained lifters.
