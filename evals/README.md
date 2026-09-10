# jon-fitness — sports-science evaluation, benchmarking & optimization system

Continuously checks whether `jon-fitness` behaves like a **high-level S&C coach and sports
scientist** — interpreting training context, managing training stress, individualising, and
making evidence-informed trade-offs across hundreds of realistic client scenarios — and feeds
the results back into the skill's instructions and references.

It evaluates the skill as a **decision-making system**, not a workout generator. Quality of
programming decisions beats quantity of exercises prescribed. It does **not** optimise for
more volume, more variety, or harder sessions — it optimises for *appropriate stimulus and
sustainable progression*.

## Layout

| Path | What |
|---|---|
| `rubric.md` | The 15 scoring dimensions (A–O, 0–5) + composites + hard-failure rules |
| `generate_scenarios.py` | Builds `scenarios/scenarios.json` (~700) by composing decision axes |
| `scenarios/adversarial.json` | 40 hand-authored benchmark scenarios where the obvious answer is wrong |
| `scenarios/scenarios.json` | Generated library (generated + adversarial merged) |
| `run_cycle.py` | Runs one cycle: answer → independent grade → record |
| `optimize.py` | Clusters recurring failures → `results/PROPOSALS.md`; `--apply` = guarded, regression-tested edit |
| `nightly.sh` | Orchestrator the cloud routine calls |
| `results/history.jsonl` | One line per scored scenario run — the permanent record |
| `results/cycles/<ts>.json` | Full detail of each cycle incl. the raw responses |
| `results/REPORT.md` | Auto-written performance history + latest weaknesses |
| `results/PROPOSALS.md` | Current improvement candidates |
| `results/rotation_state.json` | Which scenarios were run when (drives rotation) |

## How a cycle works

```
scenario  ->  answer:  fresh `claude -p` turn, project skills available, answers the client
          ->  grade:   second independent `claude -p` turn scores 0–5 on A–O against the
                       scenario's own expected_priorities / traps / must_not
          ->  record:  history.jsonl + cycles/<ts>.json + refresh REPORT.md
```

Two separate model turns so the grader never sees its own reasoning. Each scenario carries
**its own** expected priorities, baited traps, and hard-failure list, derived from the axis
combination — so grading is per-scenario, not generic.

## Scenario library

Composed from axes that each **change the correct answer**: environment (commercial
unstructured / machines / program-hopper / soreness-chaser / structured / REVL / REVL+solo /
REVL+running / gym+running / group+bodybuilding / group+powerlifting) × training frequency ×
REVL phase (Volume / Build / Deload / Peak Wk 1–3 / Rebuild) × goal (8 hypertrophy, 5
strength, hybrids, conditioning, body-comp, movement, weak-point) × training age × recovery
context × constraint × PT-session frequency.

> **BFT was dropped** from the library — the skill has no BFT reference, so BFT scenarios
> could only test whether the skill *asks* rather than fabricates. If a BFT reference is
> built later (the way `revl-class-integration.md` was), add a `bft` environment family here.

The **benchmark suite** (`benchmark: true`, all 40 in `adversarial.json`) is permanent and
never rotated out — every cycle runs a slice of it so regressions surface immediately.

## Scoring

15 dimensions, 0–5 (`rubric.md`): goal alignment, training specificity, total training load,
volume / intensity / frequency / fatigue management, recovery compatibility, exercise
selection, progression, individualisation, practicality, long-term coherence, safety &
caution, communication. Composites tracked over time: overall, goal-alignment,
load-management, recovery, individualisation, programming-quality, long-term-planning,
safety. **Automatic 0** on the affected dimension for fabricated client info, fabricated
citations/loads, out-of-scope medical/nutrition advice, unscreened near-maximal prescription,
or stating an unsupplied REVL number as fact.

## Optimization loop

`optimize.py` (analyse mode, safe, nightly-on-every-3rd-cycle):
1. cluster recent failures by `failure_category`
2. weight by how many **distinct cycles** each recurs in (never optimise on one scenario)
3. write `results/PROPOSALS.md` — candidates flagged ✅ auto-apply (≥3 cycles, ≥6 hits, one
   category, one target file) vs 👤 human review

`optimize.py --apply` (guarded, weekly on Sunday UTC):
1. take the top ✅ candidate; refuse if the working tree is dirty
2. a fresh Claude drafts the **smallest** edit to **one** skill/reference file — never
   weakening safety/scope/evidence rules, never touching `russian-strength-program.md`
   unless the failure is about the Russian methodology itself
3. run `run_cycle.py --benchmark-only` (regression) + a targeted sample of the affected category
4. **keep** only if benchmark overall doesn't drop by > `--tol` (0.05) **and** the targeted
   category improves by ≥ `--gain` (0.15); otherwise `git checkout` the edit
5. commit results always; commit the skill edit only if kept

## Regression testing

The benchmark suite is the regression baseline. `run_cycle.py --benchmark-only` runs all 40.
`REPORT.md` carries a "Benchmark trend" table so an improvement in one area can't silently
degrade another.

## Nightly schedule (cloud routine)

The runner shells out to the local `claude` CLI, so a **laptop cron would only fire while the
Mac is awake**. Instead it runs as a **cloud routine** (Anthropic cloud, laptop-independent):
it clones this repo from GitHub, runs `evals/nightly.sh`, commits results, pushes.

- **3 fires/night**, ~22:30 / 02:30 / 06:30 **Asia/Singapore** (14:30 / 18:30 / 22:30 UTC),
  covering the 10 pm → 9:30 am window.
- Each fire = one 25-scenario cycle (~7 benchmark + ~18 rotated, least-recently-run first).
  The whole library is covered every ~13 nights of full runs; the benchmark every night.
- If a fire is short on usage it records what it completed; the next fire resumes rotation —
  so "re-run 1–2× a night per token budget" happens naturally.
- Cloud routines cap at 1-hour cron minimum and the routine's own quota handling applies.

Manage / pause / see runs: https://claude.ai/code/routines

## Running it by hand

```
python evals/generate_scenarios.py --stats     # (re)build the library, show the spread
python evals/run_cycle.py --dry-run             # see what the next cycle would pick
python evals/run_cycle.py                        # one 25-scenario cycle (~30–50 min)
python evals/run_cycle.py --benchmark-only       # full 40-scenario regression run
python evals/run_cycle.py --only ADV-006 SC-0100 # specific scenarios
python evals/optimize.py                         # write PROPOSALS.md
python evals/optimize.py --apply --dry-run       # show what a guarded apply would do
bash  evals/nightly.sh                           # the full nightly sequence
```

## The objective

Make `jon-fitness` progressively better at:

> *Given everything this client is already doing, their goals, their recovery capacity, and
> their available training time — what is the highest-value training intervention next?*

Better decisions → better programming → better recovery management → better adherence →
better long-term adaptation.
