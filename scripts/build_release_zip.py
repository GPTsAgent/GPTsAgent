#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
ARCHIVE_NAME = "GPTsAgent-working-directory.zip"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "dist", ".release"}
SKIP_FILES = {".env"}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if path.name in SKIP_FILES:
        return False
    return not any(part in SKIP_DIRS for part in rel.parts)


def main() -> int:
    DIST.mkdir(parents=True, exist_ok=True)
    archive = DIST / ARCHIVE_NAME
    if archive.exists():
        archive.unlink()

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file() or not should_include(path):
                continue
            rel = path.relative_to(ROOT)
            zf.write(path, Path("GPTsAgent") / rel)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = DIST / "SHA256SUMS.txt"
    checksum.write_text(f"{digest}  {ARCHIVE_NAME}\n", encoding="utf-8")

    print(f"Wrote {archive}")
    print(f"SHA256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
