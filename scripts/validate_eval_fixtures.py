#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "eval" / "preview-scenarios.jsonl"
ALLOWED_STATUSES = {"PASS", "PARTIAL", "FAILED", "SKIPPED", "NOT RUN", "NOT VERIFIED", "TIMEOUT"}
REQUIRED_FIELDS = {
    "id",
    "category",
    "critical",
    "prompt",
    "expected_status",
    "must_include",
    "must_not_include",
}
REQUIRED_CATEGORIES = {
    "boundary",
    "archive",
    "injection",
    "secret-hygiene",
    "actions",
    "apps",
    "artifact",
    "builder",
    "recovery",
    "safety",
    "testing",
    "validation",
    "reference-distillation",
    "model-selection",
}


def fail(message: str) -> int:
    print(f"FAILED: {message}")
    return 1


def main() -> int:
    if not SCENARIOS.exists():
        return fail(f"{SCENARIOS.relative_to(ROOT)} does not exist")

    ids: set[str] = set()
    categories: set[str] = set()
    critical_count = 0
    total = 0

    for line_no, line in enumerate(SCENARIOS.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            return fail(f"blank line at {SCENARIOS.relative_to(ROOT)}:{line_no}")
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            return fail(f"invalid JSON at line {line_no}: {exc}")

        missing = sorted(REQUIRED_FIELDS.difference(item))
        if missing:
            return fail(f"line {line_no} missing fields: {', '.join(missing)}")

        scenario_id = item["id"]
        if not isinstance(scenario_id, str) or not scenario_id:
            return fail(f"line {line_no} has invalid id")
        if scenario_id in ids:
            return fail(f"duplicate id: {scenario_id}")
        ids.add(scenario_id)

        category = item["category"]
        if not isinstance(category, str) or not category:
            return fail(f"line {line_no} has invalid category")
        categories.add(category)

        if item["expected_status"] not in ALLOWED_STATUSES:
            return fail(f"line {line_no} has unsupported status: {item['expected_status']}")
        if not isinstance(item["critical"], bool):
            return fail(f"line {line_no} critical must be boolean")
        if item["critical"]:
            critical_count += 1
        for field in ("must_include", "must_not_include"):
            value = item[field]
            if not isinstance(value, list) or not all(isinstance(entry, str) and entry for entry in value):
                return fail(f"line {line_no} {field} must be a non-empty string list")
        if not isinstance(item["prompt"], str) or len(item["prompt"].strip()) < 20:
            return fail(f"line {line_no} prompt is too short")
        total += 1

    missing_categories = sorted(REQUIRED_CATEGORIES.difference(categories))
    if missing_categories:
        return fail(f"missing categories: {', '.join(missing_categories)}")
    if total < 10:
        return fail("need at least 10 preview scenarios")
    if critical_count < 7:
        return fail("need at least 7 critical scenarios")

    print("# GPTsAgent Eval Fixture Validation")
    print(f"Scenarios: {total}")
    print(f"Critical: {critical_count}")
    print(f"Categories: {', '.join(sorted(categories))}")
    print("Status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
