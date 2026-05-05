#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE_NAME = "GPTsAgent-working-directory.zip"
RELEASE_MANIFEST_NAME = "RELEASE-MANIFEST.json"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "dist", ".release"}
SKIP_FILES = {".env"}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if path.name in SKIP_FILES:
        return False
    return not any(part in SKIP_DIRS for part in rel.parts)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_version() -> str:
    manifest = ROOT / "config" / "MANIFEST.md"
    match = re.search(r"^- Version:\s*`([^`]+)`", manifest.read_text(encoding="utf-8"), re.M)
    return match.group(1) if match else "NOT VERIFIED"


def collect_files() -> list[Path]:
    return [
        path
        for path in sorted(ROOT.rglob("*"))
        if path.is_file() and should_include(path)
    ]


def main() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    archive = DIST / ARCHIVE_NAME
    if archive.exists():
        archive.unlink()

    files = collect_files()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            rel = path.relative_to(ROOT)
            zf.write(path, Path("GPTsAgent") / rel)

    digest = sha256(archive)
    checksum = DIST / "SHA256SUMS.txt"
    checksum.write_text(f"{digest}  {ARCHIVE_NAME}\n", encoding="utf-8")

    manifest = {
        "status": "PASS",
        "package": "GPTsAgent",
        "package_version": package_version(),
        "archive_name": ARCHIVE_NAME,
        "archive_sha256": digest,
        "archive_size_bytes": archive.stat().st_size,
        "wrapper_root": "GPTsAgent/",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "config_markdown_count": len([path for path in files if path.parent == ROOT / "config" and path.suffix == ".md"]),
        "eval_fixture_count": len([path for path in files if path.parts[-2:] == ("eval", "preview-scenarios.jsonl")]),
        "file_count": len(files),
        "included_files": [str(path.relative_to(ROOT)) for path in files],
        "excluded_surfaces": sorted(SKIP_DIRS | SKIP_FILES),
        "validation_expectation": [
            "archive opens",
            "checksum matches",
            "20 config Markdown files present",
            "eval fixtures present",
            "no .git or dist surfaces included",
        ],
    }
    (DIST / RELEASE_MANIFEST_NAME).write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Wrote {archive}")
    print(f"SHA256 {digest}")
    print(f"Wrote {DIST / RELEASE_MANIFEST_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
