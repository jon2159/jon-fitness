# Program research review and skill-improvement roadmap

_Written 2026-10-09, updated 2026-10-14. Scope: the programs the `jon-fitness` skill references (ACE/ISA CPT, Russian Strength Program, REVL, Chalk, Daily Pump), checked against what building a real powerbuilding block exposed (first as a 3-day full-body plan, then rebuilt on 2026-10-14 as a 4-day upper/lower plan), plus a bounded external literature check._

**Evidence rules used.** Search summaries were read, **full papers were not opened**. Every external finding below is "what a summary reported" and is labelled; nothing here upgrades a skill rule to "proven". Items marked *judgement* have no outcome data behind them. This file contains no client health data.

---

## 1. What each program contributes, and how well it's grounded

| Source | What the skill uses it for | Grounding | Main limit |
|---|---|---|---|
| **ACE / ISA CPT notes** | Screening, FITT-VP tables, progression rules, scope of practice | Course text, citable by page | A general-population framework: no wave loading, no powerbuilding, thin for trained lifters |
| **Russian Strength Program (V5 / Classic / Masters)** | Maximal-strength wave, eligibility gate, retest | A project record of the V5 template; CPT mapping of the loads | V5 is 4-day, half-body per day, assumes a true 1RM; **no outcome data** on this exact wave; the 3-day and upper/lower-with-accessories forms are coach judgement |
| **REVL** | Class-complement rules for clients who attend | 653 OCR'd posters across 5 blocks; counts are lower bounds | Describes the programme as written, not any member's week; irrelevant to non-REVL clients |
| **Chalk** | Session ordering and delivery ideas only | Public pages, retrieved 2026-09-20 | Publishes no volumes, progression or recovery rules; marketing claims excluded |
| **Daily Pump** | Not yet a source | ~4 weeks captured, one 4-day split | Too little data; the earlier agreement was to wait for several weeks and a split change |

**Take-away:** the skill is strong on *safety, scope and provenance* and on *REVL-complement logic*. It is weakest where a trained lifter wants a **hypertrophy-forward programme with a strength wave and no class constraint** — which is exactly what the latest client asked for.

## 2. External check (2026-10-09, summaries only)

| Question | What the search summaries reported | Effect on the skill |
|---|---|---|
| Weekly volume for hypertrophy in trained lifters | Graded dose-response; 12–20 weekly sets per muscle suggested for young trained men (systematic review, [PubMed 35291645](https://pubmed.ncbi.nlm.nih.gov/35291645/)); a 2025 analysis reported gains for size and strength rise with volume but with diminishing returns, **more pronounced for strength** (source not opened) | Confirms the existing 12–20 guidance. **Working standard (confirmed by Jon, 2026-10-14): 9–12 sets/muscle/week is the floor; experienced lifters are programmed at 12–20, in every week of a block including peak weeks.** New nuance worth encoding: extra volume pays more for size than for strength |
| Full-body vs split | Volume-equated frequency studies show no meaningful difference ([sci-sport summary](https://sci-sport.com/en/impact-of-training-frequency-on-muscle-strength-and-hypertrophy/)); a split-vs-full-body review of 14 studies found no between-routine difference; a 2026 meta-regression (67 studies) found volume raised size and strength with high certainty and frequency had negligible effect on size | Supports full-body as a **scheduling choice**. No evidence it is *better* — the skill must not oversell it |
| Linear vs undulating periodization | Hypertrophy similar (13 studies, [PMC5571788](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5571788/)); one meta-analysis found a small 1RM edge for undulating (ES 0.22, [PubMed 35044672](https://pubmed.ncbi.nlm.nih.gov/35044672/)); most participants **untrained** | The wave's *shape* is weakly supported either way. The V5 design (fixed anchor + progressing day) is a hybrid and defensible, but not evidence-driven |
| Concurrent training | A 2024 meta-analysis of 40 studies reported all modalities inferior to lifting alone for lower-body strength, running HIIT less so, and a **negative relationship between endurance frequency/duration and adaptations** ([PMC10767279](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767279)); cycling HIIT trended worse than running ([Sabag 2018, PubMed 29658408](https://pubmed.ncbi.nlm.nih.gov/29658408/)) | Supports keeping own cardio **easy, short and on separate days**; the *dose* of cardio matters more than its label. Add a dose cap to the rules |

**Nothing found contradicts the skill's current rules.** The check mostly confirms them, and sharpens two: (a) volume buys size more than strength, (b) cardio dose is a lever.

## 3. What building the latest plan exposed (gaps in the skill)

| # | Gap | Where it showed up | Severity | Proposed fix |
|---|---|---|---|---|
| G1 | **No track that combines a strength wave with hypertrophy volume.** Library tracks: T1 V5 (4-day, half-body, wave, little size work), T3 Masters (2-day), T4 Classic (1 lift), T5 Strength-Size (4-day upper/lower, volume, *no wave*) | The first build hand-adapted V5 to 3 full-body days; the 2026-10-14 rebuild combined V5's wave with T5's upper/lower layout by hand | **High** | Add a **T8 "Powerbuilding upper/lower"** to `program-library.md`: V5 wave on the five main lifts, PROG days spread so no session carries more than two PROG lifts, T5-style accessories sized by the set audit (G5), alternating/superset pairs to hold 75–90 min; label it a coach-designed combination. Keep a 3-day full-body variant as a secondary option |
| G2 | **No rule for starting loads from rough numbers.** I used Epley × 0.95 | Plan needed working 1RMs from "roughly 110 × 1–3" | **High** | Add a "working 1RM from rough data" rule: estimate from a rep-max (Table 10-25 method), apply a stated conservative factor, **refresh after week 1** |
| G3 | **Wave % assumes a true 1RM**; weeks 7–8 at 95–100% are not realistic off an estimated one | 3×3 @ 95% sits above a best-ever set of 3 | **High** | Introduce a **training max** (conservative), allow the PROG top weeks to be RPE-capped, and make the week-5 refresh mandatory |
| G4 | **Weighted pull-up as a wave lift with unknown load** | Added kg unknown; the generator needs a number | Medium | Add a bodyweight-relative first-session protocol (find a 3-rep top set) and a placeholder convention |
| G5 | **No per-muscle, per-week set audit.** The first upper/lower draft cut every accessory to 2 sets in weeks 7–9, leaving rear delts, calves and abs at 4–7 sets and hamstrings/side delts at ~8 in those weeks — caught only when the client asked for a triple-check | 12–20 sets/muscle standard | **High** (raised from Medium) | Add a set-audit helper (prime mover = 1 set, helper = ½; counting rule labelled *judgement*) that prints a muscle × week table and flags any week below 12 (experienced) or 9 (floor). Rule: in peak weeks trim only compound accessories; keep isolation work for arms, delts, calves and abs |
| G6 | **No guidance for 1–3 own cardio sessions alongside lifting** beyond sprint-placement rules (§2b) | Client's "flexible 1–3" | Medium | Add an "easy aerobic dose" rule: default 2, keep ≤ ~45 min, separate days, **drop order**, cap total weekly cardio volume |
| G7 | **Athlete-facing format.** A 6-tab workbook was "too difficult to follow"; a later copy opened read-only on the phone | Direct client feedback | Medium | Make **one tab per week, one block per training day, blank log column** the standard view; generate it from the CSV with a script that writes no workbook-protection element; keep the `.md` as the reasoning layer |
| G8 | **`russian_block.py` builds only the V5 half-body layout** | Both of the client's blocks (270 and 324 CSV rows) were built by an ad-hoc script | Medium | Add a `--split upper-lower` (T8) and `--split full-body-3` option, accessories included, so plans aren't hand-made |
| G9 | **Daily Pump has no usable reference** | Client asked for it to be usable as a bodybuilding source | Medium | Defer until ≥ 6 weeks and one split change (the original agreement); define "ready" criteria now (below) |
| G10 | **Eval library has no scenario for this client type** (coach-athlete, full-body powerbuilding, gen-pop without REVL) | New gold personas exist but no benchmark scenarios | Medium | Add scenarios in a new family; run as a *held-out* set first |
| G11 | **Evidence gaps** the skill can't close: nothing on this exact wave in trained lifters; periodization evidence mostly untrained | §2 of the trained-population file already says so | Low | Keep the labels; add the two new nuances (volume vs strength returns; cardio dose) |

## 4. Roadmap

**P1 — close the library gap (needs a benchmark before committing):** G1, G2, G3, G4 and the G5 volume rule as one reference edit (`program-library.md` + a short section in `russian-strength-program.md`). *Risk:* the earlier "start-low" rule lowered goal alignment and progression; test the new wording on the new scenarios (G10) **and** the existing 40.

**P2 — tooling (no behaviour change, low risk):** G5 (set-audit helper), G8 (`--split` options), G7 (the one-tab-per-week view script). Test by regenerating Jon's block and diffing against its current CSV.

**P3 — content when ready:** G9 Daily Pump reference. *Ready when:* ≥ 6 weeks captured, ≥ 1 split change, the master and repo mirror re-synced, and a labelled synthesis can be written without reproducing the paid programming.

**P4 — evals:** G10 scenarios (held-out first), then fold into the benchmark. Resume the cloud routine only after P1 holds on a broad run.

**Do not change:** the safety/scope rules, the eligibility gate, the REVL provenance rules, or the "never invent numbers" guards. Those are what keep the benchmark's hard failures at 1.

## 5. What a real-life test adds

Jon's own block (4-day upper/lower, started 2026-10-14) is a one-person trial: week 1 corrects the starting loads and the pull-up number; week 5 refreshes the 1RM estimates; week 9 retests. If actual results disagree with the plan (e.g. weeks 7–8 targets are unattainable, or cardio at 2 sessions stalls squat), that is **better evidence than any scenario we can write** and should become P1's first test case.

## Sources (summaries read; full papers not opened)

- [Baz-Valle 2022, volume systematic review](https://pubmed.ncbi.nlm.nih.gov/35291645/)
- [Linear vs daily undulating periodization, hypertrophy meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5571788/)
- [Traditional vs undulating periodization, strength meta-analysis](https://pubmed.ncbi.nlm.nih.gov/35044672/)
- [Concurrent training meta-analysis (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767279)
- [Sabag 2018, concurrent HIIT and resistance training](https://pubmed.ncbi.nlm.nih.gov/29658408/)
- [Training frequency and hypertrophy summary](https://sci-sport.com/en/impact-of-training-frequency-on-muscle-strength-and-hypertrophy/)
