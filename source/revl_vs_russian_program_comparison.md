# REVL vs the Russian Strength Program — design strengths, weaknesses, and optimization read

A sports-data-scientist comparison of the two training systems the jon-fitness skill has to
reconcile: **REVL** (the client's existing group class, both captured years) and the
**Russian Strength Program** (the skill's own V5/Classic/Masters archetype). Grounded in (a)
the 623-session REVL dataset already analysed (`revl_programming_analysis.md`,
`revl_programming_analysis_2025.md`, `revl_2025_vs_2026_analysis.md`) and (b) established
exercise-science literature, cited by author/year and clearly separated from the ISA course's
own verified page citations.

**Evidence labelling**
- **[Observed]/[Pattern]** — as in the other analysis files, backed by the REVL counts.
- **[Course]** — an ISA CPT citation already verified against the course PDFs elsewhere in the
  skill *(WkNN Ch## pN)*.
- **[Literature]** — a general exercise-science finding, cited by author/year. These are
  well-established results recalled from training knowledge and spot-checked by search this
  session; treat effect sizes as indicative, not exact, and don't quote them to a client as
  precise numbers.
- **[Inference]** — a reasoned synthesis, not directly stated by either source.

---

## 1. What each system is actually optimizing for

| | REVL | Russian Strength Program |
|---|---|---|
| **Unit of design** | A group class, 8–30+ members, one poster per session | A single client's wave, individualised load |
| **Periodization model** | Fixed 13-week block periodization (Volume→Build→Deload→Peak→Rebuild), same shape both captured years | Linear periodization within each variant (V5/Classic/Masters), volume-down/intensity-up |
| **Load prescription** | Mixed: %1RM on Perform, RIR/RPE on Move — **[Observed]** both formats run concurrently by track | %1RM primary, RPE/RIR as a modernisation layer (§4) |
| **Primary outcome** | Adherence + general work capacity + a shared maximal-strength test fortnight | A specific 1RM/3RM PB on named lifts |
| **Individualization** | None at the prescription level — scaling is member-selected (Perform/Move, load) | Full — gated by eligibility (§2), variant choice, retest history |

---

## 2. REVL — strengths

1. **Genuine block periodization with built-in testing weeks.** Peak Wk 2 (1RM/3RM) and Peak
   Wk 3 (conditioning baseline) are formal, coached, repeatable retests every 13 weeks —
   **[Observed, both years]**. Most commercial group programming has no retest structure at
   all; REVL's does, and it's a legitimate substitute for a PT-administered 1RM test (now
   wired into `russian-strength-program.md` §7).
2. **Adherence mechanics a 1-on-1 program structurally cannot match.** Team/partner formats
   (Sat/Sun) carry shared-rep totals with built-in work:rest ratios — **[Pattern]** 75–87%
   partner/team format across phases. Group exercise is consistently associated with better
   adherence than individual training in the literature — social accountability and fixed
   scheduling reduce the drop-off individualised programs suffer from **[Literature — group
   vs. individual exercise adherence is a long-standing finding, e.g. reviewed by Burke,
   Carron & Shapcott, *Sport & Exercise Psychology Review*, 2008]**. This is REVL's real edge:
   a Russian block delivers a better strength outcome on paper but only if the client
   actually completes it.
3. **Autoregulated volume on the Move track outperforms fixed %1RM for some outcomes.**
   RPE/RIR-based prescription is now shown to be equal or superior to pure %1RM prescription
   for strength and hypertrophy in recent meta-analytic work, and the newest network
   meta-analysis (2025) ranks autoregulated methods (APRE, RPE) above %1RM-based training for
   maximal-strength outcomes **[Literature — autoregulated resistance training network
   meta-analysis, *Journal of Sport and Health Science*, 2025]**. REVL's Move track already
   runs this correctly; the skill doesn't need to "fix" it.
4. **Time efficiency and format variety cover the ACE cardio and resistance FITT-VP floor
   for a time-constrained general-population client** in one session — hard to replicate in
   a 1-on-1 model without a much longer session.

## 3. REVL — weaknesses

1. **No true individualization or screening.** REVL attendance is not medical clearance
   **[Course, Wk04 Ch5]** and the group format cannot regress a single member's technique
   breakdown, a restricted joint, or a special-population override (Ch 12–15) — this is
   categorically the PT's job, not REVL's, and the gap is structural, not a bug.
2. **Zero true Zone 1–2 aerobic exposure, both years — 0% of 623 sessions.** Every session is
   capped and competitive **[Observed]**. Polarized-training research on trained endurance
   populations finds low-intensity volume (≈80% of training time in elite models) drives the
   aerobic-base adaptations (mitochondrial density, fat oxidation) that high-intensity/capped
   work does not reach **[Literature — Seiler, polarized training model, *Int J Sports Physiol
   Perform*, 2010; supporting work through 2024]**. REVL cannot supply this by design — every
   session is intensity-anchored.
3. **Rotation/anti-rotation is a real, measured, and *year-dependent* gap.** 33% (2025) → 15%
   (2026) — REVL removed its own best-covered pattern when it rebuilt the Move track
   **[Pattern]**. This is the clearest evidence in the whole dataset that REVL's programming
   choices, not just genre limits, can create or close a gap — worth flagging because it means
   the skill's gap list has to be re-verified every time REVL republishes a block, not treated
   as permanent.
4. **Carries are under-trained in both years (8–11%)** despite being one of the
   lowest-interference, highest-transfer patterns available — cheap to add, structurally
   absent from group programming that optimizes for spectacle and shared equipment.
5. **Concurrent-strength-and-conditioning design has a real physiological cost the skill
   should stop treating as a footnote.** Every REVL session mixes barbell strength work with
   metabolic/conditioning work in the same 45–60 min window, several days a week. The
   canonical concurrent-training meta-analysis found strength-only training produced larger
   strength, hypertrophy, and power gains than concurrent strength+endurance training, with
   the interference concentrated when the endurance modality is running rather than cycling
   and scales with endurance frequency/duration **[Literature — Wilson et al., concurrent
   training meta-analysis, *J Strength Cond Res* 26(8):2293–2307, 2012]**. REVL's format
   (erg/run conditioning stacked directly against barbell strength, 5–6×/week) is close to
   the worst-case interference pattern in that literature. **[Inference]** This is likely
   *why* REVL's own strength numbers (§3 macrocycle) top out lower than what a dedicated
   strength block reaches, and it strengthens the "replace, don't stack" rule in
   `revl-class-integration.md` §10 — adding a Russian wave on top of REVL doesn't just
   duplicate volume, it adds a second interference source.
6. **Maximal Olympic-lift-pattern testing under a hard time cap (Peak Wk 2: 30:00 cap,
   1RM deadlift + 1RM push press/jerk) concentrates technical-failure and injury risk in a
   single high-stakes group window** — no individualized readiness check before a member
   attempts a 1RM under time pressure. The skill already flags this as the highest-stakes
   week (§3); the risk is structural, not avoidable by REVL's format.

## 4. Russian Strength Program — strengths

1. **A validated periodization model, correctly applied to trained lifters.** Linear
   periodization's strength benefit over non-periodized training is well established, and
   for **trained individuals specifically**, undulating/daily-varied loading (which the
   program's autoregulation layer, §4, effectively approximates) outperforms strict linear
   progression for 1RM gains — though the advantage narrows or disappears for hypertrophy
   and for untrained lifters **[Literature — meta-analyses comparing linear vs. undulating
   periodization, e.g. Rhea et al. 2002; more recent synthesis in *Frontiers in Public
   Health*, 2026, finding undulating > linear for trained 1RM outcomes specifically]**. The
   program's built-in gate (§2: experience, technique competence) correctly restricts the
   full wave to the population where this advantage actually applies — the scaled-entry
   path (§6) is the right response for everyone else, not a compromise.
2. **A real, individualized 1RM/3RM retest protocol** (§7) with course-verified pre-test
   safety criteria *(Wk04 Ch8 pp70–71; Wk06 Ch10 pp69–75)* — spotting, readiness screening,
   stop-test criteria — none of which a group class can enforce per member.
3. **Explicit interference management via the fat-loss (§5) and REVL-integration (§10)
   layers.** The reduce/replace framework in §10c/d is a direct, correctly-targeted response
   to the concurrent-training literature above — it doesn't just avoid duplicated *volume*,
   it avoids duplicated *interference sources* (two near-maximal neural exposures, two
   metabolic deficits) which is the actual mechanism in the Wilson et al. findings.
4. **Scaled entry (§6) and Masters variant (§3c)** give the program population coverage REVL
   structurally lacks — genuine individualization for reduced-recovery-capacity or returning
   lifters, which no fixed-block group class can offer.

## 5. Russian Strength Program — weaknesses

1. **No adherence mechanics of its own.** It depends entirely on 1-on-1 coaching
   relationship quality and the client's individual motivation/scheduling — it has none of
   REVL's structural adherence advantages (§2.2 above). **[Inference]** This is likely why
   the skill's own decision tree (§10) so strongly favors "replace REVL's strength days"
   over "run alongside REVL" — a fully separate program stacked on top of an already-full
   week is an adherence risk even before considering physiological interference.
2. **Zero built-in conditioning or aerobic-base component.** The program is a pure strength
   archetype (§1) — it doesn't address the Zone 1–2 gap either. A client running Russian-only,
   off REVL entirely, has the *same* aerobic-base gap REVL clients have, just for a different
   reason (program scope, not format). The skill's templates (§13 Template F) currently frame
   Zone 1–2 as a REVL-complement fix; it should be framed as a **general programming
   gap the archetype itself doesn't close**, regardless of whether REVL is present.
3. **1RM/3RM testing carries its own risk that the program doesn't route through the same
   coached, high-frequency environment REVL's Peak Wk 2 provides.** A single 1-on-1 test
   session has less redundancy (spotting, pacing, peer calibration) than a coached group
   testing week with a fixed 30:00 protocol repeated every block — this is an argument *for*
   §7's new REVL cross-reference (use REVL's coached maxes when available) rather than a
   flaw to fix in isolation.
4. **The V5/Classic frequency requirements (4-day / 3-day) are documented in the skill as
   "rarely fit alongside full REVL participation"** (§10c) — correct, but it means two of the
   program's three variants are effectively unavailable to the largest realistic client
   population (REVL members), leaving Masters as the default by elimination rather than by
   design intent.

## 6. Where the two systems' gaps overlap (compounding risk)

Both systems independently fail to deliver:
- **True Zone 1–2 aerobic work** — REVL by format (everything capped), Russian by scope
  (pure strength archetype). A client who does *either* program, or both, still has no
  aerobic base unless the PT adds it deliberately.
- **Untimed technique/movement-quality work at sub-maximal load** — REVL by format, Russian
  by intent (it's a strength-peaking program, not a motor-learning program).
- **Screening/individual regression** — REVL structurally, Russian only partially (the
  eligibility gate screens *for the archetype*, not general MSK/special-population status,
  which still routes to Ch 12–15).

**[Inference]** These are not REVL-specific or Russian-specific gaps — they are **systemic
gaps of the PT-adjacent-to-programmed-training model itself**, and the highest-value thing a
1-on-1 session can do regardless of which program the client is enrolled in is exactly what
`revl-class-integration.md` §6a and `russian-strength-program.md` already independently
converge on: carries, Zone 1–2, technique, mobility, and individualized assessment.

## 7. Concrete optimization actions taken in this pass

Applied directly to the skill (see git diff):
1. `revl-class-integration.md` — 2025 coverage added, hinge/squat exposure numbers now show
   year ranges, rotation reframed as track-conditional (not a flat 15%), Wednesday caution
   made track-conditional, Peak Wk 2 test menu confirmed across both years, a Masters-anchor-
   to-Peak-Wk2 rule added, §6a reordered by how unconditional each gap is, a new conditional
   example template (G) added.
2. `intake-questions.md` — new blocking question (P18) capturing Move-track shape + block
   week for a REVL client.
3. `SKILL.md` — REVL intake flow now logs Move-track shape + week in the plan's evidence
   section so it isn't re-asked every session.
4. `russian-strength-program.md` §7 — cross-referenced REVL's Peak Wk 2 as an accepted
   substitute for a separate 1RM test, closing the loop both files already gestured at
   separately.

## 8. What's still open (not applied this pass — needs a decision, not more analysis)

1. **Eval-harness traps (R5 from the earlier recommendations doc)** — adding "client's
   Wednesday was Move Upper" and "client just finished Peak Wk 2 with a fresh 1RM" as scenario
   traps belongs in `evals/` (scenario generator + grader), not the reference files, and that
   harness has unfinished wiring (`evals/HARNESS_INTEGRATION.md` — `run_cycle.py`/`optimize.py`
   were mid-edit by another session) plus a paused cloud routine. I did not touch `evals/`.
2. **Zone 1–2 reframe (§5.2 above)** — moving Template F from "REVL-complement" framing to
   "closes a gap in both systems" framing is a small wording change I left alone pending your
   call, since it touches how the skill talks about the Russian archetype's own scope, not
   just REVL data.
3. **2026 Block 3 Rebuild** — still unpublished by REVL; your weekly memory reminder to check
   for it stands.
4. **Gold-set human scores** — `scenarios/gold/gold_responses.json` still needs your scoring
   before `grader_validity.py` can run and before any of these reference edits get a
   grader-verified non-regression check, since the optimizer loop is currently manual/paused.

*Analysis produced 2026-09-17. Literature claims spot-checked via web search this session;
treat cited effect sizes as directional, not exact quotes.*
