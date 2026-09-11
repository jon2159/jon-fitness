# AGENTS.md

## What this repository is

This is **not a software application** — it is a personal training knowledge system plus its
continuous evaluation harness. Two things live here:

1. **The `jon-fitness` skill** (`.claude/skills/jon-fitness/`) — an "evidence-grounded CPT"
   persona that answers fitness/training questions and maintains client fitness plans, with
   every recommendation traceable to Jon's ISA CPT course notes (an ACE-based curriculum).
2. **An eval/optimization system** (`evals/`) that continuously measures whether the skill
   behaves like a senior S&C coach across ~700 synthetic client scenarios, and can
   auto-edit the skill's reference files via a guarded, regression-tested loop.

The gym-programming content directories (`REVL Block*/`, `source/isa-cpt-pdfs/`) are raw
source material, not code. Python is used only for tooling — there is no app to build, run,
or deploy.

## Repository layout

| Path | What |
|---|---|
| `.claude/skills/jon-fitness/` | The skill: `SKILL.md` (behavior spec), `references/` (course notes + derived digests), `templates/`, `scripts/` |
| `evals/` | Scenario generation, scoring rubric, cycle runner, optimizer, results |
| `source/` | Raw PDFs + extraction scripts (`build.py`, `polish.py`, `strip_images.py`, `extract_revl.py`, `analyze_revl.py`) |
| `REVL Block 1/2/3 programming 2026/` | ~264 gym-workout screenshot PNGs (git-ignored, **local only**) with `INDEX.md` + analysis per block |
| `clients/` | Per-client plan pairs `<name>_fitness_plan.{md,csv}` (git-ignored — **personal health data, never publish**) |
| `docs/` | Design documents kept as rationale (e.g. `russian-strength-integration-plan.md`) |

## Essential commands

```bash
# Eval cycle (each spawns real `claude -p` subprocesses; a full cycle takes ~30–50 min)
python evals/run_cycle.py --dry-run            # show what the next cycle would pick
python evals/run_cycle.py --n 10               # smaller cycle
python evals/run_cycle.py --benchmark-only     # full 40-scenario regression run
python evals/run_cycle.py --only ADV-006 SC-0100

# Scenario library
python evals/generate_scenarios.py --stats     # (re)build ~700 scenarios deterministically

# Optimizer (clustered failure analysis → improvement proposals)
python evals/optimize.py                       # analyse only, writes results/PROPOSALS.md
python evals/optimize.py --apply --dry-run     # preview a guarded skill edit
bash evals/nightly.sh                          # full nightly sequence (pull → regen → cycle → optimize → commit/push)

# Grader checks (see evals/HARNESS_INTEGRATION.md)
python evals/grader_reliability.py --k 3       # self-consistency of the grader
python evals/grader_validity.py                # calibration vs human gold scores (needs Jon's human_scores filled in)

# Held-out / exploratory sets
python evals/generate_generalization.py        # 40 held-out scenarios, deterministic
python evals/wildcards.py                      # fresh Claude invents new tricky scenarios (non-deterministic)

# Skill client-plan scripts
python .claude/skills/jon-fitness/scripts/new_client.py "John Tan"     # scaffold plan pair
python .claude/skills/jon-fitness/scripts/russian_block.py             # strength-block CSV from 1-RMs
python .claude/skills/jon-fitness/scripts/validate_plan.py clients/<name>_fitness_plan.md

# Source extraction (rarely needed)
python source/build.py            # PDFs → ./out/<lesson>/<lesson>.md (needs PyMuPDF)
python source/extract_revl.py     # OCR screenshots → source/revl_raw_data.md (--limit 6 to smoke test)
python source/analyze_revl.py     # frequency tables → source/revl_programming_analysis.md
```

There is no test suite, linter, or build for the "project" itself — the **benchmark suite
(`run_cycle.py --benchmark-only`) is the regression test**, and the two grader scripts are the
test-suite analog for the grading system. Python 3 with only stdlib + `PyMuPDF` (for
`build.py`) + `rapidocr-onnxruntime` (for `extract_revl.py`); no requirements file exists.

## Critical gotchas

- **`clients/` is git-ignored personal health data.** Never commit, move, or publish anything
  in it. Same for `REVL Block*/` directories (large local-only binary assets) and
  `source/.revl_ocr_cache/`.
- **Never fabricate client data or course citations.** The rubric scores an automatic 0 for
  invented client info, invented numbers/protocols attributed to the course, out-of-scope
  medical/nutrition advice, unscreened near-maximal prescriptions, or stating a REVL number
  as fact. This applies to any code/docs touching the eval too.
- **Specific REVL loads/reps from the screenshots are approximate OCR** — never present one
  as fact. The analysis files label claims `[Observed] / [Pattern] / [Inference]`; preserve
  that labeling.
- **Nested `claude -p` calls** in `run_cycle.py` / `optimize.py` set `IS_SANDBOX=1` and
  redirect stdin to `/dev/null` — required so `--permission-mode` works under root in the
  cloud container and the subprocess doesn't eat the parent's stdin. Preserve both if editing.
- **`optimize.py --apply` has hard guardrails** (don't weaken them): refuses on a dirty
  working tree, edits exactly one skill file, never weakens safety/scope/evidence rules, never
  touches `russian-strength-program.md` unless the failure is about that methodology, keeps
  the edit only if the benchmark doesn't drop >0.05 and the targeted category improves ≥0.15,
  otherwise `git checkout`s the change. Analysis mode only writes `PROPOSALS.md` — steps 1–4
  of `nightly.sh` never touch the skill.
- **The optimizer must not see generalization/wildcard rows.** In `optimize.py`, `rows()`
  excludes `set in ("generalization", "wildcard")` — those sets are read-only scoreboards;
  only `primary` + `benchmark` drive proposals.
- **`gold_responses.json` is incomplete**: it needs Jon's human `human_scores` filled in
  before `grader_validity.py` can run.
- **BFT was deliberately dropped from the scenario library** (the skill has no BFT reference).
  Don't re-add a BFT environment family unless a `bft` reference is built first.
- **Two-turn grading is intentional**: the grader is a separate, independent `claude -p` turn
  so it never sees the answerer's reasoning. Don't merge them.
- **Cloud routine context**: `nightly.sh` runs on Anthropic cloud (not the laptop) — it
  clones the repo, runs, commits, pushes. It passes `--ff-only` on pull and tolerates pull
  failure. 3 fires/night Asia/Singapore, ~25 scenarios each, covering the full library every
  ~13 nights; the 40-scenario adversarial benchmark (`benchmark: true`) runs a slice every
  night and is never rotated out.

## Architecture: how the eval system fits together

```
generate_scenarios.py ──► scenarios/scenarios.json (~700: generated + 40 adversarial)
generate_generalization.py ──► scenarios/generalization.json (40 held-out)
                                     │
                          run_cycle.py  (answer turn → grade turn → record)
                                     │
        results/history.jsonl  +  results/cycles/<ts>.json  +  results/REPORT.md
                                     │
        rotation_state.json (least-recently-run selection)   optimize.py
                                     │                        │
                          clusters failures by category ──► results/PROPOSALS.md
                                     │                        │
                        nightly.sh orchestrates all of it, guarded --apply edits the skill
```

- **Scenarios** are composed along decision axes (environment × frequency × REVL phase ×
  goal × training age × recovery × constraint × PT frequency). Each scenario carries *its
  own* `expected_priorities`, baited `traps`, and `must_not` hard-failure list — grading is
  per-scenario, never generic.
- **Scoring**: 15 dimensions A–O, 0–5 (`rubric.md`), plus composite scores and an
  automatic-0 hard-failure list. `REPORT.md` tracks a benchmark trend table so an improvement
  in one area can't silently degrade another.
- **wildcards.py** is exploratory only: a fresh Claude (no skill in context) invents new
  scenarios; outputs are disposable.

## The skill: conventions that aren't obvious from one file

- **Everything routes through `references/COURSE_MAP.md`** — do not grep the whole
  `references/isa-cpt/` course (12 lessons, `## Page N` per slide); the map is the navigation
  layer with topic → lesson/page tables.
- **Three-tier epistemic labeling** is core behavior: *Course-supported* (cite lesson +
  page) / *Applied from the course* / *General knowledge* (flagged, minimal). Never attribute
  an invented number to the course.
- **Special populations / chronic disease / MSK chapters override the general FITT-VP
  tables** — always check for an override before using a general value.
- **REVL trigger rule**: any mention of REVL or a REVL phase (Volume/Build/Deload/Peak/
  Rebuild) requires consulting `references/revl-class-integration.md` first, and
  `russian-strength-program.md` alongside it if a Russian protocol is considered. Never stack
  two strength peaks; dose PT work on top of REVL's weekly totals.
- **Client plans are a synchronized pair**: `<name>_fitness_plan.md` (canonical state +
  reasoning + evidence) and `.csv` (derived executable schedule, reasoning kept out of it).
  Filenames are normalized (`John Tan` → `john_tan_…`). When updating: read both, update the
  `.md`, change the `.csv` only if the prescription actually changed, then run
  `validate_plan.py`. Never regenerate the whole program per message; never touch another
  client's files.
- **Evidence traceability chain** must be reconstructable: `client fact → ISA CPT section →
  interpretation → decision → CSV row`, recorded in the plan's *ISA CPT Evidence* section.
- **Screening is blocking**: if ACSM screening flags medical clearance, treat it as a BLOCKING
  gap and don't prescribe beyond what the algorithm permits. Intake uses staged MCQs
  (`references/intake-questions.md`), not a question dump.

## Editing the skill or references

- The skill lives in `.claude/skills/jon-fitness/`. Edits to `SKILL.md` or `references/`
  should be minimal and must preserve the traceability, scope-of-practice, and
  fabrication-guard rules.
- `source/` scripts regenerate `references/isa-cpt/` — the canonical extracted text is
  **inside the skill**, not in `source/`. If you change the notes, re-run
  `build.py → polish.py → strip_images.py` and copy `out/*/*.md` into the skill's
  `references/isa-cpt/`.
- There's also a Claude-Code-native eval set at `.claude/skills/jon-fitness/evals/evals.json`
  (9 scenario prompts with expectations) separate from the `evals/` harness — update it if
  you change skill behavior those evals cover.
- `skills-lock.json` at the repo root tracks an installed external skill (`agent-browser`);
  it's unrelated to the `jon-fitness` skill.

## Working in this repo

- Commits are made by both the cloud routine (results/cycles) and humans; keep result-file
  commits (`results/history.jsonl`, `REPORT.md`, `cycles/`) separate from skill edits when
  possible — `optimize.py --apply` already follows this pattern (always commit results;
  commit the skill edit only if kept).
- Design decisions are documented in `docs/` and `evals/HARNESS_INTEGRATION.md` (read it
  before touching `run_cycle.py` / `optimize.py` / `rubric.md` — it lists intentional
  wiring, including parts deliberately not yet applied).
- `evals/README.md` and `source/README.md` are accurate and maintained; prefer them for
  detail over re-deriving from code.
