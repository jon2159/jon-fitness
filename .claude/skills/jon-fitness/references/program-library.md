# Program library — goal-based tracks on one shared engine

A Chalk-style **library of tracks chosen by goal, equipment and experience**, built only from this skill's own
foundations (ISA CPT, Russian Strength Program, REVL logic) and evidence graded in
`chalk-design-reference.md` §6. It is a routing and design layer: each track points to the reference or script
that holds its numbers. **Nothing here copies Chalk content.**

**What "better" means here — and what it doesn't.** Designed to be stronger on: screening and eligibility
(G1–G7 before any heavy track), provenance labels on every claim, conditioning placed by interference evidence,
autoregulation with explicit triggers, four *total* days honoured, and honesty about unknowns. **Not established:**
better outcomes than Chalk or any program — no head-to-head data exists. Chalk is ahead on app delivery, exercise
videos, community and scale, which a skill cannot replicate. Judge this library by the client's logged results.

## 1. Choose the track (ask intake P19 first: strength vs conditioning experience, total training days)

| Client situation | Track | Where the numbers live |
|---|---|---|
| Cleared, experienced, wants maximal strength, 4 days, no classes | **T1 Max Strength (V5, 9 wk)** | `russian-strength-program.md` §3a; `scripts/russian_block.py --variant v5` |
| Same, plus wants conditioning / work capacity kept, 4 days | **T2 Strength-Hybrid (12 wk)** | `docs/twelve-week-four-day-program.md`; `scripts/hybrid_block.py` |
| Cleared, but low recovery or only 2 days | **T3 Masters (8 wk, 2-day)** | reference §3c; `--variant masters` |
| One focus lift, meet-style peak, 3 days | **T4 Classic (6 wk)** | reference §3b; `--variant classic` |
| Wants size **and** strength, 4 days | **T5 Strength-Size (upper/lower)** | §3 below (framework; numbers from ISA Table 9-12) |
| Novice, returning, or fails G2–G4 | **T6 Foundations (movement → load)** | reference §6 scaled entry; ISA Table 11-10 |
| Already trains at REVL | **T7 REVL complement** | `revl-class-integration.md` — do not stack a full track |
| Wants fat loss | **Overlay on T1–T5, not a track** | reference §5 (deficit periodisation) |

Route by these facts, never by preference alone: any unmet gate item sends the client to T6. A 4-day request means
**four total planned days** unless the client says four *additional* PT days.

## 2. The shared engine (identical across tracks, so they behave as one system)

| Element | Rule | Evidence / source |
|---|---|---|
| Priority quality | One primary, at most one secondary; the secondary gets the minimum effective dose | `coaching-decision-framework.md` §3 |
| Frequency | Each main lift 2×/wk unless the track says otherwise; chosen for feasibility, never sold as a growth multiplier | Schoenfeld 2019; Grgic/Ralston 2018; Ramos-Campo 2024 (abstract read) |
| Periodisation | A planned wave with a fixed anchor and a progressing day (weekly undulation inside a linear wave) | Moesgaard 2022 (abstract read): periodized > non-periodized; undulating > linear for 1RM, larger in trained lifters (borderline) |
| Conditioning | Separate session from lifting (≥ 3 h) for trained lifters; short bike sprint intervals first choice; never before lifting; bike over running | Petré 2021, Ferraro-Farro 2026, Vechin 2021 (abstracts read); Wilson 2012 (summary) |
| Aerobic base | Easy Zone 1 (below VT1) on off days; dose is judgement | ISA three-zone model (Table 8-11) |
| Power / primer | Low-dose jumps or throws first while fresh; not sold as a power block or potentiation | de Villarreal 2009; Seitz & Haff 2016 (summaries) |
| Accessories | 2–3 × 8–12 near failure, rotated between phases; priority lifts stay fixed | Schoenfeld 2017; Lopez 2021; Baz-Valle 2019 (summaries) |
| Autoregulation | RPE ≥ 9 twice → hold or −5%; anchor ≤ RPE 6 → raise the working 1RM; failed 2-for-2 or rising anchor RPE → anchor-only week or −10% | `russian-strength-program.md` §4 (general knowledge) |
| Recovery weeks | Test / reassess at the end of a block; use autoregulated reductions rather than a fixed deload | Bell 2023 (consensus); Coleman 2024 (RCT) — summaries |
| Logging | Every session: loads, reps, RPE, sleep, session RPE; weekly review | Michie 2009 (indirect evidence) |
| Testing | 1RM only if G4 passes, else estimated 1RM (Table 10-25); one repeatable conditioning test at start and end | Wk06 Ch10 p69–75 |
| Substitutions | Swap within a movement pattern only; keep the pattern, load basis and RPE target; record it in the plan | Movement patterns, Wk06 Ch10 |

## 3. T5 Strength-Size — framework (upper/lower, 4 days)
Chalk's own 4-day plan is upper/lower; split choice is a scheduling decision when volume is equal (Ramos-Campo 2024).
- **Days:** Lower A / Upper A / Lower B / Upper B, ≥ 48 h between the same muscle groups.
- **Heavy anchor lift first each day** at 3–5 × 4–6 (80–85% 1RM, RPE 8), then accessories at 3–6 sets total per muscle
  per session in the 8–15 range near failure (ISA Table 9-12 hypertrophy row: 3–6 sets, 6–12 reps, 67–85%;
  strength row ≥ 85%, ≤ 6 reps, 2–5 min rest).
- **Progression:** double progression, 2-for-2 then ~5% (Wk07 Ch11 p7, p20). No wave is prescribed here — the
  Russian archetype is for maximal strength; a size goal earns volume, not a peak.
- **Conditioning:** as §2, kept short so the volume budget goes to lifting.
- **Unknown:** the weekly set target per muscle for this client. Set it from intake and adjust from the log; no study
  gives one number (Pelland 2026, via `research_notes/`).

## 4. Guardrails
- Screening, clearance and scope are unchanged (ISA Wk01 Ch1; Wk04 Ch5). Fat-loss diet detail goes to a registered dietitian.
- Every plan records: client fact → source principle → gap → evidence → decision → progression → schedule row.
- Label judgement as judgement. Do not fill any Chalk detail (rest, RPE, progression, volumes) that Chalk did not publish.
- Review outcomes after each block against the log (1RM change, conditioning test, sessions completed, RPE drift)
  and change the plan from the results, not from the design.
