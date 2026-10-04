# jon-fitness — evaluation performance history

_Auto-written by `evals/run_cycle.py`. 333 trained-distribution runs, 0 generalization, 0 wildcard, across 29 cycles._

## Scoreboard — cycle 29 vs 28

| Metric | Current | Previous | Trend |
|---|--:|--:|:-:|
| Overall (trained) | 3.86 | 4.33 | ↓ |
| Goal alignment | 3.96 | 4.50 | ↓ |
| Load management | 3.92 | 4.50 | ↓ |
| Recovery | 4.04 | 4.00 | ↑ |
| Individualisation | 3.67 | 4.00 | ↓ |
| Programming quality | 3.83 | 4.00 | ↓ |
| Safety | 3.83 | 5.00 | ↓ |
| Consistency (0-5) | 3.25 | 4.00 | ↓ |
| Benchmark overall | 3.79 | 4.33 | ↓ |
| Generalization overall | — | — | — |
| **Hard failures (count)** | **2** | 0 | ↓ |

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
| 27 | 20261004T115536Z | 36 | **3.87** | 4.01 | 3.90 | 3.82 | 3.79 | 3.69 | 3.92 | 4.08 | regr-poor_decision_hierarchy |
| 28 | 20261004T163443Z | 1 | **4.33** | 4.50 | 4.50 | 4.00 | 4.00 | 4.00 | 5.00 | 5.00 | probe-recheck |
| 29 | 20261004T163538Z | 12 | **3.86** | 3.96 | 3.92 | 4.04 | 3.67 | 3.83 | 3.58 | 3.83 | target-recheck |

## Latest cycle — weakest dimensions

| Dim | Name | Mean |
|---|---|--:|
| K | individualisation | 3.58 |
| M | long_term_coherence | 3.58 |
| B | training_specificity | 3.75 |
| D | volume_management | 3.75 |
| J | progression | 3.75 |
| L | practicality | 3.75 |

## Latest cycle — failure categories

| Category | n |
|---|--:|
| poor_decision_hierarchy | 3 |
| insufficient_individualisation | 2 |
| poor_load_management | 1 |

## Latest cycle — most-hit traps

- (1×) Wrote three full hypertrophy sessions because three slots exist, and defaulted to running all three
- (1×) Prescribing more work than the time allows (12-14 hard sets plus a carry per 30-minute session, with a 5-min warm-up and a cool-down, is over budget; the fix is deferred to 'cut set counts')

## Hard failures in the latest cycle

- **ADV-038** — Prescribed three additional hypertrophy sessions of roughly 40-50 min each on top of 5 REVL sessions as the default (about 14-17 working sets per upper session). They are isolation-focused and low systemic cost, but the hard-failure condition is still arguably triggered. Dimension D is scored 2 rather than 0 because of the mitigations.
- **SC-0052** — Possible unsupported REVL claims asserted as fact: 'No day of a REVL week leaves the lower body unloaded', 'Upper-body work is concentrated on fewer days than lower-body work', and 'Build loads are climbing toward near-maximal'. They are tagged to the REVL reference but without a lower-bound or provenance caveat, and the grader cannot verify them from the response alone. Affects C, K and N, which are held at 3-4 rather than zeroed because they are labelled as reference-derived.

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
| 27 | 36 | 3.87 |
| 28 | 1 | 4.33 |
| 29 | 7 | 3.79 |

## Consistency contradictions — latest cycle

- **ADV-037** — "The lower-body part is my coaching judgement from general knowledge. I haven't pulled course pages for it" is followed by specific unsupported figures stated as fact: "Restart at roughly 60–70% of his old loads", "Progress about 5–10% a week", "clears within about 48 hours" and "peaks around 24–72 hours". The response admits it has no source, yet it gives these numbers with no flag that they are heuristics.
- **ADV-037** — "Cancel the session if he can't move comfortably" sits alongside "Train around it... Upper-body work at a reduced load is fine" and "Add easy movement... bike". The conditions for training upper body and moving versus cancelling the whole session are not clearly separated. This is a soft ambiguity, not a hard contradiction.
- **ADV-038** — "Do not train to failure, because her cumulative fatigue is already high" asserts high fatigue as fact, though the client's recovery/fatigue state was never given. It is also stated alongside "I don't yet know her phase".
- **ADV-038** — "My default is to run all three as written" (including C) sits uneasily with "Session C is the one to cut first... the most expensive session" and the opening point that she has no full rest day. Running the costliest session by default is only weakly justified.
- **ADV-038** — "Keep PT clear of about 24 h either side of her densest mixed REVL day and her hinge-led day" is hard to reconcile with "three PT sessions means at least one lands on a REVL day" and with 8 sessions in 7 days. Five REVL days plus a 24 h buffer around two of them leaves almost no valid slots, and the plan gives no concrete resolution.
- **ADV-038** — Session B is placed "on or next to her upper-body-led REVL day, since REVL barely loads her legs that day", but B is an upper-body session (chest, shoulders, triceps). Stacking it on the REVL upper day adds pressing volume to the very area REVL already loads, which contradicts the stated aim of adding work REVL under-serves.
- **ADV-038** — Session B includes an incline DB press and a low-to-high cable fly, which are chest work, while the stated REVL gaps list no chest. This is a minor mismatch with the 'under-served' rationale.
- **ADV-038** — "Hypertrophy band from Table 9-12" and "Wk07 Ch11 p7, p20" are cited to the course digest while the plan admits "I haven't re-verified the page this turn". The RIR 1–3 and the 60–90 s rest are given with only soft support.
- **ADV-038** — The plan assumes "Volume or Rebuild" as the default but gives no volume cut or build-up rule for Rebuild. It only gives a Build adjustment, so Rebuild is treated like Volume without justification.
- **ADV-038** — Fixed 3–4 sets of 8–15 reps with 60–90 s rest is stated as the default dose for all three sessions. Yet the Build row says to halve the volume, and the plan never says how this default relates to an unknown training age.
- **ADV-039** — Opens with "trim volume a little" and "Drop extra accessory sets", but the progression trigger says "add about 5% load" and the client asked for harder sessions. This is a soft tension: it says to hold load and not make sessions harder, then builds in load increases. It is partly justified by the conditional "if load can't hold or rises, don't add volume".
- **ADV-039** — The progression rule says "If load can't hold or rises, don't add volume. That's the signal the deficit is too big." The phrase "or rises" is incoherent, because rising load is the success condition elsewhere ("If her lifts are flat or rising, she is retaining muscle"). It treats a rising load as a sign the deficit is too big.
