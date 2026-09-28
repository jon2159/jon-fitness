# Routing clarification continuation handoff

**Current optimization work (2026-09-28):** The working skill is now hash
`08a1c82df3955c80`. `coaching-decision-framework.md` has a safety clarification
for unexplained symptoms, a conditional minimum-dose option when one quality stays
primary, and a rule that available PT slots are a ceiling. Native eval cases 20–22
cover those decisions. The hand-written benchmark's ADV-035 expectation now defers
exercise until concerning breathlessness is assessed; ADV-040 supplies Peak week 1
to the answerer; the grader no longer penalizes hidden metadata. The 700-scenario
library regenerated and static checks passed. **No model evaluation of this new
version has run** because the Codex CLI cannot initialize in the current restricted
sandbox. The installed `.agents/skills/jon-fitness/` copy is read-only here and has
not been synced with this new canonical reference; sync it before a Codex behavior
run. The prior corrected hash `ef1f3756ad4144ab` remains 36/40 scored, with
ADV-031/035/039/040 and two consistency grades pending. A separately labeled
canonical cycle 23 wrote `evals/results/history.jsonl` and `rotation_state.json`
during this work; preserve those concurrent results, which are outside this isolated
comparison.

**2026-09-28 optimization checkpoint:** The user's current goal is to optimize the skill.
Codex evaluated the original `e7ee73b282a89372` snapshot 40/40 and the corrected
`ef1f3756ad4144ab` snapshot 36/40 on the same benchmark. The latter still needs
ADV-031, ADV-035, ADV-039 and ADV-040 plus consistency grades for ADV-014 and ADV-016.
See `docs/routing-skill-optimization-assessment.md` for the matched comparison. Its
current +0.017/5 overall difference is too small to establish improvement. A proposed
coaching-framework patch is saved in the ignored workspace but **not applied**; it needs
behavior testing. No model process is active. The Codex CLI failed to initialize under
the current restricted sandbox (`Operation not permitted`), so the four runs cannot be
continued in this environment. When execution is available, resume
`revision-2/continue_codex_serial.py` from the saved results; it skips scored IDs.

**Current outcome:** Jon clarified that Codex should cover only the nine cases Claude
left unfinished (ADV-030, 031, 034–040). All nine have been scored on the original
snapshot and reviewed in `docs/routing-claude-remainder-codex.md`. Do not treat the
mixed-runner coverage as a 40/40 Claude result. The extra corrected full regression
was stopped at Jon's direction; no eval process is active.

## Latest user instruction

**Use Codex, not Claude.** Jon explicitly corrected the runner choice on 2026-09-28.
Claude was briefly available and a continuation was started, then stopped promptly
at Jon's correction. Its scored checkpoint remains 31/40 plus 9/10 targeted.
Codex completed its separate 40/40 baseline. Corrected revision 2 has all ten native
checks graded (28/30 expectations) and only a partial full regression.
Keep runner/version results separate and do not merge isolated rows into production history.

## Source state and edits

Jon asked to pull main, clarify routing/evidence details, test behavior after the newer
program sources, and leave work resumable by Claude. Main was already up to date.
Source commit: `5a99109` (full commit in workspace metadata). Final Markdown skill hash:
`e7ee73b282a89372`, 25 files, was the initial assessed snapshot. The corrected working
version is now `ef1f3756ad4144ab`; both have uncommitted local changes.

Changed canonical skill files:
- `SKILL.md`: tracks are conditional candidates; relevant research does not import programs;
  screening and course-specific population rules retain precedence.
- `references/russian-strength/russian-strength-program.md`: RPE/RIR research does not
  validate our exact two-session/5%/10% thresholds; Coleman did not directly test our deload.
- `references/program-library.md`: optional activities require client need and capacity;
  no standard extra off-day cardio/days; exact implementation rules are coach judgement.
- `evals/evals.json`: native cases 10–19 test original routing clarifications, T2/T5,
  Chalk limits, and Daily Pump exclusion.

Corresponding local `.agents/skills/jon-fitness/` files were synchronized. No production
harness, rubric, optimizer, scheduler or canonical result files were changed. No commits
or pushes were made. Preserve unrelated local changes (`skills-lock.json`, `.agents/`,
`.commandcode/`) and real client data.

## Durable workspace and active runs

Local ignored workspace: `evals/routing-review-workspace/2026-09-27-codex/`.
The active continuation uses Codex, with Claude's checkpoint preserved.
It contains exact snapshots, the source patch, metadata, raw per-turn calls, scores, logs
and continuation helpers. Keep it available on this laptop: it is not uploaded by Git.

## Codex continuation and corrected revision

- Baseline snapshot: `e7ee73b282a89372`, `batch-*/`, resumed via `continue_codex.py`.
- Corrected snapshot: `ef1f3756ad4144ab`, `revision-2/batch-*/`, full 40-case regression.
- Corrected native checks: `revision-2/targeted/`, cases 10–19, independent answer/grade.
- Revision 2 fixes source-page references and removes standard added cardio from Russian
  instructions; the generator still emits conditioning rows, which the coach must review
  and omit when not justified. No generator or production harness change was made.
- Both `.claude` and matching installed `.agents` source files were synchronized.

Resume helpers (check active processes first):

```bash
python3 evals/routing-review-workspace/2026-09-27-codex/continue_codex.py
python3 evals/routing-review-workspace/2026-09-27-codex/revision-2/continue_codex.py
python3 evals/routing-review-workspace/2026-09-27-codex/revision-2/targeted/run_targeted.py
```

These do not consume Claude quota. A Codex result measures Codex behavior; it does not
establish a Claude regression pass. Preserve the Claude resume commands below.

### Claude benchmark — all 40 final-state cases

Four ten-case batches live under `claude-benchmark/batch-*/`. Each uses the existing
harness and rubric, with fresh independent answer, grading and consistency turns.
The original `IS_SANDBOX=1` and DEVNULL stdin behavior is retained. A local wrapper records
raw prompts, responses and errors after each turn in `claude-calls/*.json`.

Refresh completed/pending IDs and this document's checkpoint:

```bash
python3 evals/routing-review-workspace/2026-09-27-codex/status.py
```

`claude-status.json` contains only matching-hash, matching-label, scored benchmark IDs.
Full results are in each batch's `evals/results/`; live logs are `run.log`.
An overall score alone does not prove consistency succeeded; inspect both.

Resume once an existing run is no longer active:

```bash
python3 evals/routing-review-workspace/2026-09-27-codex/continue_claude.py
```

The master and each batch have an exclusive process lock, preventing duplicate live runs.
The helper checks the snapshot hash, skips completed cases across the Claude copies,
assigns new raw-call filenames, and returns failure if selected IDs remain unscored.
Interrupted/ungraded cases remain pending. Do not change the skill snapshots mid-run;
new source changes require a new evaluation version.

### Claude targeted checks — all native cases 10–19

The original six clarification cases are in `claude-targeted-core/` (10–15). New-source
checks are in `claude-new-source-checks/` (16–19). Each uses independent Claude answer and
reference-aware evaluator turns. Prompts, responses, expectations and grades are in
`results/<id>.json`; `run.log` records progress. After confirming no prior run is active:

```bash
python3 evals/routing-review-workspace/2026-09-27-codex/claude-targeted-core/run_checks.py
python3 evals/routing-review-workspace/2026-09-27-codex/claude-new-source-checks/run_checks.py
```

Both skip successfully graded saved cases. Cases with errors or missing grades are not passes.

## Historical results — not final-state Claude completion

Canonical history ends at cycle 22 (2026-09-19T16:36:59Z). Cycle 17's four-case trend slice
is unrelated to the recent isolated attempt. Earlier Claude scored ADV-001, ADV-003,
ADV-004 and ADV-007 on hash `16c9971bb48df70b`, before the final shared-table edit.
Scores were 3.800, 3.933, 4.133 and 3.733 with no recorded hard failures. They test peak
stacking, soreness versus performance, deload-week conditioning and severe sleep restriction.
They cannot complete the current final-state benchmark.

All six earlier targeted Claude responses were saved; five received independent grading.
The sixth added cardio as standard, prompting the final clarification. A monthly spend-limit
error stopped that earlier run; it recurred during the final-state continuation. A later minimal probe returned OK, but a resumed benchmark then hit the monthly spend limit again. Current error states reset at 2026-09-28 00:50 Asia/Singapore. No process is active now. Do not alter account/billing settings.

Codex was stopped after 24/40 final-state benchmark cases. Its independent scores and partial
targeted outputs remain archived under `batch-*/` and `targeted/`. These do not establish
Claude's behavior. No model improvement claim is justified without a comparable baseline.

## Restart assessment and scheduler state

See `docs/routing-restart-assessment.md`. A fresh manual assessment was attempted; Claude is stopped on its monthly spend limit, and no scheduler
was installed or resumed, and `nightly.sh` was not invoked. Local launchctl inspection found
Daily Pump loaded with no running PID and no nightly-eval job. Cloud pause status came from
Jon's supplied account and has not been independently verified through the cloud service.
Cycle 1 is `baseline`, cycles 2–4 `nightly`: three explicitly nightly-labelled cycles.

New path coverage matters: generic hybrid goals in the main library do not explicitly test
T2/T5 routing, trained-evidence retrieval, Chalk limits or Daily Pump exclusion. Daily Pump
remains on hold, not a usable program foundation.

Before unattended scheduling resumes, review account availability, coverage and results;
ensure the cloud checkout has the intended source state (these edits are uncommitted);
review partial-run handling (`run_cycle.py` exits 0 if any case scores, while `nightly.sh`
checks exit status before proceeding); and reconcile the local fallback's three fires with
the cloud README's two-fire schedule. No such script changes were made here. Preserve all
optimizer safeguards. Do not run `nightly.sh` merely to test: it can optimize, commit and push.

## Finish the assessment

Verified follow-up findings and the correction patch are documented in
`docs/routing-clarification-followup.md`. The patch passed `git apply --check`. It corrects
course-page navigation and the Russian reference's conflicting default-cardio instruction.
The patch has now been applied to the working files as revision 2. The original snapshots
remain fixed; scores for different hashes remain separate.

1. Confirm 40 distinct scored Claude benchmark IDs and 10 graded targeted cases, with errors
   and consistency failures reported separately. At the latest stop, only 31/40 benchmark cases
   and 9/10 targeted checks are graded; Claude reports a spend reset at 00:50 Asia/Singapore. Inspect raw responses for grader findings.
2. The completed 31-case Claude slice averaged 4.20/5 with 2 hard-failure rows. Case 13 did not fully state the trained-population evidence applicability limits; case 16 chose T2 correctly but missed conditioning-experience/placement intake; case 15 remains ungraded. ADV-007 and ADV-016 were flagged for fabricated/misattributed pinpoint course citations; review and correct those citation behaviors before treating the skill as ready for unattended scheduling.
3. Separate successful routing from other omissions. For example, Claude selected T2 in
   case 16 but its evaluator flagged missing conditioning intake/placement; the prompt asks
   for a selection answer, so interpret that omission in context rather than calling the
   track selection wrong.
4. Verify flagged source claims against actual reference/course pages before editing. Treat
   grader warnings as review candidates, not confirmed facts.
5. Keep runner/hash labels separate and do not claim regression improvement from mixed models
   or different scenario sets. Do not feed isolated alternative-runner rows to the optimizer.
6. Update the assessment and final checkpoint. Leave commits/pushes and scheduler changes
   for explicit instructions; preserve unrelated changes and all real client files.

## Latest saved checkpoint

Refreshed 2026-09-28T01:30:48.221640+00:00 UTC.

Claude benchmark: 31/40 scored on final hash `e7ee73b282a89372`.
Completed: ADV-001, ADV-002, ADV-003, ADV-004, ADV-005, ADV-006, ADV-007, ADV-008, ADV-009, ADV-010, ADV-011, ADV-012, ADV-013, ADV-014, ADV-015, ADV-016, ADV-017, ADV-018, ADV-019, ADV-020, ADV-021, ADV-022, ADV-023, ADV-024, ADV-025, ADV-026, ADV-027, ADV-028, ADV-029, ADV-032, ADV-033.
Pending: ADV-030, ADV-031, ADV-034, ADV-035, ADV-036, ADV-037, ADV-038, ADV-039, ADV-040.

Claude targeted cases graded: 9/10.
Case 15: pending/errored (exit 1: ).
Claude was stopped at Jon's explicit request to use Codex. Do not resume Claude without a new instruction.
