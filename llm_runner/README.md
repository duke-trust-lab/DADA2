# LLM runner for the five ADA2 conditions (A0 to A4)

Runs the language-model experiment in a repeatable way: builds each condition's input from the same files, calls the model with fixed settings, and saves the exact inputs, outputs and a log. Everything marked DRAFT must be finalized by the team before formal runs.

## What is here

| Path | Purpose | Status |
|---|---|---|
| `LLM_team_runs.ipynb` | **Start here.** Notebook for team members: pick conditions, run them with the real model, read the hypotheses, check citations, save a summary. Pilot mode only | Ready |
| `LLM_runner.ipynb` | Fuller notebook: rebuild the A3 evidence, check inputs, pilot, formal batch, blind review sheet | Ready |
| `LLM_model_check.ipynb` | Staged tests to run when changing the model: key and model access, a tiny call, which settings the model accepts | Ready |
| `runner/llm_runner.py` | The runner (also a command-line tool) | Tested offline with a fake model and against the real API (pilot with `gpt-6-astra`) |
| `runner/build_structure_evidence.py` | Builds the A3 evidence package from the saved AlphaFold results | Ready |
| `config.json` | Model, settings, file paths, condition definitions, `frozen` switch | `model` is `gpt-6-astra`; `frozen` is `false` |
| `prompts/system_prompt_v0.1_DRAFT.md` | Rules the model must follow | DRAFT; Sienna and Dr. Bent to finalize |
| `prompts/task_prompt_v0.1_DRAFT.md` | Task text with slots for context and evidence | DRAFT |
| `prompts/output_schema.json` | Required JSON format (the packet's hypothesis-card fields) | DRAFT |
| `context/shared_context_v0.1_DRAFT.md` | Shared background, identical in all five conditions | DRAFT; every CTX record must be verified |
| `evidence/structure_evidence_A3.md` and `..._records_DRAFT.csv` | The 8 structure records (STRUCT-01 to 08) from the AlphaFold track | DRAFT; needs a second person's check |
| `evidence/sequence_evidence_A1.md`, `surface_evidence_A2.md` | Placeholders for Yang's and Sienna's packages | Waiting |
| `runs_pilot/`, `runs/`, `runs_mock/` | Saved outputs for pilot, formal, and fake-model runs. `runs_pilot/` holds the first A0 and A3 pilot (see its README); `runs/` is empty; `runs_mock/` is created only by fake-model runs and is not committed | Pilot done |

## Setup (once)

1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` in this folder and put your key in it: `OPENAI_API_KEY=...`. `.env` is ignored by git; never commit it.
3. Check `config.json`. `"model"` is set to `gpt-6-astra`, which the account used for the pilot can access; change it only with team agreement, and run `LLM_model_check.ipynb` first. The starter packet also suggests a second model for a cross-check; that is not set up. `"reasoning_effort"` is sent as the reasoning setting (the packet suggests trying standard and high, then freezing).

## Workflow

1. **Build and check inputs (no cost).** In the notebook, or `python runner/llm_runner.py dry-run`. It checks that the context and system prompt are identical in all conditions and that each evidence package appears unchanged inside A4, and shows approximate input size.
2. **Rehearse with a fake model (no cost).** `python runner/llm_runner.py run --mock --pilot`. The fake model deliberately cites a non-existent ID so you can see the citation check work.
3. **Pilot with the real model.** `python runner/llm_runner.py run --pilot --conditions A0 A3 --repeats 1`. Saved in `runs_pilot/`. Use it to check length, formatting, cost and logging. Pilot runs are not study data.
4. **Freeze.** When the team has agreed the prompt, context, evidence and settings: finalize the files (rename away from DRAFT), update `prompt_version`, set `"frozen": true`.
5. **Formal batch.** `python runner/llm_runner.py run --formal`. This is 5 conditions x 3 repeats, in random order (seed recorded). It is refused unless frozen, the model is set, the version is not DRAFT, and no evidence package is a placeholder.
6. **Check citations.** `python runner/llm_runner.py check --mode formal` lists any evidence ID the model cited that was not in its input.
7. **Review sheet.** `python runner/llm_runner.py review-sheet --mode formal` writes a blind sheet (random codes, no condition or run labels, with the packet's 0-2 scoring columns) and a separate key file. Do not give the key to reviewers.

## What gets saved for every run

In `runs*/<run_id>/`: `input.json` and `input.txt` (exact text sent), `response_raw.json`, `output.json` (parsed), `output.md` (the same output formatted for reading, headings are the JSON keys; `python runner/llm_runner.py render-md --mode pilot` rewrites it for saved runs), `run.json`. In `run_log.csv`: UTC time, model requested and model returned, reasoning effort, max output tokens, prompt version, hashes of the input, context and evidence, token usage, status, retry count, error, number of hypotheses, unknown cited IDs, and cost (if you fill in `pricing_usd_per_million_tokens`).

## Rules built in (from the starter packet)

- Identical context and system prompt in every condition. A package is never shortened in A4.
- No browsing or retrieval; the prompt tells the model to use only what it is given and to cite IDs.
- One logged retry for transport errors only; other errors are recorded, not retried.
- A hypothesis count above the limit, or missing fields, is flagged in the status. Fewer than three hypotheses is accepted.
- Failed or incomplete runs stay in the log.

## Known limits and assumptions

- The OpenAI call uses the Responses API with a JSON-schema output format and a reasoning-effort setting. With `gpt-6-astra` the API accepted reasoning effort low, medium and high and the JSON schema, and the pilot completed. If a different model fails, check the error in `runs_pilot/run_log.csv`; settings you may need to change are `use_json_schema` and `reasoning_effort` in `config.json`.
- Model access depends on each person's API key. Prices are not set in `config.json`, so cost is not logged.
- The shared context is built only from the packet text. Its CTX facts are drafts and are not yet verified against the sources.
- A3 evidence is computed from the 12 AlphaFold jobs (`../structure_prediction/af3_results/`). Draft position map; unchecked by a second person.
- The study measures how reliable and context-sensitive the model's suggestions look to reviewers. It does not show that any experiment works in a lab.
