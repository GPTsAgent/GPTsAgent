# Release Process

Use this when preparing a public update.

## Preflight

```bash
python3 scripts/extract_instructions.py
python3 scripts/validate_workspace.py
python3 scripts/build_release_zip.py
```

Expected result:

- `scripts/validate_workspace.py` returns `Status: PASS`.
- `dist/GPTsAgent-working-directory.zip` exists.
- `dist/SHA256SUMS.txt` exists.

## Publish Order

1. Merge the PR into `GPTsAgent/GPTsAgent`.
2. Tag or release the canonical workspace.
3. Publish the release ZIP from `dist/` if a downloadable artifact is needed.
4. Sync `GPTsAgent/.github` only if profile or community files changed.

## Release Evidence

Record:

- commit SHA;
- validation output;
- ZIP SHA256;
- GPT Builder Preview tests that ran;
- anything marked `NOT RUN`, `NOT VERIFIED`, or `TIMEOUT`.
