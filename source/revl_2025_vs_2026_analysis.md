# REVL 2025 vs 2026 — programming comparison, differences and gaps

**Sources (all local, all git-ignored except this file):**

| Cohort | Blocks | Sessions | Raw data | Tables |
|---|---|---|---|---|
| **2025** | Block 3 2025, Block 4 2025 | 260 (130 + 130) | `revl_raw_data_2025.md` | `revl_programming_analysis_2025.md` |
| **2026** | Blocks 1, 2, 3 | 363 (131 + 133 + 99) | `revl_raw_data.md` | `revl_programming_analysis.md` |

Both cohorts were passed through the same two-engine OCR and the same keyword-presence
analyzer (`source/analyze_revl.py`), so the tables below are directly comparable.
2026's Block 3 lacks its Rebuild phase (never published) — that only affects Block-3
Rebuild counts, not the year-level comparison.

**Evidence labelling:** **[Observed]** read off specific graphics · **[Pattern]** backed
by the frequency counts · **[Inference]** a reading of intent, not stated by REVL.
**Every specific load, %, rep, tempo or cap is approximate OCR** — never quote as fact.

---

## 1. What did NOT change (the house model) **[Pattern]**

These are identical across all five captured blocks, so the skill's existing
`revl-class-integration.md` rules remain valid for a 2025 client:

1. **13-week block**: Volume 3 → Build 3 → Deload 1 → Peak 3 → Rebuild 3, 10 graphics/week.
2. **Weekly skeleton**: Perform+Move on Mon/Wed/Fri, Sweat Tue/Thu (Sprint ↔ Engine
   alternating), Sweat Team Sat, Complete Sun. Verified in the 2025 file structure.
3. **Testing weeks are formal**: Peak Wk 2 = strength baselines (`30:00 Cap`, build to
   1RM deadlift + push press/jerk, `7-5-3-3-3 (Build to 3RM)` variants); Peak Wk 3 =
   Sweat baselines. REVL's own TOC labels both. **[Observed]**
4. **100% of sessions are time-capped** in both years (AMRAP/for-time = 100% of all 623
   sessions). No untimed, self-paced or easy-aerobic work exists.
5. **Load-led periodisation over a near-constant movement menu** — %-1RM tokens ramp
   ~45–60% → 60–90% → 40–50% (deload) → 90–100% → 40–60% in both years.
6. **Deload is a strength-only deload** in both years: %1RM tokens drop to 40–50% and RIR
   disappears, but EMOM density stays at 70–90% and Sunday Complete remains a large
   partner session.
7. **Team-format rep totals are shared** (studio-confirmed for 2026; the same poster
   conventions — In Pairs / YGIG / Teams of N — are used throughout 2025).

---

## 2. What changed 2025 → 2026 **[Observed unless marked]**

### 2a. The Move track was rebuilt: upper/lower split → total-body every day

The largest structural change of the year. In 2025 the Move track is
**Mon Total / Wed Upper / Fri Lower**; in 2026 it is **Move Total on all three strength
days** (Mon deadlift-led, Wed bench-led, Fri squat-led).

Consequences, measured:

| Metric (share of sessions) | 2025 (n=260) | 2026 (n=363) | Read |
|---|--:|--:|---|
| Wednesday hinge exposure | 52% | 99% | 2026 Wed = Perform Lower **+ Move Total (hinge/bench-led)** → lower body loaded twice every Wednesday |
| Sunday hinge exposure | 69% | 89% | same driver (2026 Complete carries more barbell) |
| Move Upper-type rotation exposure | 81% of Move Upper | (no Move Upper) | 2026 members lost the dedicated upper + anti-rotation session |

**[Inference]** A Move-track member in 2026 trains the lower body on every strength day
and the upper body mostly as accessories inside total-body sessions; in 2025 they got a
true upper day. The 2026 change raises per-member lower-body frequency and cuts
upper-body-focused volume.

### 2b. Rotation / anti-rotation halved; carries stay rare

| Pattern | 2025 | 2026 | Δ |
|---|--:|--:|--:|
| **Rotation / anti-rotation** | **33%** | **15%** | **−18 pts** |
| Carry / loaded hold | 8% | 11% | +3 pts |
| Horizontal pull | 28% | 39% | +11 pts |
| Vertical pull | 38% | 43% | +5 pts |
| Horizontal push | 55% | 53% | −2 pts |
| Vertical push | 42% | 50% | +8 pts |

**[Pattern]** The 2025 rotation exposure is concentrated in Move Upper (81%) and Move
Lower (85%) plus Complete (38%); 2026 removed those two sessions' dedicated rotation
blocks. **[Inference]** The 2026 programme trades anti-rotation work for more barbell
push/pull volume — the rotation gap in 2026 is a programming *choice*, not an accident,
and it re-widened the hole the skill already flags.

### 2c. Lower-body volume climbed in 2026

| Pattern | 2025 | 2026 |
|---|--:|--:|
| Squat (bilateral) | 66% | 73% |
| Hinge (bilateral) | 63% | 74% |
| Unilateral lower | 53% | 64% |

Combined with §2a, **2026 loads the lower body harder and more often than 2025**.
**[Inference]** For a REVL member doing PT, added lower-body work is even more expensive
against a 2026 block than a 2025 one.

### 2d. Autoregulation style changed

| Quality (share of phase sessions) | 2025 Volume/Build | 2026 Volume/Build | 2025 Rebuild | 2026 Rebuild |
|---|--:|--:|--:|--:|
| RIR prescribed | 30% / 30% | 18% / 25% | **0%** | 17% |
| RPE prescribed | 28% / 32% | 22% / 19% | **43%** | 17% |
| %1RM prescribed | 28% / 30% | 29% / 29% | **22%** | **12%** |
| Tempo / eccentric cue | 45% / 37% | 55% / 27% | 32% | 50% |

**[Pattern]** 2025 confines RIR to the accumulation phases and hands Rebuild to RPE with
lingering %1RM tokens (40–60%); 2026 keeps RIR alive year-round and nearly abandons %1RM
in Rebuild. **[Inference]** 2026's Rebuild is deliberately more autoregulated/less
prescribed — the PT "fresh start" window in Rebuild is softer-coded in 2026.

### 2e. Small shifts, same shape

- **Olympic/ballistic** 63% (2025) vs 56% (2026) — Sweat Sprint/Engine carry 84–88% in
  2025; the conditioning days got slightly less ballistic in 2026.
- **Core/trunk** 62% vs 55%; **burpee/metcon** 32% vs 30% — noise-level.
- **Density (EMOM)**: Deload 70% (2025) vs 90% (2026) — 2026's deload is *more* density
  formats; partner/team 75% vs 87%. Same conclusion (strength-only deload), starker data.
- **Peak wave tops**: 2025 tokens include `60-70-80-90-95-100` and `60-70-80-90-100`
  (goal-1RM builds); 2026 image-checked builds run to 100%+ of *goal* 1RM in Block 3 and
  token waves to `95-95`/`90-95`. Effectively the same maximal-stakes week.
- **Block 3 2025 published its Deload as seven day-pages** (`3.1 Monday` … `3.7 Sunday`),
  and Block 4 2025 named its baseline sessions inside ordinary titles while Block 3 2025
  added `baseline` to file names — portal housekeeping differences only.

---

## 3. Gaps — what neither year programmes **[Pattern]**

Ranked by how much a 1-on-1 PT can add on top of either year's block:

| # | Gap | 2025 | 2026 | Why it matters **[Course/research]** |
|---|---|--:|--:|---|
| 1 | **True Zone 1–2 easy aerobic work** | 0% | 0% | Every session is capped and competitive. The one cardio quality REVL never supplies — and the IFT cardio model's Base phase *(Wk02 Ch2; Wk05 Ch8)*. |
| 2 | **Carries / loaded holds** | 8% | 11% | Cheapest trainable pattern with the lowest interference risk; grip/trunk/hinge-stability transfer with minimal next-day soreness. |
| 3 | **Rotation / anti-rotation (2026 only)** | 33% | 15% | 2025 covered it; 2026 does not. Trunk stability under load protects the axial-loading the programme prescribes. |
| 4 | **Unilateral *stability* (vs unilateral load)** | both | both | Unilateral work is 53–64% but almost always loaded and timed; slow, unsupported single-leg control is not. |
| 5 | **Untimed technique / movement-quality work** | 0% | 0% | No session allows technique practice at sub-maximal load without a clock. |
| 6 | **Dedicated mobility / tissue work** | warm-ups only | warm-ups only | 4:00 caps cannot deliver ROM change for a restricted joint. |
| 7 | **Screening, assessment, individual regression** | absent | absent | Group format cannot individualise; the CPT owns screening *(Wk04 Ch5)*, assessment *(Ch 7, 10)* and population overrides *(Ch 12–15)*. |
| 8 | **Max-effort upper push risk management** | — | — | Both years put true 1RM overhead builds (push press/jerk) in a 30:00 partner-capped window — the highest-skill maximal lift under time pressure. |

**Pattern-level exposure in both years is otherwise broad** — squat/hinge/push/pull/erg
all land on ≥38% of sessions in every phase, so a complementary PT session should target
the table above, not "more fitness".

---

## 4. Practical read for the jon-fitness skill

1. **The `revl-class-integration.md` stimulus model survives the new data.** Every
   structural rule (phase headroom, Wednesday/Monday caution, deload = assessment window,
   protect Peak Wk 2–3, team totals shared, no phase rests a pattern) reproduces on 2025.
2. **Two numbers in the reference are 2026-specific and now have year ranges:**
   hinge 63–74%, squat 66–73% of sessions (not "23–32% BB squat / 44–55% BB hinge"
   phrased as constants); rotation 15–33% depending on year.
3. **Wednesday caution should be conditional on the track.** For a 2025-style block,
   Wednesday is *less* lower-loaded than 2026 (Move Upper); for 2026 it is the heaviest
   mixed day. Ask which Move session the client actually did.
4. **If the client is on the 2025 Move track**, upper-body pull/rotation is already
   served — the PT's marginal value shifts toward carries, aerobic base and lower-limb
   stability. If on the **2026 Move track**, rotation and horizontal pull return to the
   top of the gap list.

*Analysis produced 2026-09-16. Regenerate tables with
`python source/analyze_revl.py --blocks 4 5` / `--blocks 1 2 3`.*
