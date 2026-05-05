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
README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
CONFIG_README = CONFIG / "README.md"
EVAL_SCENARIOS = ROOT / "eval" / "preview-scenarios.jsonl"
TELEGRAM_URL = "https://t.me/GPTsAgentChat"
EXPECTED_VERSION = "v0.2.0"

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
    "OpenAI key": re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}(?![A-Za-z0-9_-])"),
    "AWS access key": re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----"),
    "Slack token": re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{20,}(?![A-Za-z0-9-])"),
    "GitHub token": re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9_]{30,}(?![A-Za-z0-9_])"),
}

COMMUNITY_FILES = [
    Path("AGENTS.md"),
    Path("CONTRIBUTING.md"),
    Path("SUPPORT.md"),
    Path("docs/BOUNDARY-AND-STATE-CONTRACT.md"),
    Path("docs/AGENT-OPERATING-PATTERNS.md"),
    Path("docs/CONTRIBUTOR-WORKFLOW.md"),
    Path("docs/COMMUNITY-PLAYBOOK.md"),
    Path("docs/OFFICIAL-DOCS-BASIS.md"),
    Path("docs/MODEL-SELECTION.md"),
    Path("docs/PILOT-LAUNCH-CHECKLIST.md"),
    Path("docs/PREVIEW-TEST-MATRIX.md"),
    Path("docs/REFERENCE-DISTILLATION-POLICY.md"),
    Path("docs/ROADMAP.md"),
    Path("docs/THREAT-MODEL.md"),
    Path("eval/preview-scenarios.jsonl"),
    Path("scripts/check_open_prs.py"),
    Path("scripts/validate_eval_fixtures.py"),
    Path("scripts/validate_release_artifacts.py"),
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
        re.compile("Capsule" + "OS", re.I),
        re.compile(r"(?<![A-Za-z0-9])" + "N" + r"1(?![A-Za-z0-9])"),
        re.compile("number1" + "projects", re.I),
        re.compile("Aps" + "ny", re.I),
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


def scan_legacy_version_references() -> list[str]:
    patterns = [
        re.compile(r"\bv4\.1\b"),
        re.compile(r"\bv4\.1\.0\b"),
        re.compile(r"\bv4\.0\.0\b"),
        re.compile(r"\bv5\."),
        re.compile(r"\bv0\.0\.1\b"),
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
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                hits.append(f"{rel}:{line}: {match.group(0)}")
                break
    return hits


def extract_version(path: Path) -> str | None:
    text = read(path)
    match = re.search(r"^Version:\s*`([^`]+)`", text, re.M)
    if match:
        return match.group(1)
    return None


def load_eval_scenarios() -> tuple[list[dict], list[str]]:
    errors: list[str] = []
    scenarios: list[dict] = []
    if not EVAL_SCENARIOS.exists():
        return scenarios, [f"{EVAL_SCENARIOS.relative_to(ROOT)} missing"]
    for line_no, line in enumerate(read(EVAL_SCENARIOS).splitlines(), start=1):
        if not line.strip():
            errors.append(f"blank line {line_no}")
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: {exc}")
            continue
        if isinstance(item, dict):
            scenarios.append(item)
        else:
            errors.append(f"line {line_no}: not an object")
    return scenarios, errors


def main() -> int:
    config_files = sorted(path.name for path in CONFIG.glob("*.md") if path.is_file())
    instruction_block = extract_instruction_block()
    system_instructions = INSTRUCTIONS / "SYSTEM-INSTRUCTIONS.txt"
    instructions_md = INSTRUCTIONS / "INSTRUCTIONS.md"
    builder_config = CONFIG / "GPT-BUILDER-CONFIG.md"
    profile_text = read(PROFILE) if PROFILE.exists() else ""
    root_readme_text = read(README) if README.exists() else ""
    agents_text = read(AGENTS) if AGENTS.exists() else ""
    contributing_text = read(ROOT / "CONTRIBUTING.md") if (ROOT / "CONTRIBUTING.md").exists() else ""
    builder_config_text = read(builder_config) if builder_config.exists() else ""
    agent_patterns_text = read(ROOT / "docs" / "AGENT-OPERATING-PATTERNS.md") if (ROOT / "docs" / "AGENT-OPERATING-PATTERNS.md").exists() else ""
    boundary_contract_text = read(ROOT / "docs" / "BOUNDARY-AND-STATE-CONTRACT.md") if (ROOT / "docs" / "BOUNDARY-AND-STATE-CONTRACT.md").exists() else ""
    config_readme_text = read(CONFIG_README) if CONFIG_README.exists() else ""
    prompt_library_text = read(CONFIG / "PROMPT-LIBRARY.md") if (CONFIG / "PROMPT-LIBRARY.md").exists() else ""
    onboarding_text = read(CONFIG / "USER-ONBOARDING.md") if (CONFIG / "USER-ONBOARDING.md").exists() else ""
    limitations_text = read(CONFIG / "LIMITATIONS-AND-DISCLAIMERS.md") if (CONFIG / "LIMITATIONS-AND-DISCLAIMERS.md").exists() else ""
    refusal_text = read(CONFIG / "SAFETY-REFUSAL-POLICY.md") if (CONFIG / "SAFETY-REFUSAL-POLICY.md").exists() else ""
    examples_text = read(CONFIG / "EXAMPLES.md") if (CONFIG / "EXAMPLES.md").exists() else ""
    evaluation_text = read(CONFIG / "EVALUATION-CHECKLIST.md")
    pilot_text = read(ROOT / "docs" / "PILOT-LAUNCH-CHECKLIST.md") if (ROOT / "docs" / "PILOT-LAUNCH-CHECKLIST.md").exists() else ""
    preview_matrix_text = read(ROOT / "docs" / "PREVIEW-TEST-MATRIX.md") if (ROOT / "docs" / "PREVIEW-TEST-MATRIX.md").exists() else ""
    docs_basis_text = read(ROOT / "docs" / "OFFICIAL-DOCS-BASIS.md") if (ROOT / "docs" / "OFFICIAL-DOCS-BASIS.md").exists() else ""
    model_selection_text = read(ROOT / "docs" / "MODEL-SELECTION.md") if (ROOT / "docs" / "MODEL-SELECTION.md").exists() else ""
    reference_policy_text = read(ROOT / "docs" / "REFERENCE-DISTILLATION-POLICY.md") if (ROOT / "docs" / "REFERENCE-DISTILLATION-POLICY.md").exists() else ""
    secret_hits = scan_secrets()
    community_missing = [str(path) for path in COMMUNITY_FILES if not (ROOT / path).exists()]
    community_text = "\n".join(read(ROOT / path) for path in COMMUNITY_FILES if (ROOT / path).exists())
    undefined_labels = scan_undefined_issue_labels()
    private_path_hits = scan_private_path_references()
    legacy_version_hits = scan_legacy_version_references()
    eval_scenarios, eval_errors = load_eval_scenarios()
    critical_eval_count = sum(1 for item in eval_scenarios if item.get("critical") is True)
    missing_preview_matrix_ids = [
        str(item.get("id"))
        for item in eval_scenarios
        if item.get("id") and str(item.get("id")) not in preview_matrix_text
    ]
    versioned_paths = [path for path in CONFIG.glob("*.md")] + [INSTRUCTIONS / "INSTRUCTIONS.md"]
    version_mismatches = []
    for path in versioned_paths:
        if path.exists():
            version = extract_version(path)
            if version != EXPECTED_VERSION:
                version_mismatches.append(f"{path.relative_to(ROOT)}: {version or 'missing'}")

    checks = [
        check(CONFIG.exists(), "config directory exists"),
        check(config_files == EXPECTED_CONFIG_FILES, "config has exactly the expected 20 Markdown files", f"found {len(config_files)}"),
        check(not version_mismatches, f"version strings match {EXPECTED_VERSION}", "; ".join(version_mismatches)),
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
        check("v0.2.0" in root_readme_text and "public pilot" in root_readme_text.lower(), "root README states the public pilot version and status"),
        check(
            "## Static Package Model" in root_readme_text
            and "maintainer" in root_readme_text.lower()
            and "End users do not edit those 20 files" in root_readme_text,
            "root README explains the static maintainer-updated package model",
        ),
        check("static Builder package" in profile_text and "maintainers/admins publish the Instructions and 20 Knowledge files" in profile_text, "profile README explains the static builder package model"),
        check(AGENTS.exists(), "root AGENTS.md exists for AI-agent contributors"),
        check("scripts/check_open_prs.py" in agents_text and "open pr" in agents_text.lower(), "root AGENTS.md requires open PR coordination"),
        check("static release snapshot" in contributing_text and "release process" in contributing_text, "contributing guide treats the shipped GPT as a static release snapshot"),
        check("docs/AGENT-OPERATING-PATTERNS.md" in agents_text and "private pattern-only" in agent_patterns_text, "agent operating patterns document public-safe private-reference intake"),
        check("docs/BOUNDARY-AND-STATE-CONTRACT.md" in root_readme_text and "zone" in boundary_contract_text and "NOT VERIFIED" in boundary_contract_text, "boundary/state contract defines repository zones and fail-closed placement"),
        check((ROOT / "scripts" / "check_open_prs.py").exists(), "open PR checker script exists"),
        check("AGENTS.md" in root_readme_text and "check_open_prs.py" in root_readme_text, "root README documents agent and PR-check surfaces"),
        check(EVAL_SCENARIOS.exists(), "machine-readable Preview scenarios exist"),
        check(not eval_errors, "machine-readable Preview scenarios are parseable JSONL", "; ".join(eval_errors[:10])),
        check(len(eval_scenarios) >= 10 and critical_eval_count >= 7, "eval scenarios include sufficient critical coverage", f"{len(eval_scenarios)} total, {critical_eval_count} critical"),
        check("validate_eval_fixtures.py" in root_readme_text and "validate_release_artifacts.py" in root_readme_text and "docs/PREVIEW-TEST-MATRIX.md" in root_readme_text, "root README documents eval and release artifact validation"),
        check((ROOT / "docs" / "THREAT-MODEL.md").exists(), "public threat model exists"),
        check(not missing_preview_matrix_ids, "Preview matrix lists every eval scenario id", "; ".join(missing_preview_matrix_ids[:10])),
        check("THREAT-MODEL.md" in evaluation_text and "eval/preview-scenarios.jsonl" in evaluation_text, "evaluation checklist points to threat model and eval fixtures"),
        check("reference-distillation-private" in {str(item.get("id")) for item in eval_scenarios}, "eval scenarios include private-reference distillation coverage"),
        check("model-selection-not-overclaim" in {str(item.get("id")) for item in eval_scenarios}, "eval scenarios include model-selection overclaim coverage"),
        check("static-package-update-request" in {str(item.get("id")) for item in eval_scenarios}, "eval scenarios include static package update boundary coverage"),
        check("docs/REFERENCE-DISTILLATION-POLICY.md" in root_readme_text and "REFERENCE_DISTILLATION" in read(CONFIG / "FILE-WORKFLOW.md"), "root docs and workflow cover private-reference distillation"),
        check("docs/MODEL-SELECTION.md" in root_readme_text and "ChatGPT Builder" in model_selection_text and "Codex" in model_selection_text and "NOT VERIFIED" in model_selection_text, "model-selection guidance separates Codex-local preference from public Builder evidence"),
        check("private source material" in reference_policy_text and "Do not" in reference_policy_text, "reference distillation policy defines prohibited private-source handling"),
        check("OWASP" in docs_basis_text and "NIST" in docs_basis_text, "official docs basis includes public security references"),
        check("docs/OFFICIAL-DOCS-BASIS.md" in config_readme_text and "_codex-session" not in config_readme_text, "config README points to public docs basis instead of private session notes"),
        check(
            "## Static Package Model" in config_readme_text
            and "Users cannot update the 20 Knowledge files" in config_readme_text,
            "config README states users cannot update Knowledge or Instructions inside GPT sessions",
        ),
        check("static package boundary" in prompt_library_text.lower() and "deployed package is static" in prompt_library_text.lower(), "prompt library includes static package boundary prompt"),
        check("Example 15: Static Package Boundary" in examples_text and "maintainer/admin must update the repository package" in examples_text, "examples include static package boundary behavior"),
        check("Static Package Note" in onboarding_text and "maintainer/admin release assets" in onboarding_text, "user onboarding explains the static package model"),
        check("static to normal users" in limitations_text and "maintainer/admin publishes a refreshed GPT Builder configuration package" in limitations_text, "limitations file states deployed Knowledge and Instructions are static"),
        check("Update your Knowledge files from this chat" in refusal_text and "deployed package is static" in refusal_text, "safety refusal policy covers static package rewrite requests"),
        check("static release snapshot" in pilot_text and "end users do not edit the 20 Knowledge files or system Instructions" in pilot_text, "pilot checklist treats the deployed GPT as a static release snapshot"),
        check("## Recommended Model" in builder_config_text and "not combined with Actions" in builder_config_text, "GPT Builder config includes current model and Apps/Actions caveat"),
        check(
            "## Static Package Model" in builder_config_text
            and "not user-editable inside a normal GPT conversation" in builder_config_text,
            "GPT Builder config states the deployed configuration is static to users",
        ),
        check(not community_missing, "community contributor files exist", ", ".join(community_missing)),
        check(TELEGRAM_URL in community_text and "Contribution Idea" in community_text, "community path names Telegram and Contribution Idea workflow"),
        check(not undefined_labels, "issue-template labels are defined in .github/labels.json", "; ".join(undefined_labels)),
        check(not legacy_version_hits, "no stale public version references remain", "; ".join(legacy_version_hits[:10])),
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
