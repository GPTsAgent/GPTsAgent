#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE = DIST / "GPTsAgent-working-directory.zip"
CHECKSUMS = DIST / "SHA256SUMS.txt"
MANIFEST = DIST / "RELEASE-MANIFEST.json"


def fail(message: str) -> int:
    print(f"FAILED: {message}")
    return 1


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    for path in (ARCHIVE, CHECKSUMS, MANIFEST):
        if not path.exists():
            return fail(f"{path.relative_to(ROOT)} does not exist")

    actual_digest = sha256(ARCHIVE)
    checksums_text = CHECKSUMS.read_text(encoding="utf-8")
    if f"{actual_digest}  {ARCHIVE.name}" not in checksums_text:
        return fail("SHA256SUMS.txt does not match archive digest")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"release manifest is invalid JSON: {exc}")

    if manifest.get("archive_sha256") != actual_digest:
        return fail("release manifest archive_sha256 does not match archive digest")
    if manifest.get("archive_name") != ARCHIVE.name:
        return fail("release manifest archive_name does not match expected archive")
    if manifest.get("wrapper_root") != "GPTsAgent/":
        return fail("release manifest wrapper_root is not GPTsAgent/")

    try:
        with zipfile.ZipFile(ARCHIVE) as zf:
            bad_file = zf.testzip()
            if bad_file:
                return fail(f"zip integrity check failed at {bad_file}")
            names = zf.namelist()
    except zipfile.BadZipFile as exc:
        return fail(f"archive is not a valid ZIP: {exc}")

    required = {
        "GPTsAgent/README.md",
        "GPTsAgent/config/MANIFEST.md",
        "GPTsAgent/instructions/SYSTEM-INSTRUCTIONS.txt",
        "GPTsAgent/eval/preview-scenarios.jsonl",
        "GPTsAgent/docs/BOUNDARY-AND-STATE-CONTRACT.md",
        "GPTsAgent/docs/AGENT-OPERATING-PATTERNS.md",
        "GPTsAgent/docs/COMMAND-SESSION-PATTERNS.md",
        "GPTsAgent/docs/MODEL-SELECTION.md",
        "GPTsAgent/docs/PREVIEW-TEST-MATRIX.md",
        "GPTsAgent/docs/REFERENCE-DISTILLATION-POLICY.md",
        "GPTsAgent/docs/THREAT-MODEL.md",
    }
    missing = sorted(required.difference(names))
    if missing:
        return fail(f"archive missing required files: {', '.join(missing)}")

    forbidden_parts = {".git", "dist", "__pycache__"}
    forbidden = [
        name
        for name in names
        if any(part in forbidden_parts for part in Path(name).parts)
    ]
    if forbidden:
        return fail(f"archive contains forbidden paths: {', '.join(forbidden[:10])}")

    config_count = len([name for name in names if name.startswith("GPTsAgent/config/") and name.endswith(".md")])
    if config_count != 20:
        return fail(f"archive has {config_count} config Markdown files, expected 20")

    if manifest.get("file_count") != len(names):
        return fail("release manifest file_count does not match archive entries")
    if manifest.get("config_markdown_count") != 20:
        return fail("release manifest config_markdown_count is not 20")

    print("# GPTsAgent Release Artifact Validation")
    print(f"Archive: {ARCHIVE.relative_to(ROOT)}")
    print(f"SHA256: {actual_digest}")
    print(f"Entries: {len(names)}")
    print("Status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
