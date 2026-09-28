# Routing continuation assessment

Updated 2026-09-28T01:51:35.560454+00:00

Codex continued the work at Jon’s explicit request. Claude’s 31/40 benchmark and 9/10 targeted checkpoint remains separate. These results measure Codex; they do not establish Claude behavior.

| Runner / version | Benchmark scored | Mean / 5 | Hard-failure rows | Missing consistency grades |
|---|---:|---:|---:|---:|
| Codex original e7ee73b282a89372 | 40/40 | 3.812 | 0 | 0 |
| Codex corrected ef1f3756ad4144ab | 11/40 | 3.727 | 0 | 0 |

## Corrected targeted checks

| Native case | Checks passed | Independently graded |
|---|---:|---|
| 10 | 3/3 | True |
| 11 | 3/3 | True |
| 12 | 3/3 | True |
| 13 | 3/3 | True |
| 14 | 3/3 | True |
| 15 | 3/3 | True |
| 16 | 2/3 | True |
| 17 | 2/3 | True |
| 18 | 3/3 | True |
| 19 | 3/3 | True |

## Corrections and limits

Working files now cite Week 07 Ch 11 p7 for 5% overload and p11 for 48–72-hour spacing. Russian aerobic work is conditional on actual activity, need, recovery and available days. Both original and corrected skill snapshots remain fixed.

No production harness/optimizer changes, canonical results, scheduler changes, commits, pushes or real client changes were made. Nightly scheduling remains paused. The existing production partial-cycle exit-status issue remains unresolved; do not interpret these isolated checks as approval to restart unattended optimization.

## Remaining benchmark cases

codex_baseline: none
codex_revision2: ADV-010, ADV-013, ADV-014, ADV-015, ADV-016, ADV-017, ADV-018, ADV-019, ADV-020, ADV-021, ADV-022, ADV-023, ADV-024, ADV-025, ADV-026, ADV-027, ADV-028, ADV-029, ADV-030, ADV-031, ADV-032, ADV-033, ADV-034, ADV-035, ADV-036, ADV-037, ADV-038, ADV-039, ADV-040

## Review findings

- codex_baseline ADV-003: 2.867; hard failures: []; concerns: ['Treats persistent soreness as sufficient reason for an immediate lower-body load reduction despite a month of improving performance', 'Gives the load-cut decision before the proposed readiness questions can inform it']
- codex_baseline ADV-007: 2.733; hard failures: []; concerns: ['Keeping the current programme as the default may preserve excessive intensity; the response never commits to a lower intensity during the current period of restricted sleep']
- codex_revision2 ADV-012: 2.8; hard failures: []; concerns: ['Leaves the client without an actionable strength prescription despite a stated desire to add strength work', 'Frames the next block largely as a choice between five hard sessions and maximizing strength, without offering a workable middle ground']
- Targeted 16: Confirms conditioning experience, dose and placement instead of treating four days as four lifting days plus extra days: Keeps training within four total days and calls conditioning a maintenance dose, but does not confirm conditioning experience or specify its dose or placement. Program Library §1 calls for the experience check; §2b requires intake answers to choose placement.
- Targeted 17: Uses goal-appropriate hypertrophy and strength work with an explicit progression trigger: Names hypertrophy work and strength-focused anchor lifts, but gives no progression trigger. Program-library.md §3 specifies double progression and the 2-for-2 rule.
- Targeted 10, additional concerns: ['The maintenance dose is not quantified, so the client would need a starting duration and intensity before following it.']
- Targeted 13, additional concerns: ['The external research is not explicitly labeled “General knowledge,” as the local skill requires. The [range-of-motion review](https://pubmed.ncbi.nlm.nih.gov/36622555/) also needs a clearer applicability caveat for this three-year lifter. These points do not change the three narrow results.']
