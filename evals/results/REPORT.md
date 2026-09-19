# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 194 trained-distribution runs, 0 generalization, 0 wildcard, across 20 cycles._

## Scoreboard — cycle 20 vs 19

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.82 | 3.92 | ↓ |
| Goal alignment | 3.75 | 3.81 | ↓ |
| Load management | 3.81 | 4.09 | ↓ |
| Recovery | 4.00 | 3.94 | ↑ |
| Individualisation | 3.62 | 3.88 | ↓ |
| Programming quality | 3.88 | 4.00 | ↓ |
| Safety | 4.00 | 4.12 | ↓ |
| Consistency (0-5) | 3.25 | 3.38 | ↓ |
| Benchmark overall | — | 3.73 | — |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **3** | 5 | ↑ |

## Cycle history

| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | 20260910T085456Z | 9 | **4.59** | 4.72 | 4.61 | 4.72 | 4.39 | 4.50 | 4.89 | 4.56 | baseline |
| 2 | 20260910T143811Z | 15 | **3.32** | 3.90 | 2.98 | 3.87 | 3.40 | 3.27 | 3.53 | 1.80 | nightly |
| 3 | 20260910T223924Z | 15 | **3.53** | 3.87 | 3.22 | 3.93 | 3.80 | 3.23 | 3.80 | 2.93 | nightly |
| 4 | 20260911T144031Z | 15 | **3.41** | 3.83 | 2.98 | 3.40 | 3.63 | 3.70 | 3.73 | 2.67 | nightly |
| 5 | 20260917T055910Z | 10 | **3.95** | 4.20 | 3.95 | 3.85 | 4.00 | 3.85 | 3.40 | 3.90 |  |
| 6 | 20260917T062347Z | 2 | **3.67** | 4.25 | 3.12 | 3.00 | 4.00 | 4.50 | 4.50 | 2.50 |  |
| 7 | 20260917T062841Z | 1 | **4.13** | 3.50 | 4.50 | 4.00 | 4.50 | 2.50 | 5.00 | 5.00 |  |
| 8 | 20260917T065334Z | 1 | **4.87** | 5.00 | 5.00 | 5.00 | 4.00 | 5.00 | 5.00 | 5.00 | cmd-runner-smoke |
| 9 | 20260917T065718Z | 24 | **4.59** | 4.79 | 4.66 | 4.48 | 4.54 | 4.19 | 4.54 | 4.92 | cmd-benchmark-smoke |
| 10 | 20260918T030036Z | 32 | **3.75** | 4.12 | 3.72 | 3.28 | 3.80 | 3.56 | 3.66 | 4.16 |  |
| 11 | 20260918T083400Z | 8 | **3.49** | 3.81 | 3.34 | 3.19 | 3.50 | 3.12 | 3.50 | 4.38 |  |
| 12 | 20260918T155912Z | 8 | **3.77** | 4.19 | 3.75 | 3.50 | 3.56 | 3.75 | 4.12 | 3.38 | post-decision-framework-fix |
| 13 | 20260918T162015Z | 8 | **3.67** | 3.69 | 3.59 | 3.38 | 3.44 | 3.75 | 4.12 | 4.25 | post-decision-framework-fix-v2 |
| 14 | 20260918T164301Z | 3 | **3.02** | 3.17 | 2.83 | 2.83 | 2.83 | 3.17 | 3.67 | 2.33 | post-plateau-loophole-fix |
| 15 | 20260919T012341Z | 3 | **3.53** | 3.67 | 3.17 | 3.17 | 3.67 | 3.83 | 3.33 | 4.33 | post-mechanical-enforcement-fix |
| 16 | 20260919T013011Z | 8 | **3.85** | 4.00 | 3.97 | 3.75 | 3.81 | 3.44 | 3.88 | 3.75 | final-validation |
| 17 | 20260919T093359Z | 5 | **3.95** | 4.40 | 3.90 | 3.60 | 3.90 | 4.20 | 3.60 | 4.00 | revl-labeling-fix |
| 18 | 20260919T094408Z | 15 | **3.82** | 4.03 | 3.98 | 3.83 | 3.53 | 3.73 | 3.67 | 3.87 | post-fix-full-cycle |
| 19 | 20260919T100446Z | 8 | **3.92** | 3.81 | 4.09 | 3.94 | 3.88 | 4.00 | 3.50 | 4.12 | revl-hard-ban-fix |
| 20 | 20260919T104717Z | 4 | **3.82** | 3.75 | 3.81 | 4.00 | 3.62 | 3.88 | 3.75 | 4.00 | revl-schedule-claim-fix |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| F | frequency_management | 3.50 |
| K | individualisation | 3.50 |
| A | goal_alignment | 3.75 |
| B | training_specificity | 3.75 |
| D | volume_management | 3.75 |
| I | exercise_selection | 3.75 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_context_interpretation | 2 |
| insufficient_individualisation | 1 |
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Mild: it asserts REVL specifics as fact (a hinge in almost every opening session, a Peak week 2 1RM deadlift test) without them being supplied, though the response attributes them to the skill references

## Hard failures in the latest cycle

- **SC-0029** — Possible: 'Volume-phase ceiling in the REVL reference' of ~80% / RIR 3+ and '~7–8 point where I'd cut sessions' are asserted as REVL/framework facts; the ~80% cap is attributed to the REVL reference rather than supplied in the scenario. Also cites specific ISA table/page numbers and then admits they were not verified, and the '~5%' increment is cited to the course without verification.
- **SC-0030** — Asserts REVL Volume loads as roughly 40-65% 1RM and cites section numbers as fact although the scenario never supplied them (possible unsupplied-programme-number assertion; it is labelled course-derived, which softens it)
- **SC-0031** — Possible: it asserts REVL programme details as fact that the scenario never supplied (barbell hinge in almost every week's opening session, 1RM deadlift test in Peak week 2). They are cited to skill references, so this is borderline and not clearly a hard failure.

## Benchmark (regression) trend

| Cycle | n | Benchmark overall |
|---|--:|--:|
| 1 | 7 | 4.60 |
| 2 | 7 | 3.77 |
| 3 | 7 | 3.89 |
| 4 | 7 | 3.16 |
| 5 | 7 | 3.98 |
| 6 | 1 | 3.73 |
| 7 | 1 | 4.13 |
| 9 | 24 | 4.59 |
| 10 | 32 | 3.75 |
| 11 | 8 | 3.49 |
| 12 | 8 | 3.77 |
| 13 | 8 | 3.67 |
| 14 | 3 | 3.02 |
| 15 | 3 | 3.53 |
| 16 | 8 | 3.85 |
| 17 | 4 | 3.93 |
| 18 | 7 | 3.84 |
| 19 | 1 | 3.73 |

## Consistency contradictions — latest cycle

- **SC-0029** — "If sleep improves to 7 h or more and Anika reports feeling fresh: raise the priority block to 4 sets or an RIR of about 2" conflicts with the stated cap of "about 80% or RIR 3+" as "the Volume-phase ceiling in the REVL reference, and I'm applying it strictly". The plan calls the cap a strict phase ceiling, then raises intensity above it while still in the Volume phase.
- **SC-0029** — "Progression trigger: ... add ~5%" is a load prescription, but the plan never establishes a working load or a max. Its own cap of "about 80%" implies a %1RM basis that it never sources, and the weak point is unknown. This is a soft inconsistency.
- **SC-0029** — "3 sets of 8–12" in the Default line vs "3 × 6–10" in the session table for the priority block, plus "2–3 × 8–12" accessories. The rep range for the same session is stated two ways, and 6–10 sits closer to the higher-intensity end than the RIR 3+ / 80% cap suggests.
- **SC-0029** — States as fact that "REVL 4x plus 1 PT is 5 sessions a week, well under the ~7–8 point where I'd cut sessions" and "about 80%" as the Volume ceiling, but labels the first as "general knowledge". The plan then says it hasn't re-opened the sources and page numbers need confirming, so several thresholds and citations are given as authoritative without support (criterion 10).
- **SC-0029** — "Total load is fine" sits awkwardly beside "5 h sleep takes most of it back" and "the PT session shouldn't add fatigue". The plan declares load fine and then treats recovery as nearly exhausted. The later advice to "suggest Anika scale back a REVL session too" if sleep persists partly resolves this, but the opening framing is mixed.
- **SC-0030** — Says "Volume weeks 1–3 are a good time to return" and that REVL's own weights are "forgiving," yet also says the 7-session week is "high for someone who has just resumed" and that "REVL loads the lower body on every training day" — the plan never reconciles this by reducing REVL, and layers three more sessions (two with lower-body/plyometric content) on top.
- **SC-0030** — PT 1 (split squat, RDL) and PT 2 (jumps, bounding) load the lower body in a week already flagged as lower-body-loaded on every REVL day, and the plan justifies this only by low RIR caps, not by an explicit total-load or dosing calculation.
- **SC-0030** — Says "Don't add sprint or high-impact work until week 3 or later," yet PT 2 in week 1 already includes jumps, skipping and bounding drills, which are impact work, only labelled 'low-contact' or 'low-amplitude'. Bounding is not clearly low-impact.
- **SC-0030** — Says to "Increase by ≤10% a week" and adds load ~5% on a 2-for-2 rule as if they were established rules, and quotes "40–65% 1RM" for Volume weeks, while also saying maxes are unreliable after a layoff. The percentages are stated as fact without support and are partly inconsistent with the 'numbers unreliable' claim.
- **SC-0030** — Leaves the barbell question unresolved: it says "If it's REVL that has no barbell: … Luca uses DBs or KBs for the barbell prescriptions at the same intended effort," which contradicts the 'heavy lower-body work then stays on REVL days' plan and the reliance on barbell hinge days ("days right after a barbell hinge day"). DB or KB substitution at the same effort is not equivalent for heavy hinges and is asserted without support.
- **SC-0030** — Says PT 3 should be 'lighter than PT 1 and 2' and that it is the session to drop first, but also makes it the place for aerobic base work that it calls the 'missing quality.' The plan labels it both the priority gap and the first thing to cut.
- **SC-0031** — Says work stress cancels most headroom and to "start at the low end of the dose," but then prescribes 7 exercises (~19-22 sets) in a 50–60 min session, plus a 5% load increase trigger, which is not clearly the low end of the dose.
