"""Verify sequence artifacts and runner integration without model/API calls."""
from pathlib import Path
import csv, hashlib, importlib.util, json
ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'sequence_analysis'
checks = json.loads((HERE / 'evidence/output_checksums.json').read_text())
for path, expected in checks.items():
    assert hashlib.sha256((HERE / 'evidence' / path).read_bytes()).hexdigest() == expected, path
spec = importlib.util.spec_from_file_location('ada2_runner', ROOT / 'llm_runner/runner/llm_runner.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
cfg = runner.load_config()
for label, passed, detail in runner.consistency_checks(cfg):
    assert passed, (label, detail)
assert not runner.build_prompt(cfg, 'A1')['placeholders']
logs = list(csv.DictReader((ROOT / 'llm_runner/runs/run_log.csv').open()))
for row in logs:
    if row['condition'] in ('A0', 'A3'):
        assert runner.build_prompt(cfg, row['condition'])['input_sha256'] == row['input_sha256'], row['run_id']
with (HERE / 'evidence/tables/Human_Pig_Residue_Correspondence.csv').open() as f:
    official = {r['human_position']: r for r in csv.DictReader(f) if r['human_position']}
with (ROOT / 'structure_prediction/human_pig_position_map_DRAFT.csv').open() as f:
    differences = [r['human_pos'] for r in csv.DictReader(f) if r['human_pos'] and r['pig_pos'] != official[r['human_pos']]['pig_position']]
expected = json.loads((HERE / 'integration/integration_audit.json').read_text())['mapping_discrepancy_positions']
assert differences == expected, (differences, expected)
print(f'PASS: {len(checks)} cloud artifact hashes, runner consistency, A1 availability, archived A0/A3 input hashes and draft-map reconciliation.')
print('A4 remaining placeholders:', runner.build_prompt(cfg, 'A4')['placeholders'])
print('No LLM calls or scientific rerun performed.')
