# jon-fitness skill — improvement recommendations from the 2025 REVL data

**Date:** 2026-09-16 · **Author context:** five REVL blocks now captured and OCR'd —
Blocks 1–3 of 2026 (363 sessions) and Blocks 3–4 of 2025 (260 sessions) = **623 sessions**,
all dual-engine OCR (`source/revl_raw_data.md`, `source/revl_raw_data_2025.md`), all
quantified (`source/revl_programming_analysis.md`, `source/revl_programming_analysis_2025.md`),
compared in `source/revl_2025_vs_2026_analysis.md`.

These are **proposals, not applied edits.** Skill edits should go through the guarded
optimizer loop (dirty-tree refusal, one file per pass, benchmark non-regression gate) or
a deliberate manual pass — see `evals/HARNESS_INTEGRATION.md`.

**Evidence labelling:** [Observed] / [Pattern] / [Course] *(WkNN Ch## pN)* / [Inference]
as used in the skill's references.

---

## R1. Update `revl-class-integration.md` coverage + numbers (highest value)

**What the data shows.** The 2025 blocks confirm every structural rule in the reference
(§3 macrocycle, §4 phase table, §5a weekday matrix, deload = strength-only, Peak Wk 2–3
testing, team totals shared, no phase rests a pattern). But several constants in the
reference are actually **year ranges**, and one structural fact is **track-conditional**:

| Reference claim today | What the 5-block data supports |
|---|---|
| "Blocks 1, 2 and 3 of 2026 — 363 sessions" (coverage header) | "Blocks 1–3 of 2026 and Blocks 3–4 of 2025 — 623 sessions" |
| BB hinge ~51% of all sessions, BB squat 23–32% | Hinge 63–74%, squat 66–73% of sessions **by year** (pattern-level, any implement) |
| Rotation/anti-rotation 15% — systematic gap | **15% (2026) vs 33% (2025)** — the gap is year-specific: 2025's Move track carried rotation on 81–85% of Move Upper/Lower sessions [Observed] |
| Wednesday = "heaviest mixed day" | True for **2026** (hinge 99% of Wednesdays). For **2025** Wednesday hinge = 52% (Move Upper sits there) — conditional on the Move track |
| Move track = "RIR-based, higher reps" | True both years, but 2025 confines RIR to Volume/Build (30%) and hands Rebuild to RPE (43%) — Rebuild reads as softer-coded in 2026 |

**Suggested edits.**
1. Coverage/provenance header: add the two 2025 blocks and the raw/analysis file names.
2. Replace point constants with the observed **ranges** and keep the existing
   "never a fact" caveat.
3. §5a/§6a: make **rotation a conditional gap** ("2026-style blocks: 15% — top gap;
   2025-style: 33% — covered") and keep carries (8–11%) as the unconditional #1.
4. §7 "windows to avoid": make the Wednesday caution **track-conditional** — ask which
   Move session the client did before declaring Wednesday off-limits for lower-body work.
5. Add one sentence to §2: "REVL has shipped at least two Move-track shapes (2025:
   upper/lower split; 2026: total-body). **Ask the client what their Wednesday Move day
   is**, don't assume either."

**Why this matters for scoring.** The grader zeros fabricated or over-confident claims;
per-scenario traps include misreading which session the client did. Track-conditional
rules directly de-risk the "client did REVL yesterday" decision table (§14).

## R2. Add "which year/shape is the block?" to the intake flow

**What the data shows.** REVL rewrites the block every 13 weeks and has already changed
the Move track once within 12 months [Observed]. A client citing "REVL" may be on either
shape plus future variants.

**Suggested edits.**
1. `references/intake-questions.md`: add one staged question — *"Which sessions does your
   gym run on Wednesday — a Move Upper (upper-body) day or a Move Total day? And which
   week of the block are you in?"*
2. `SKILL.md` client-plan conventions: when logging a client's REVL phase, also log the
   **Move-track shape** and week number in the plan's evidence section so later sessions
   inherit it.

## R3. Wire Peak Wk 2 into the Russian retest protocol explicitly

**What the data shows.** Both years' Peak Wk 2 = build-to-1RM deadlift + push press/jerk
(30:00 split) and 3RM variants; 2025 files even name them `baseline` [Observed, both
engines agree]. The reference already says "capture the tested maxes — they satisfy the
current-1RM requirement (G4/§7)".

**Suggested edits (small, in `revl-class-integration.md` §3 and
`russian-strength-program.md` §7 cross-ref).**
1. State the observed test menu as the **expected retest evidence**: deadlift 1RM,
   push press/jerk 1RM, 3RM baselines, Sweat Engine/Sprint baselines the following week.
2. Rule: a **Masters 2-day wave started in Rebuild** should be anchored to the Peak Wk 2
   maxes captured 3–5 weeks earlier — no re-testing, no stacking *(respects the
   never-stack-two-peaks rule and the §2 G6 combined-recovery gate)*.
3. Keep the hard line: in Build/Peak the protocol **replaces** a REVL strength day
   (§10d) — the 2025 data strengthens this, since 2025 Peak tokens reach 95–100% of goal
   1RM, i.e. REVL is already running a full peak itself.

## R4. Refresh the complementary-session templates (§13) against the measured gaps

**What the data shows (unconditional gaps, both years):** carries 8–11%, easy Zone 1–2
aerobic 0%, untimed technique work 0%, unilateral *stability* rare, dedicated mobility
absent. **Conditional gap:** rotation 15% + horizontal pull 28% *only if* the client is on
a 2026-style track (2025 covers both).

**Suggested edits.**
1. Re-order §6a complementary list: carries → easy aerobic → (conditional) rotation +
   horizontal pull → unilateral stability → untimed technique → assessment.
2. Add one template: *"2026-Move-track client, Volume phase, Friday"* — Pallof/banded
   anti-rotation 3×8/side, suitcase carry 4×30 m, controlled horizontal row 3×10, single-
   leg RDL @ RIR 3 — fills the three measured gaps, zero axial load, no interference with
   Friday Perform Upper.
3. Keep template F (Zone 1–2) unchanged — the data reconfirms it.

**Course anchor.** Volume budget first: REVL + PT counts together against Table 9-12 /
11-10 ceilings *(Wk07 Ch11 p16, p29–31)*; the gaps above are all low-neural, low-axial
additions, which is why they survive that budget [Inference].

## R5. Eval-side suggestions (for the optimizer, not the reference)

1. **Traps to add** (scenario-level): "client's Wednesday was Move Upper (2025-style)" —
   a naive answer treats Wednesday as lower-body-loaded and stacks wrong; "client finished
   Peak Wk 2 with a 1RM deadlift" — correct action is log-and-use for a Rebuild-start
   Russian block, not immediate heavy testing.
2. **Expected-priorities to widen:** "carry" and "zone-2 aerobic" as acceptable top
   priorities on top of rotation (already present), so a correct 2025-track answer isn't
   penalised for deprioritising rotation.
3. **Guardrail reminder:** do not weaken the automatic-0 fabrication rules when adding
   2025 numbers — everything quoted from OCR stays "roughly/approximate".

## R6. Data hygiene / provenance tasks

1. Regenerate the 2026 Block 3 capture if REVL publishes its Rebuild phase — the only
   known coverage hole (2025 blocks are complete; 130/130 each).
2. Keep result-document commits (raw data, analysis) separate from skill-edit commits,
   per repo convention.
3. If a third year-shape appears, re-run `extract_revl.py` → `analyze_revl.py` before
   touching the reference again — the analysis rests on counts, not impressions.

---

**Priority order:** R1 → R2 → R4 → R3 → R5 → R6. R1/R2/R4 are documentation edits with
direct grader-visible effect; R3 closes the loop between the Russian reference and the
REVL testing calendar; R5 belongs in the eval harness; R6 is standing maintenance.

**Scope note.** All recommendations stay inside the skill's existing scope-of-practice:
screening and medical clearance per ACSM *(Wk04 Ch5)*, referral out for injury/rehab and
dietetics *(Wk01 Ch1 p7–8)*, no invented numbers — 2025 additions are labelled as OCR-
derived approximations like their 2026 counterparts.
