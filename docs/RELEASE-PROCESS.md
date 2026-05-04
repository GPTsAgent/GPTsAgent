# Release Process

Use this when preparing a public update.

## Preflight

```bash
python3 scripts/extract_instructions.py
python3 scripts/validate_workspace.py
python3 scripts/sync_labels.py
python3 scripts/build_release_zip.py
```

Shortcut:

```bash
make check
```

Expected result:

- `scripts/validate_workspace.py` returns `Status: PASS`.
- `scripts/sync_labels.py` returns a dry-run label report without errors.
- `docs/OFFICIAL-DOCS-BASIS.md` and `docs/PILOT-LAUNCH-CHECKLIST.md` are current if Builder behavior or public launch claims changed.
- `dist/GPTsAgent-working-directory.zip` exists.
- `dist/SHA256SUMS.txt` exists.

## Publish Order

1. Merge the PR into `GPTsAgent/GPTsAgent`.
2. Sync missing GitHub labels if community templates changed and maintainer credentials are available.
3. Re-check `docs/OFFICIAL-DOCS-BASIS.md` and `docs/PILOT-LAUNCH-CHECKLIST.md` if Builder settings or public claims changed.
4. Tag or release the canonical workspace when the update is a versioned release.
5. Publish the release ZIP from `dist/` if a downloadable artifact is needed.
6. Sync `GPTsAgent/.github` only if profile or community files changed.

## Release Evidence

Record:

- commit SHA;
- validation output;
- ZIP SHA256;
- label sync result;
- pilot launch checklist result if Builder settings changed;
- GPT Builder Preview tests that ran;
- anything marked `NOT RUN`, `NOT VERIFIED`, or `TIMEOUT`.
