# Pilot runs: GPT-6 Astra, conditions A0 and A3

Written for: team members reviewing the first real-model pilot.

**These are rehearsal runs, not study data.** They test that the runner works with the real model. Do not count them in the study. Each run used the DRAFT prompt and DRAFT context (`v0.1_DRAFT`).

## What was run

One round: A0 and A3, one repeat each, with the real model (`gpt-6-astra`).

| Condition | Run folder | Started (UTC) |
|---|---|---|
| A3 | `pilot_A3_r1_20261110T005054_00_a498/` | 2026-11-10 00:50:54 |
| A0 | `pilot_A0_r1_20261110T005204_01_5416/` | 2026-11-10 00:52:04 |

A second identical round (same inputs) was also run to test `LLM_team_runs.ipynb` against the real API, then deleted as a duplicate. It completed the same way, and its observations are summarized under "How to read these results".

The detail below is for this round.

| | A0 | A3 |
|---|---|---|
| What the model was given | Question and shared background only (CTX-01 to CTX-08) | Same, plus the structure evidence (STRUCT-01 to STRUCT-08) |
| Run folder | `pilot_A0_r1_20261110T005204_01_5416/` | `pilot_A3_r1_20261110T005054_00_a498/` |
| Started (UTC) | 2026-11-10 00:52:04 | 2026-11-10 00:50:54 |
| Hypotheses returned | 2 | 3 |
| Input / output tokens | 2,181 / 1,929 | 4,596 / 2,418 |
| Cited an ID it was not given | No | No |

Settings for both: model `gpt-6-astra` (the returned model name matched), reasoning effort `medium`, max output 16,000 tokens, one repeat, no retries, status `completed`. The order was randomized (seed 20261104), so A3 ran first.

## What the model proposed

**A0 (no computational evidence)**
1. **Preparation and maturation differences** (processing, folding, zinc loading, assembly) may cause the lower pig activity. Test: reproduce the comparison with matched human and pig preparations and check protein amount and processing.
2. **Pig ADA2 may be selectively poor on free adenosine** while keeping DNA binding or editing. Test: measure free-adenosine activity and DNA binding/editing as separate readouts.

It named no specific residue, and said no alignment or pig structure was supplied.

**A3 (with structure evidence)**
1. **Preparation and maturation differences**, as in A0.
2. **Sequence differences near human positions 281 and 347** (V277A, E278K, E282G, K346S, D347R in pig) may change catalysis or dimer arrangement. Test: swap those regions between human and pig and compare activity, folding and assembly. This is the new idea that only appears with structure evidence (STRUCT-03, 04, 05, 08).
3. **Altered substrate preference with DNA activity retained**, as in A0, with an added free-deoxyadenosine arm.

## How to read these results

- **The model uses the evidence cautiously.** It says the predicted differences do not show impaired catalysis, and that STRUCT-08 has not yet been placed relative to the active site or dimer interface. It steers away from the largest shifts next to the insertion and chain ends (STRUCT-06, 07), where confidence is lower.
- **It uses the lab context.** Both runs cite CTX-08 and say recombinant protein work is supported, but that specific assays (glycan, zinc, DNA editing) must be confirmed with the team. CTX-08 does not list instruments.
- **Two runs per condition gave similar but not identical answers.** In the deleted second round, A3 again proposed the same three ideas (preparation differences, the 281/347 region, selective loss on free adenosine with DNA function kept), citing the same STRUCT records and again listing STRUCT-02 as conflicting for the 281/347 idea. A0 again proposed two ideas. Wording, ordering and some labels changed: A0's first hypothesis was rated "low" in the first round and "moderate" in the second.
- **Two runs are still too few to judge reliability.** The formal design uses three repeats per condition. The "confidence" labels are the model's own rating, not a measure of correctness, and they can change between repeats.
- **Model output is a suggestion, not a finding.** Hypotheses are not evidence about pig or human ADA2. The evidence records themselves are still DRAFT and need a second person's check.

## Files in each run folder

| File | Contents |
|---|---|
| `input.txt` / `input.json` | The exact text sent to the model |
| `output.md` | The same hypotheses as `output.json`, formatted for reading. Headings are the JSON keys |
| `output.json` | The hypotheses (parsed) |
| `response_raw.json` | The full API response |
| `run.json` | Settings, hashes, token counts and status for this run |

`run_log.csv` in this folder has one row per run. `plan_*.json` records the run order and the full config used.

## Known limits

- A1 (sequence) and A2 (surface) evidence are still placeholders, so only A0 and A3 were run.
- Cost is not recorded because no prices are set in `config.json`.
- The citation check only confirms that cited IDs were given to the model. It does not check that the model described each record correctly. Read the text against the evidence.
