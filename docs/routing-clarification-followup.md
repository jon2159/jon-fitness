# Follow-up corrections identified during the paused Claude evaluation

The original assessed snapshot remains unchanged at `e7ee73b282a89372`.
The correction patch is now applied to working files as `ef1f3756ad4144ab`. The current Claude benchmark
has 31/40 graded cases, and 9/10 targeted cases have independent grades. The current account
limit prevents further Claude calls until its stated reset at 2026-09-28 00:50 Asia/Singapore.

## Verified source errors

- `SKILL.md` routes progression to Ch 9 p7–8 and attributes the 5% load increment to Ch 9 p7.
  The actual Week 03 Ch 9 p7 is bone remodelling/Wolff's Law. Week 07 Ch 11 p7 explicitly
  contains training progression, double-progressive protocol and overload in 5% increments.
- Week 07 Ch 11 p11 contains 2–3 days/week and 48–72 hours rest between sessions. It is
  distinct from Table 9-12 (p16) and Table 11-10 (p29–31). Some reference wording conflates
  those locations, which can seed misleading pinpoint citations.
- Russian §1 explicitly says to add aerobic work as standard for every Russian-block client.
  That conflicts with the shared-engine rule requiring a confirmed need. The saved targeted
  case-15 answer followed the Russian instruction and added aerobic work by default; its
  independent grade is still pending.

## Concrete next revision

`evals/routing-review-workspace/2026-09-27-codex/proposed-followup.patch` contains a reviewable
patch correcting the navigation/citation locations and making aerobic additions conditional
on actual client activity, need, recovery and total days. It also tells the coach to review
and omit default conditioning rows emitted by the Russian CSV generator when not needed.

The patch is **applied as revision 2**, with isolated Codex targeted checks and a separate
full regression. The original frozen evaluation continues separately. Review the affected
decisions (ADV-007, ADV-016, core targeted case 15) and the required regression benchmark. Do not merge new-version
scores with the 31 old-version scores. Source files were corrected; no scheduler or canonical history was changed.
