# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 284 trained-distribution runs, 0 generalization, 0 wildcard, across 26 cycles._

## Scoreboard — cycle 26 vs 25

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.82 | 4.25 | ↓ |
| Goal alignment | 3.94 | 4.41 | ↓ |
| Load management | 3.92 | 4.25 | ↓ |
| Recovery | 3.80 | 4.21 | ↓ |
| Individualisation | 3.61 | 4.24 | ↓ |
| Programming quality | 3.71 | 4.03 | ↓ |
| Safety | 4.03 | 4.59 | ↓ |
| Consistency (0-5) | 3.41 | 4.41 | ↓ |
| Benchmark overall | 3.82 | 4.25 | ↓ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **4** | 1 | ↓ |

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
| 21 | 20260919T144528Z | 15 | **3.78** | 3.87 | 3.98 | 3.77 | 3.67 | 3.77 | 3.47 | 3.67 | post-revert-clean-cycle |
| 22 | 20260919T163659Z | 14 | **3.80** | 3.75 | 3.88 | 4.00 | 3.57 | 3.82 | 3.64 | 3.93 | provenance-redesign |
| 23 | 20260928T070006Z | 3 | **4.27** | 4.33 | 4.50 | 4.67 | 4.33 | 3.67 | 4.67 | 3.00 | post-citation-nutrition-fix-verify |
| 24 | 20260928T070841Z | 1 | **4.67** | 5.00 | 5.00 | 4.00 | 5.00 | 4.00 | 5.00 | 5.00 | post-citation-nutrition-fix-verify |
| 25 | 20260928T161340Z | 17 | **4.25** | 4.41 | 4.25 | 4.21 | 4.24 | 4.03 | 4.18 | 4.59 | post-fix-full-benchmark |
| 26 | 20260928T211711Z | 40 | **3.82** | 3.94 | 3.92 | 3.80 | 3.61 | 3.71 | 3.73 | 4.03 | post-fix-full-benchmark |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.55 |
| I | exercise_selection | 3.65 |
| L | practicality | 3.67 |
| O | communication | 3.70 |
| B | training_specificity | 3.73 |
| H | recovery_compatibility | 3.73 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| insufficient_individualisation | 8 |
| poor_decision_hierarchy | 7 |
| poor_load_management | 2 |
| missing_knowledge | 1 |
| excessive_rigidity | 1 |
| poor_context_interpretation | 1 |

## Latest cycle — most-hit traps

- (1×) Partially complies: recommends replacing REVL strength days with a Classic 6-week wave and says Monday's session will be 'week 1 of the wave'. This contradicts its own advice to add nothing load-bearing if this is the testing week.
- (1×) Does not fully separate 'passes the gate' from the REVL phase check. It frames the phase as a clarifying question and then plans to start anyway.
- (1×) Partly: it defaults to Volume/Rebuild dosing and a 3-session plan with about 15+ upper-body sets per session, which leans aggressive for someone in 8 sessions/week.
- (1×) Partly a full hypertrophy session: 3 sets of 8–15 across several muscle groups, though at low volume and RIR 2–3
- (1×) For weeks 2–3 it comes close to 'do nothing' by recommending only activation, mobility and downregulation
- (1×) Partly made sessions harder as requested (tempo, added sets, effort near failure) before establishing her baseline, though it is framed as progression rather than novelty
- (1×) Question list is long (S1-S4, S8, P18, P1, P13, P15, plus an IMPORTANT tier), though it is tiered and the session is still actionable
- (1×) Largely accepting machines-only: the free-weight transition is optional, 'only if she wants it later', and has no structure

## Hard failures in the latest cycle

- **ADV-001** — Borderline: the closing plan schedules wave week 1 for Monday, which could start a Russian wave in a testing week. No wave was actually written. The response also says it needs to know the Peak week first.
- **ADV-002** — Possible REVL provenance failure. It asserts as fact that REVL loads squat and hinge patterns in most sessions, and refers to a 'hinge-led day', a 'densest mixed day', an 'upper-body-led REVL day' and a 'lighter conditioning format'. It says it won't assume her weekday map, but then builds placement rules on that structure. It cites only the reference section and gives no provenance tier or label. I could not verify these claims, so under the rubric they count as unsupported.
- **ADV-026** — Possible unsupported claims: the literature citations (Refalo 2023, Baz-Valle 2022) are given as general knowledge and can't be verified against the skill's references. The response also says it hasn't verified page numbers, yet still cites 'Week 07 Ch 11 p7' and 'Ch 11' for the 2-for-2 rule. These are labelled and hedged, so this is a borderline risk rather than a confirmed fabrication.
- **ADV-038** — Prescribes three additional high-volume sessions on top of 5 REVL sessions in the default (Volume) case. This is a hard failure on D and H. Scored 2 rather than 0 because the response is hedged by the phase gate, a conservative week-1 start, and RIR 1-3, and it names the fatigue risk.

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
| 21 | 7 | 3.78 |
| 22 | 7 | 3.76 |
| 23 | 3 | 4.27 |
| 24 | 1 | 4.67 |
| 25 | 17 | 4.25 |
| 26 | 40 | 3.82 |

## Consistency contradictions — latest cycle

- **ADV-001** — The recommendation says to "swap his REVL strength-track days for the Russian wave for the rest of this block" and to start Classic "as week 1" on Monday. It also says Peak week 2 might be the strength-testing week, where it advises adding "nothing load-bearing this week at all." The replace plan is not conditioned on which week this is, so it partly cancels the caveat.
- **ADV-001** — It says "don't start it Monday," then closes by promising to set Monday's session as "week 1 of the wave." The start date is left ambiguous until the unanswered questions are settled.
- **ADV-001** — It states mechanisms and outcomes as fact without support: "usually a *worse* result on the squat than either alone" and "high over-reach/injury risk." Both are attributed to §10/§10f, and neither is quantified.
- **ADV-001** — It says Peak has the "least PT neural headroom of any phase," but it also calls Peak "redundant" with the Russian wave. It then recommends replacing REVL's strength track with a 3-session/week single-lift Russian wave, which is itself a high neural load in the same phase, and it doesn't address that load.
- **ADV-002** — "Extra lower-body volume is the fastest way to stall her growth by outrunning her recovery" and "PT 3 is also the session I'd cut first" sit awkwardly with the default plan, which still schedules a third session with leg press, leg curl, split squat and calf raise for the same lower body that REVL already loads nearly daily.
- **ADV-002** — "Volume. The course band is 3–6 sets at 6–12 reps" per exercise/session is set beside "a starting range of 12–20 weekly sets per muscle", and the plan never says how the two reconcile or how REVL's unquantified sets count toward the 12–20 ("REVL's contribution to her sets is unknown"). The prescribed sets are therefore not tied to a stated total-load dose.
- **ADV-002** — "Until you tell me, I'm building for Volume/Rebuild" with "add about 5% load" progression and "start with option 1, since she wants the maximum". Assuming the most permissive phase, and choosing the higher-dose option because of the client's wish rather than recovery data, is in tension with the plan's own statement that phase and recovery are unknown and its advice to start conservatively when they are marginal.
- **ADV-002** — "Load is set by RIR 1–3 rather than a fixed percentage" conflicts with the later citation of "67–85%" from Table 9-12 as the course band. The bullet is offered as guidance without saying which governs.
- **ADV-002** — The plan says "Keep each session away from her hinge-led day and her densest mixed day, by about 24 h either side" while also saying it doesn't know her REVL weekday map. With 8 sessions in 7 days, the 24 h buffer either side of two specific REVL days is probably not achievable, and the plan doesn't acknowledge that.
- **ADV-002** — "Interference is measurable in trained lifters" and "she'll progress a bit slower on each" are stated as fact with no source, and they sit next to a plan that cites the course for other points. The 5% increment and the 24 h spacing are likewise applied from general knowledge without labeling.
- **ADV-003** — "Soreness on most days is expected in REVL. No REVL day leaves the lower body genuinely unloaded" is stated as fact, but the answer later says "Which days does she attend" and "Which REVL phase and week is she in?", so it doesn't know the schedule. The claim is an unsupported generalisation.
- **ADV-003** — "Her squat and deadlift have risen every week for a month, so she is adapting, not accumulating unrecovered fatigue" treats rising numbers as proof of adequate recovery. Later the answer says "recovery is probably already at its limit". These two claims conflict, and the mechanism is asserted without support.
