#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST_ZIP = ROOT / "dist" / "GPTsAgent-working-directory.zip"
STATUS_LABELS = ("PASS", "PARTIAL", "FAILED", "SKIPPED", "NOT RUN", "NOT VERIFIED", "TIMEOUT")
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "dist", ".release"}
SKIP_SUFFIXES = {".zip", ".pyc", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf"}
SECRET_ALLOW_FILES = {Path(".env.example")}


PRIVATE_MARKERS: dict[str, re.Pattern[str]] = {
    "private host path": re.compile(r"/home/[A-Za-z0-9._-]+(?:/|$)"),
    "private token file marker": re.compile("token" + "_github", re.I),
    "private project marker 1": re.compile("Capsule" + "OS", re.I),
    "private project marker 2": re.compile(r"(?<![A-Za-z0-9])" + "N" + r"1(?![A-Za-z0-9])", re.I),
    "private org marker": re.compile("number" + "1projects", re.I),
    "private project marker 3": re.compile("Aps" + "ny", re.I),
    "private project marker 4": re.compile("Omni" + "Route", re.I),
    "private reference marker": re.compile("skill " + r"\(2\)" + r"\.zip", re.I),
}

SECRET_PATTERNS: dict[str, re.Pattern[str]] = {
    "OpenAI key": re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}(?![A-Za-z0-9_-])"),
    "AWS access key": re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])"),
    "Slack token": re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{20,}(?![A-Za-z0-9-])"),
    "GitHub token": re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9_]{30,}(?![A-Za-z0-9_])"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |)?PRIVATE KEY-----"),
}


@dataclass
class CommandResult:
    label: str
    command: list[str]
    returncode: int
    status: str
    output: str


@dataclass
class ScanResult:
    label: str
    status: str
    hits: list[str]


def run_command(label: str, command: list[str]) -> CommandResult:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    output = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part)
    status = extract_status(output)
    if result.returncode != 0 and status == "PASS":
        status = "FAILED"
    elif not status:
        status = "PASS" if result.returncode == 0 else "FAILED"
    return CommandResult(label=label, command=command, returncode=result.returncode, status=status, output=output)


def extract_status(output: str) -> str:
    for line in reversed(output.splitlines()):
        match = re.search(r"\bStatus:\s*(" + "|".join(re.escape(item) for item in STATUS_LABELS) + r")\b", line)
        if match:
            return match.group(1)
    return ""


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        paths.append(path)
    return paths


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def scan_text(label: str, text: str, patterns: dict[str, re.Pattern[str]]) -> list[str]:
    hits: list[str] = []
    for name, pattern in patterns.items():
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            hits.append(f"{label}:{line_no}: {name}")
    return hits


def scan_workspace(label: str, patterns: dict[str, re.Pattern[str]], allow_files: set[Path] | None = None) -> ScanResult:
    hits: list[str] = []
    allow_files = allow_files or set()
    for path in iter_text_files():
        rel = path.relative_to(ROOT)
        if rel in allow_files:
            continue
        text = read_text(path)
        if text is None:
            continue
        hits.extend(scan_text(str(rel), text, patterns))
    return ScanResult(label=label, status="PASS" if not hits else "FAILED", hits=hits)


def scan_release_zip(label: str, patterns: dict[str, re.Pattern[str]], allow_names: set[str] | None = None) -> ScanResult:
    if not DIST_ZIP.exists():
        return ScanResult(label=label, status="FAILED", hits=[f"{DIST_ZIP.relative_to(ROOT)} missing"])
    hits: list[str] = []
    allow_names = allow_names or set()
    with zipfile.ZipFile(DIST_ZIP) as zf:
        for name in zf.namelist():
            if name.endswith("/"):
                continue
            parts = Path(name).parts
            if any(part in SKIP_DIRS for part in parts):
                continue
            if Path(name).name in allow_names:
                continue
            if Path(name).suffix.lower() in SKIP_SUFFIXES:
                continue
            for marker_name, pattern in patterns.items():
                if pattern.search(name):
                    hits.append(f"{name}:path: {marker_name}")
            try:
                text = zf.read(name).decode("utf-8")
            except Exception:
                continue
            hits.extend(scan_text(name, text, patterns))
    return ScanResult(label=label, status="PASS" if not hits else "FAILED", hits=hits)


def scan_git_history_private_markers() -> ScanResult:
    revs_result = subprocess.run(["git", "rev-list", "--all"], cwd=ROOT, capture_output=True, text=True)
    if revs_result.returncode != 0:
        return ScanResult("git history private-marker scan", "FAILED", ["git rev-list --all failed"])

    hits: list[str] = []
    for rev in revs_result.stdout.splitlines():
        tree = subprocess.run(["git", "ls-tree", "-r", "--name-only", rev], cwd=ROOT, capture_output=True, text=True)
        if tree.returncode != 0:
            hits.append(f"{rev}: git ls-tree failed")
            break
        for name in tree.stdout.splitlines():
            path = Path(name)
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() in SKIP_SUFFIXES:
                continue
            hits.extend(scan_text(f"{rev}:{name}", name, PRIVATE_MARKERS))
            blob = subprocess.run(["git", "show", f"{rev}:{name}"], cwd=ROOT, capture_output=True)
            if blob.returncode != 0:
                continue
            try:
                text = blob.stdout.decode("utf-8")
            except UnicodeDecodeError:
                continue
            hits.extend(scan_text(f"{rev}:{name}", text, PRIVATE_MARKERS))
        if hits:
            break
    return ScanResult("git history private-marker scan", "PASS" if not hits else "FAILED", hits)


def prepublish_commands() -> list[tuple[str, list[str]]]:
    scripts = sorted(str(path.relative_to(ROOT)) for path in (ROOT / "scripts").glob("*.py"))
    return [
        ("open PR coordination", ["python3", "scripts/check_open_prs.py"]),
        ("workspace validation", ["python3", "scripts/validate_workspace.py"]),
        ("eval fixture validation", ["python3", "scripts/validate_eval_fixtures.py"]),
        ("script compile", ["python3", "-m", "py_compile", *scripts]),
        ("label dry run", ["python3", "scripts/sync_labels.py"]),
        ("release ZIP build", ["python3", "scripts/build_release_zip.py"]),
        ("release artifact validation", ["python3", "scripts/validate_release_artifacts.py"]),
    ]


def format_report(command_results: list[CommandResult], scan_results: list[ScanResult]) -> str:
    overall_ok = all(item.returncode == 0 and item.status == "PASS" for item in command_results)
    overall_ok = overall_ok and all(item.status == "PASS" for item in scan_results)
    lines = [
        "# GPTsAgent Prepublish Audit",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
    ]
    for item in command_results:
        detail = "ok" if item.returncode == 0 else f"exit {item.returncode}"
        lines.append(f"| {item.label} | {item.status} | {detail} |")
    for item in scan_results:
        detail = "0 hits" if not item.hits else f"{len(item.hits)} hit(s)"
        lines.append(f"| {item.label} | {item.status} | {detail} |")
    lines.extend(["", "## Findings"])
    any_findings = False
    for item in scan_results:
        if item.hits:
            any_findings = True
            lines.append(f"- {item.label}:")
            for hit in item.hits[:20]:
                lines.append(f"  - {hit}")
            if len(item.hits) > 20:
                lines.append(f"  - ... {len(item.hits) - 20} more")
    for item in command_results:
        if item.returncode != 0 or item.status != "PASS":
            any_findings = True
            lines.append(f"- {item.label}: command failed or did not report PASS")
            if item.output:
                snippet = "\n".join(item.output.splitlines()[-12:])
                lines.append("```text")
                lines.append(snippet)
                lines.append("```")
    if not any_findings:
        lines.append("- No blocking findings.")
    lines.extend(["", f"Status: {'PASS' if overall_ok else 'FAILED'}"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the full GPTsAgent maintainer prepublish audit.")
    parser.add_argument("--write", type=Path, help="Optional path for a Markdown audit report.")
    args = parser.parse_args()

    command_results = [run_command(label, command) for label, command in prepublish_commands()]
    scan_results = [
        scan_workspace("workspace private-marker scan", PRIVATE_MARKERS),
        scan_release_zip("release ZIP private-marker scan", PRIVATE_MARKERS),
        scan_workspace("workspace secret-like scan", SECRET_PATTERNS, SECRET_ALLOW_FILES),
        scan_release_zip("release ZIP secret-like scan", SECRET_PATTERNS, {item.name for item in SECRET_ALLOW_FILES}),
        scan_git_history_private_markers(),
    ]
    report = format_report(command_results, scan_results)
    print(report, end="")
    if args.write:
        target = args.write if args.write.is_absolute() else ROOT / args.write
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(report, encoding="utf-8")
    return 0 if report.rstrip().endswith("Status: PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
