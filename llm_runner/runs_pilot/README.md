# Pilot runs

Rehearsal runs of the LLM experiment are saved here. They are not study data and must not be counted in the study.

This folder is currently empty of runs. The earlier A0 and A3 pilots were deleted before the formal runs. Formal runs are saved in `../runs/`.

Create a pilot with `python runner/llm_runner.py run --pilot --conditions A0 A3 --repeats 1`, or with `RUN_PILOT = True` in `LLM_runner.ipynb`. Each run gets its own folder (`input.txt`, `input.json`, `output.md`, `output.json`, `response_raw.json`, `run.json`). `run_log.csv` has one row per run.
