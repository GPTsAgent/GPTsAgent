#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "GPT-BUILDER-CONFIG.md"
OUT = ROOT / "instructions"


def main() -> int:
    text = CONFIG.read_text(encoding="utf-8")
    match = re.search(
        r"## Ready-to-Copy Instructions Block\n\n```text\n(.*?)\n```",
        text,
        re.S,
    )
    if not match:
        raise SystemExit("Instructions block not found in config/GPT-BUILDER-CONFIG.md")

    instructions = match.group(1).rstrip() + "\n"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "SYSTEM-INSTRUCTIONS.txt").write_text(instructions, encoding="utf-8")
    (OUT / "INSTRUCTIONS.md").write_text(
        "# Sandbox File Operator System Instructions\n\n"
        "Version: `v4.0.0`\n\n"
        "This is the canonical ready-to-copy Instructions block for the GPTsAgent "
        "Sandbox File Operator Custom GPT configuration.\n\n"
        "```text\n"
        f"{instructions}"
        "```\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT / 'SYSTEM-INSTRUCTIONS.txt'}")
    print(f"Wrote {OUT / 'INSTRUCTIONS.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
