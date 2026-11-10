"""Repeatable runner for the five LLM conditions (A0-A4) of the ADA2 project.

Usage (from the llm_runner folder):
  python runner/llm_runner.py dry-run                        # build all prompts, run consistency checks, no API call
  python runner/llm_runner.py preview A3                     # print the exact text sent for one condition
  python runner/llm_runner.py run --conditions A0 A3 --repeats 1 --pilot      # rehearsal, saved in runs_pilot/
  python runner/llm_runner.py run --conditions A0 A1 A2 A3 A4 --formal        # formal batch (needs frozen config)
  python runner/llm_runner.py run --mock --pilot             # full pipeline with a fake model, no API call, no cost
  python runner/llm_runner.py check --mode pilot             # flag cited IDs that were never provided
  python runner/llm_runner.py render-md --mode pilot         # (re)write a readable output.md for every saved run
  python runner/llm_runner.py review-sheet --mode formal     # blind review sheet + separate key file

The OpenAI API key is read from the OPENAI_API_KEY environment variable (a .env file is used if python-dotenv is installed).
Every run saves: exact input, raw response, parsed output, and a row in run_log.csv (model, settings, UTC time, input hash,
prompt version, token usage, status, retries, cost if pricing is set).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # llm_runner/
ID_RE = re.compile(r"\b(?:CTX|SEQ|SURF|STRUCT)-\d{2,3}\b")
LOG_FIELDS = ["run_id", "mode", "condition", "repeat", "started_utc", "finished_utc", "model_requested", "model_returned",
              "reasoning_effort", "max_output_tokens", "prompt_version", "input_sha256", "context_sha256", "evidence_sha256",
              "input_chars", "input_tokens", "output_tokens", "reasoning_tokens", "status", "incomplete_reason",
              "retry_count", "error", "n_hypotheses", "unknown_ids", "cost_usd", "run_dir"]


# ----------------------------------------------------------------------------- helpers
def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_config(path: str | Path | None = None) -> dict:
    path = Path(path) if path else ROOT / "config.json"
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)
    cfg["_path"] = str(path)
    return cfg


def read_text(rel: str) -> str:
    """Read a text file; internal 'STATUS:' draft banners are dropped so they are never sent to the model."""
    lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    return "\n".join(ln for ln in lines if not ln.strip().lower().startswith("status:")).strip()


def is_placeholder(text: str) -> bool:
    first = next((ln for ln in text.splitlines() if ln.strip()), "")
    return first.strip().upper().startswith("PLACEHOLDER")


def runs_dir(mode: str) -> Path:
    d = ROOT / {"formal": "runs", "pilot": "runs_pilot", "mock": "runs_mock"}[mode]
    d.mkdir(exist_ok=True)
    return d


# ----------------------------------------------------------------------------- prompt building
def build_prompt(cfg: dict, condition: str) -> dict:
    """Return the exact system and user text for one condition, plus hashes and the placeholder status of its packages."""
    if condition not in cfg["conditions"]:
        raise KeyError(f"Unknown condition {condition}")
    system = read_text(cfg["files"]["system_prompt"])
    context = read_text(cfg["files"]["shared_context"])
    packages, placeholders = [], []
    for key in cfg["conditions"][condition]:
        text = read_text(cfg["evidence_files"][key])
        if is_placeholder(text):
            placeholders.append(key)
        packages.append(text)
    evidence = "\n\n".join(packages) if packages else "No computational evidence is provided for this task."
    task = read_text(cfg["files"]["task_prompt"])
    user = (task.replace("{{CONTEXT}}", context).replace("{{EVIDENCE}}", evidence)
            .replace("{{MAX_HYPOTHESES}}", str(cfg["max_hypotheses"])))
    return dict(condition=condition, system=system, user=user, context=context, evidence=evidence, packages=packages,
                placeholders=placeholders, input_sha256=sha(system + "\n\n" + user), context_sha256=sha(context),
                evidence_sha256=sha(evidence), input_chars=len(system) + len(user),
                available_ids=sorted(set(ID_RE.findall(user))))


def consistency_checks(cfg: dict) -> list[tuple[str, bool, str]]:
    """Checks the packet asks for: identical context everywhere; each package unchanged inside the combined condition."""
    out = []
    prompts = {c: build_prompt(cfg, c) for c in cfg["conditions"]}
    ctx = {p["context_sha256"] for p in prompts.values()}
    out.append(("Identical shared context in all conditions", len(ctx) == 1, f"{len(ctx)} distinct context hash(es)"))
    sys_h = {sha(p["system"]) for p in prompts.values()}
    out.append(("Identical system prompt in all conditions", len(sys_h) == 1, f"{len(sys_h)} distinct hash(es)"))
    allc = [c for c, keys in cfg["conditions"].items() if len(keys) > 1]
    for c in allc:
        for key in cfg["conditions"][c]:
            text = read_text(cfg["evidence_files"][key])
            out.append((f"{key} package appears unchanged in {c}", text in prompts[c]["user"], "verbatim substring check"))
    for c, p in prompts.items():
        lim = cfg.get("max_input_tokens_warning")
        est = p["input_chars"] // 4
        out.append((f"{c} input size (~{est} tokens by chars/4)", (lim is None) or est <= lim, f"limit {lim}"))
    return out


# ----------------------------------------------------------------------------- output validation
def strip_unsupported(schema: dict) -> dict:
    """Remove keywords some structured-output endpoints reject; limits are re-checked in validate_output()."""
    if isinstance(schema, dict):
        return {k: strip_unsupported(v) for k, v in schema.items() if k not in ("maxItems", "minItems")}
    if isinstance(schema, list):
        return [strip_unsupported(v) for v in schema]
    return schema


def validate_output(obj: dict, schema: dict, max_h: int) -> list[str]:
    problems = []
    if not isinstance(obj, dict) or "hypotheses" not in obj:
        return ["missing 'hypotheses'"]
    hs = obj["hypotheses"]
    if not isinstance(hs, list):
        return ["'hypotheses' is not a list"]
    if len(hs) > max_h:
        problems.append(f"{len(hs)} hypotheses (max {max_h})")
    req = schema["properties"]["hypotheses"]["items"]["required"]
    for i, h in enumerate(hs):
        miss = [k for k in req if k not in h]
        if miss:
            problems.append(f"hypothesis {i + 1} missing {miss}")
    return problems


def cited_ids(h: dict) -> list[str]:
    ids = list(h.get("supporting_evidence_ids", [])) + list(h.get("conflicting_evidence_ids", []))
    for k in ("evidence_notes", "added_value_from_computation"):
        ids += ID_RE.findall(str(h.get(k, "")))
    return sorted({i.strip() for i in ids})


# ----------------------------------------------------------------------------- model calls
class MockClient:
    """Offline stand-in used to test the pipeline. It cites one real ID and one invented ID on purpose."""

    class _Resp:
        def __init__(self, text, model):
            self.output_text, self.model, self.status, self.incomplete_details = text, model, "completed", None
            self.usage = type("U", (), {"input_tokens": 1000, "output_tokens": 400,
                                        "output_tokens_details": type("D", (), {"reasoning_tokens": 100})()})()
            self._d = {"mock": True, "output_text": text}

        def model_dump(self):
            return self._d

    def __init__(self, ids):
        self.ids = ids
        self.responses = self

    def create(self, **kw):
        real = self.ids[0] if self.ids else "CTX-01"
        h = {k: "mock" for k in ["title", "question_and_explanation", "evidence_notes", "alternative_explanation", "proposed_test",
                                  "predicted_outcome_if_true", "falsifying_outcome", "controls_and_feasibility", "next_decision",
                                  "added_value_from_computation"]}
        h.update(supporting_evidence_ids=[real, "STRUCT-99"], conflicting_evidence_ids=[], confidence="low")
        return self._Resp(json.dumps({"hypotheses": [h], "overall_note": "mock run"}), "mock-model")


def get_client():
    try:
        from dotenv import load_dotenv  # optional
        load_dotenv()
    except Exception:
        pass
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set. Put it in your environment or in a .env file.")
    from openai import OpenAI
    return OpenAI()


def call_model(client, cfg: dict, system: str, user: str, schema: dict):
    kwargs = dict(model=cfg["model"], input=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                  max_output_tokens=cfg["max_output_tokens"])
    if cfg.get("reasoning_effort"):
        kwargs["reasoning"] = {"effort": cfg["reasoning_effort"]}
    if cfg.get("use_json_schema", True):
        kwargs["text"] = {"format": {"type": "json_schema", "name": "ada2_hypotheses", "schema": strip_unsupported(schema), "strict": True}}
    return client.responses.create(**kwargs)


def _transport_errors():
    try:
        import openai
        return (openai.APIConnectionError, openai.APITimeoutError, openai.RateLimitError, openai.InternalServerError)
    except Exception:
        return (ConnectionError, TimeoutError)


# ----------------------------------------------------------------------------- one run
def run_one(client, cfg: dict, condition: str, repeat: int, mode: str, schema: dict, order_index: int = 0) -> dict:
    p = build_prompt(cfg, condition)
    rid = f"{mode}_{condition}_r{repeat}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{order_index:02d}_{uuid.uuid4().hex[:4]}"
    d = runs_dir(mode) / rid
    d.mkdir(parents=True, exist_ok=False)
    (d / "input.json").write_text(json.dumps({"system": p["system"], "user": p["user"]}, indent=1), encoding="utf-8")
    (d / "input.txt").write_text("### SYSTEM\n" + p["system"] + "\n\n### USER\n" + p["user"], encoding="utf-8")
    row = dict(run_id=rid, mode=mode, condition=condition, repeat=repeat, started_utc=utc_now(), model_requested=cfg["model"],
               reasoning_effort=cfg.get("reasoning_effort"), max_output_tokens=cfg["max_output_tokens"], prompt_version=cfg["prompt_version"],
               input_sha256=p["input_sha256"], context_sha256=p["context_sha256"], evidence_sha256=p["evidence_sha256"],
               input_chars=p["input_chars"], retry_count=0, status="error", run_dir=str(d.relative_to(ROOT)))
    resp, err = None, ""
    for attempt in range(cfg.get("retry_on_transport_error", 1) + 1):
        try:
            resp = call_model(client, cfg, p["system"], p["user"], schema)
            err = ""
            break
        except _transport_errors() as e:           # one logged retry for transport problems only
            err, row["retry_count"] = f"{type(e).__name__}: {e}", attempt + 1
            time.sleep(5)
        except Exception as e:                       # anything else is recorded, not retried
            err = f"{type(e).__name__}: {e}"
            break
    row["finished_utc"], row["error"] = utc_now(), err[:500]
    if resp is not None:
        usage = getattr(resp, "usage", None)
        row["model_returned"] = getattr(resp, "model", None)
        row["input_tokens"] = getattr(usage, "input_tokens", None)
        row["output_tokens"] = getattr(usage, "output_tokens", None)
        det = getattr(usage, "output_tokens_details", None)
        row["reasoning_tokens"] = getattr(det, "reasoning_tokens", None)
        inc = getattr(resp, "incomplete_details", None)
        row["incomplete_reason"] = getattr(inc, "reason", None) if inc else None
        (d / "response_raw.json").write_text(json.dumps(resp.model_dump(), indent=1, default=str), encoding="utf-8")
        text = getattr(resp, "output_text", "") or ""
        row["status"] = "completed" if getattr(resp, "status", "") == "completed" else "incomplete"
        try:
            obj = json.loads(text)
            probs = validate_output(obj, schema, cfg["max_hypotheses"])
            (d / "output.json").write_text(json.dumps(obj, indent=1), encoding="utf-8")
            hs = obj.get("hypotheses", [])
            row["n_hypotheses"] = len(hs)
            unknown = sorted({i for h in hs for i in cited_ids(h)} - set(p["available_ids"]))
            row["unknown_ids"] = ";".join(unknown)
            if probs:
                row["status"] = "format_problem: " + "; ".join(probs)
        except json.JSONDecodeError:
            (d / "output_unparsed.txt").write_text(text, encoding="utf-8")
            row["status"] = "parse_error"
    pr = cfg.get("pricing_usd_per_million_tokens") or {}
    if pr.get("input") is not None and pr.get("output") is not None and row.get("input_tokens") is not None:
        row["cost_usd"] = round(row["input_tokens"] * pr["input"] / 1e6 + (row.get("output_tokens") or 0) * pr["output"] / 1e6, 4)
    (d / "run.json").write_text(json.dumps(row, indent=1, default=str), encoding="utf-8")
    write_output_md(d)
    log = runs_dir(mode) / "run_log.csv"
    new = not log.exists()
    with open(log, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow(row)
    return row


def formal_guards(cfg: dict, conditions: list[str], allow_draft: bool) -> list[str]:
    errs = []
    if not cfg.get("frozen"):
        errs.append("config.json: 'frozen' is false. Freeze only after the team agrees the prompt, context, evidence and settings.")
    if cfg["model"].startswith("REPLACE"):
        errs.append("config.json: set 'model' to a real model ID.")
    if "DRAFT" in cfg["prompt_version"] and not allow_draft:
        errs.append("prompt_version still says DRAFT (use --allow-draft only if you know why).")
    for c in conditions:
        ph = build_prompt(cfg, c)["placeholders"]
        if ph:
            errs.append(f"{c}: evidence package(s) still PLACEHOLDER: {ph}")
    return errs


def run_batch(cfg: dict, conditions: list[str], repeats: int, mode: str, mock: bool = False, allow_draft: bool = False) -> list[dict]:
    if mode == "formal":
        errs = formal_guards(cfg, conditions, allow_draft)
        if errs:
            raise SystemExit("Formal run refused:\n - " + "\n - ".join(errs))
    else:
        if not mock and cfg["model"].startswith("REPLACE"):
            raise SystemExit("config.json: set 'model' to a real model ID (or use --mock).")
        for c in conditions:                         # pilots may run with placeholders, but say so
            ph = build_prompt(cfg, c)["placeholders"]
            if ph:
                print(f"note: {c} includes PLACEHOLDER package(s) {ph}; this is only a rehearsal")
    rows = []
    if mock:
        mode = "mock"
    schema = json.loads(read_text(cfg["files"]["output_schema"]))
    plan = [(c, r) for c in conditions for r in range(1, repeats + 1)]
    random.Random(cfg.get("shuffle_seed", 0)).shuffle(plan)    # randomised execution order, seed recorded
    (runs_dir(mode) / f"plan_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}.json").write_text(
        json.dumps({"seed": cfg.get("shuffle_seed"), "order": plan, "config": {k: v for k, v in cfg.items() if not k.startswith("_")}}, indent=1))
    client = MockClient(build_prompt(cfg, conditions[0])["available_ids"]) if mock else get_client()
    for i, (c, r) in enumerate(plan):
        print(f"[{i + 1}/{len(plan)}] {c} repeat {r} ...", end=" ", flush=True)
        row = run_one(client, cfg, c, r, "mock" if mock else mode, schema, i)
        print(row["status"], f"(unknown IDs: {row.get('unknown_ids') or 'none'})")
        rows.append(row)
    return rows


# ----------------------------------------------------------------------------- post-run tools
def _md_value(v) -> str:
    if isinstance(v, list):
        return "\n".join(f"- {x}" for x in v) if v else "_(none)_"
    return str(v).strip() or "_(empty)_"


def _input_summary(inp: dict, meta: dict) -> list[str]:
    """Short description of what the model was given, read from the saved input.json."""
    user = inp.get("user", "")
    by_prefix = {}
    for i in sorted(set(ID_RE.findall(user))):
        by_prefix.setdefault(i.split("-")[0], []).append(i)
    names = {"CTX": "background / literature records (shared by all conditions)", "SEQ": "sequence evidence",
             "SURF": "surface evidence", "STRUCT": "structure evidence"}
    lines = ["## context_provided_to_model", ""]
    lines += [f"- condition: {meta.get('condition', 'unknown')}",
              f"- prompt version: {meta.get('prompt_version', 'unknown')}"]
    for pre in ("CTX", "SEQ", "SURF", "STRUCT"):
        if pre in by_prefix:
            ids = by_prefix[pre]
            lines.append(f"- {names[pre]}: {ids[0]} to {ids[-1]} ({len(ids)} records)" if len(ids) > 1 else f"- {names[pre]}: {ids[0]}")
    if not any(p in by_prefix for p in ("SEQ", "SURF", "STRUCT")):
        lines.append("- computational evidence: none")
    for k, label in (("input_sha256", "full input"), ("context_sha256", "shared context"), ("evidence_sha256", "evidence")):
        if meta.get(k):
            lines.append(f"- {label} hash (sha256, first 12): {meta[k][:12]}")
    lines += ["", "The exact text sent to the model (also saved as `input.txt`):", ""]
    for title, key in (("system prompt", "system"), ("user message (task, background information and evidence)", "user")):
        lines += [f"<details><summary>{title}</summary>", "", "~~~~~~text", inp.get(key, "").strip(), "~~~~~~", "", "</details>", ""]
    return lines


def output_to_markdown(obj: dict, meta: dict | None = None, inp: dict | None = None) -> str:
    """Readable copy of output.json. Headings are the JSON keys, in the order they appear in the file.
    If the saved input is given, a final section lists the context the model was provided."""
    meta = meta or {}
    lines = [f"# {meta.get('run_id', 'output')}", ""]
    info = [f"{k}: {meta[k]}" for k in ("condition", "model_returned", "reasoning_effort", "prompt_version", "status") if meta.get(k)]
    if info:
        lines += ["  \n".join(info), ""]
    for key, val in obj.items():
        lines += [f"## {key}", ""]
        if key == "hypotheses" and isinstance(val, list):
            for i, h in enumerate(val, 1):
                lines += [f"### hypotheses[{i}]", ""]
                for k, v in h.items():
                    lines += [f"#### {k}", "", _md_value(v), ""]
        else:
            lines += [_md_value(val), ""]
    if inp:
        lines += _input_summary(inp, meta)
    return "\n".join(lines).rstrip() + "\n"


def write_output_md(run_dir: Path) -> Path | None:
    """Write output.md next to output.json (and run.json, if present) in one run folder."""
    run_dir = Path(run_dir)
    if not (run_dir / "output.json").exists():
        return None
    obj = json.loads((run_dir / "output.json").read_text(encoding="utf-8"))
    meta = json.loads((run_dir / "run.json").read_text(encoding="utf-8")) if (run_dir / "run.json").exists() else {}
    inp = json.loads((run_dir / "input.json").read_text(encoding="utf-8")) if (run_dir / "input.json").exists() else None
    out = run_dir / "output.md"
    out.write_text(output_to_markdown(obj, meta, inp), encoding="utf-8")
    return out


def load_runs(mode: str) -> list[dict]:
    out = []
    for d in sorted(runs_dir(mode).glob("*/")):
        if (d / "output.json").exists():
            meta = json.loads((d / "run.json").read_text(encoding="utf-8"))
            out.append(dict(meta=meta, output=json.loads((d / "output.json").read_text(encoding="utf-8")), dir=d))
    return out


def citation_report(mode: str) -> list[dict]:
    rows = []
    for r in load_runs(mode):
        avail = set(ID_RE.findall(json.loads((r["dir"] / "input.json").read_text(encoding="utf-8"))["user"]))
        for i, h in enumerate(r["output"].get("hypotheses", []), 1):
            ids = cited_ids(h)
            rows.append(dict(run_id=r["meta"]["run_id"], condition=r["meta"]["condition"], hypothesis=i, cited_ids=";".join(ids),
                             unknown_ids=";".join(sorted(set(ids) - avail)), n_cited=len(ids), title=h.get("title", "")))
    return rows


def review_sheet(mode: str, seed: int = 1) -> tuple[Path, Path]:
    """Blind review sheet (no condition, run or model labels) and a separate key that links codes back to runs."""
    items = []
    for r in load_runs(mode):
        for i, h in enumerate(r["output"].get("hypotheses", []), 1):
            items.append((r, i, h))
    random.Random(seed).shuffle(items)
    out = runs_dir(mode)
    sheet, key = out / f"review_sheet_{mode}.csv", out / f"review_key_{mode}_KEEP_SEPARATE.csv"
    fields = ["code", "title", "question_and_explanation", "supporting_evidence_ids", "conflicting_evidence_ids", "evidence_notes",
              "alternative_explanation", "proposed_test", "predicted_outcome_if_true", "falsifying_outcome", "controls_and_feasibility",
              "next_decision", "added_value_from_computation"]
    score_cols = ["score_evidence_accuracy_0_2", "score_specific_explanation_0_2", "score_discriminating_prediction_0_2", "score_feasibility_0_2",
                  "score_decision_value_0_2", "literature_overlap_known_extension_unclear", "comments"]
    with open(sheet, "w", newline="", encoding="utf-8") as fs, open(key, "w", newline="", encoding="utf-8") as fk:
        ws = csv.DictWriter(fs, fieldnames=fields + score_cols)
        wk = csv.DictWriter(fk, fieldnames=["code", "run_id", "condition", "repeat", "hypothesis"])
        ws.writeheader(); wk.writeheader()
        for n, (r, i, h) in enumerate(items, 1):
            code = f"H{n:03d}"
            row = {k: (";".join(h[k]) if isinstance(h.get(k), list) else h.get(k, "")) for k in fields if k != "code"}
            ws.writerow({"code": code, **row})
            wk.writerow(dict(code=code, run_id=r["meta"]["run_id"], condition=r["meta"]["condition"], repeat=r["meta"]["repeat"], hypothesis=i))
    return sheet, key


# ----------------------------------------------------------------------------- CLI
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("dry-run")
    p = sub.add_parser("preview"); p.add_argument("condition")
    r = sub.add_parser("run")
    r.add_argument("--conditions", nargs="+", default=None)
    r.add_argument("--repeats", type=int, default=None)
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--pilot", action="store_true"); g.add_argument("--formal", action="store_true")
    r.add_argument("--mock", action="store_true"); r.add_argument("--allow-draft", action="store_true")
    r.add_argument("--effort", default=None, help="override reasoning effort for this batch (low/medium/high)")
    c = sub.add_parser("check"); c.add_argument("--mode", default="pilot", choices=["pilot", "formal", "mock"])
    m = sub.add_parser("render-md"); m.add_argument("--mode", default="pilot", choices=["pilot", "formal", "mock"])
    s = sub.add_parser("review-sheet"); s.add_argument("--mode", default="formal", choices=["pilot", "formal", "mock"])
    a = ap.parse_args(argv)
    cfg = load_config(a.config)

    if a.cmd == "dry-run":
        for name, ok, note in consistency_checks(cfg):
            print(("PASS " if ok else "FAIL ") + name + f"   [{note}]")
        for c_, keys in cfg["conditions"].items():
            p_ = build_prompt(cfg, c_)
            print(f"{c_}: hash {p_['input_sha256'][:12]}  chars {p_['input_chars']}  IDs {len(p_['available_ids'])}  placeholders {p_['placeholders'] or 'none'}")
    elif a.cmd == "preview":
        p_ = build_prompt(cfg, a.condition)
        print("### SYSTEM\n" + p_["system"] + "\n\n### USER\n" + p_["user"])
    elif a.cmd == "run":
        if a.effort:
            cfg["reasoning_effort"] = a.effort
        conds = a.conditions or list(cfg["conditions"])
        reps = a.repeats or (1 if a.pilot else cfg["repeats"])
        mode = "pilot" if a.pilot else "formal"
        rows = run_batch(cfg, conds, reps, mode, mock=a.mock, allow_draft=a.allow_draft)
        print(f"done: {len(rows)} runs; log: {runs_dir(rows[0]['mode']) / 'run_log.csv'}")
    elif a.cmd == "check":
        rows = citation_report(a.mode)
        bad = [x for x in rows if x["unknown_ids"]]
        for x in rows:
            print(x["run_id"], "H" + str(x["hypothesis"]), "cited:", x["cited_ids"] or "none", "| UNKNOWN:" if x["unknown_ids"] else "", x["unknown_ids"])
        print(f"{len(rows)} hypotheses checked; {len(bad)} cite IDs that were never provided")
    elif a.cmd == "render-md":
        n = 0
        for d in sorted(runs_dir(a.mode).glob("*/")):
            if write_output_md(d):
                n += 1
        print(f"wrote output.md for {n} run(s) in {runs_dir(a.mode).name}/")
    elif a.cmd == "review-sheet":
        sheet, key = review_sheet(a.mode)
        print("review sheet:", sheet, "\nkey (do not share with reviewers):", key)


if __name__ == "__main__":
    main()
