#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config"
INSTRUCTIONS = ROOT / "instructions"
PROFILE = ROOT / "profile" / "README.md"
TELEGRAM_URL = "https://t.me/GPTsAgentChat"

EXPECTED_CONFIG_FILES = [
    "ACTIONS-API-BLUEPRINT.md",
    "AGENTS.md",
    "ARTIFACT-CONTRACT.md",
    "CAPABILITIES-MAP.md",
    "EVALUATION-CHECKLIST.md",
    "EXAMPLES.md",
    "FILE-WORKFLOW.md",
    "GPT-BUILDER-CONFIG.md",
    "LIMITATIONS-AND-DISCLAIMERS.md",
    "MANIFEST.md",
    "PROMPT-LIBRARY.md",
    "PUBLISHING-GPT-STORE.md",
    "README.md",
    "REPORT-TEMPLATES.md",
    "SAFETY-REFUSAL-POLICY.md",
    "SANDBOX.md",
    "SECRET-HYGIENE.md",
    "USER-ONBOARDING.md",
    "VERSIONING-ROADMAP.md",
    "ZIP-SAFETY-POLICY.md",
]

SECRET_PATTERNS = {
    "OpenAI key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    "Slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
}

COMMUNITY_FILES = [
    Path("CONTRIBUTING.md"),
    Path("SUPPORT.md"),
    Path("docs/CONTRIBUTOR-WORKFLOW.md"),
    Path("docs/COMMUNITY-PLAYBOOK.md"),
    Path("docs/ROADMAP.md"),
    Path(".github/ISSUE_TEMPLATE/community_idea.yml"),
    Path(".github/labels.json"),
]

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "dist", ".release"}
SKIP_SUFFIXES = {".zip", ".pyc", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf"}
ALLOW_FILES = {Path(".env"), Path(".env.example")}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(condition: bool, label: str, detail: str = "") -> tuple[bool, str]:
    status = "PASS" if condition else "FAILED"
    suffix = f" - {detail}" if detail else ""
    return condition, f"{status}: {label}{suffix}"


def extract_instruction_block() -> str | None:
    text = read(CONFIG / "GPT-BUILDER-CONFIG.md")
    match = re.search(
        r"## Ready-to-Copy Instructions Block\n\n```text\n(.*?)\n```",
        text,
        re.S,
    )
    if not match:
        return None
    return match.group(1).rstrip() + "\n"


def scan_secrets() -> list[str]:
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel in ALLOW_FILES:
            continue
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for name, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                hits.append(f"{rel}:{line}: {name}")
    return hits


def load_label_names() -> set[str]:
    labels_path = ROOT / ".github" / "labels.json"
    labels = json.loads(read(labels_path))
    return {item["name"] for item in labels if isinstance(item, dict) and "name" in item}


def labels_from_issue_template(path: Path) -> set[str]:
    labels: set[str] = set()
    lines = read(path).splitlines()
    in_labels = False
    labels_indent = 0
    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if re.match(r"^labels:\s*$", stripped):
            in_labels = True
            labels_indent = indent
            continue
        if in_labels and stripped:
            if indent <= labels_indent:
                in_labels = False
            elif stripped.startswith("- "):
                labels.add(stripped[2:].strip().strip("'\""))
    return labels


def scan_undefined_issue_labels() -> list[str]:
    label_names = load_label_names()
    hits: list[str] = []
    for path in sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml")):
        for label in sorted(labels_from_issue_template(path)):
            if label not in label_names:
                hits.append(f"{path.relative_to(ROOT)}: {label}")
    return hits


def scan_private_path_references() -> list[str]:
    private_patterns = [
        re.compile(r"/home/[A-Za-z0-9._-]+(?:/|$)"),
        re.compile("token" + "_github", re.I),
    ]
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for pattern in private_patterns:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                hits.append(f"{rel}:{line}")
    return hits


def main() -> int:
    config_files = sorted(path.name for path in CONFIG.glob("*.md") if path.is_file())
    instruction_block = extract_instruction_block()
    system_instructions = INSTRUCTIONS / "SYSTEM-INSTRUCTIONS.txt"
    instructions_md = INSTRUCTIONS / "INSTRUCTIONS.md"
    profile_text = read(PROFILE) if PROFILE.exists() else ""
    secret_hits = scan_secrets()
    community_missing = [str(path) for path in COMMUNITY_FILES if not (ROOT / path).exists()]
    community_text = "\n".join(read(ROOT / path) for path in COMMUNITY_FILES if (ROOT / path).exists())
    undefined_labels = scan_undefined_issue_labels()
    private_path_hits = scan_private_path_references()

    checks = [
        check(CONFIG.exists(), "config directory exists"),
        check(config_files == EXPECTED_CONFIG_FILES, "config has exactly the expected 20 Markdown files", f"found {len(config_files)}"),
        check(instruction_block is not None, "GPT-BUILDER-CONFIG.md contains a ready-to-copy Instructions block"),
        check(system_instructions.exists(), "SYSTEM-INSTRUCTIONS.txt exists"),
        check(
            instruction_block is not None and system_instructions.exists() and read(system_instructions) == instruction_block,
            "SYSTEM-INSTRUCTIONS.txt matches GPT-BUILDER-CONFIG.md",
        ),
        check(
            instruction_block is not None and instructions_md.exists() and instruction_block.strip() in read(instructions_md),
            "INSTRUCTIONS.md contains the canonical Instructions block",
        ),
        check(PROFILE.exists(), "profile README exists"),
        check("GPTsAgent" in profile_text and "Sandbox File Operator" in profile_text, "profile README names GPTsAgent and Sandbox File Operator"),
        check(not community_missing, "community contributor files exist", ", ".join(community_missing)),
        check(TELEGRAM_URL in community_text and "Contribution Idea" in community_text, "community path names Telegram and Contribution Idea workflow"),
        check(not undefined_labels, "issue-template labels are defined in .github/labels.json", "; ".join(undefined_labels)),
        check(not private_path_hits, "no private host paths or token-file references were found", "; ".join(private_path_hits[:10])),
        check(not secret_hits, "no obvious secret-like tokens were found", "; ".join(secret_hits[:10])),
    ]

    print("# GPTsAgent Workspace Validation")
    print("")
    ok = True
    for passed, line in checks:
        print(line)
        ok = ok and passed

    print("")
    print("Status: PASS" if ok else "Status: FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
