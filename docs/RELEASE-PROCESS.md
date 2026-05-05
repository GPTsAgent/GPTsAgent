# Release Process

Use this when preparing a public update.

## Preflight

```bash
python3 scripts/check_open_prs.py
python3 scripts/extract_instructions.py
python3 scripts/validate_workspace.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/sync_labels.py
python3 scripts/build_release_zip.py
python3 scripts/validate_release_artifacts.py
python3 scripts/prepublish_audit.py
```

Shortcut:

```bash
make check
```

Expected result:

- `scripts/validate_workspace.py` returns `Status: PASS`.
- `scripts/validate_eval_fixtures.py` returns `Status: PASS`.
- `scripts/check_open_prs.py` reports no overlapping open PRs for the release files.
- `scripts/sync_labels.py` returns a dry-run label report without errors.
- `scripts/validate_release_artifacts.py` verifies the release ZIP, checksum, wrapper root, and release manifest.
- `scripts/prepublish_audit.py` returns `Status: PASS` before a maintainer pushes or publishes a release.
- `docs/BOUNDARY-AND-STATE-CONTRACT.md` is current and reflected in contributor workflow and release validation.
- `docs/OFFICIAL-DOCS-BASIS.md` and `docs/PILOT-LAUNCH-CHECKLIST.md` are current if Builder behavior or public launch claims changed.
- `docs/REFERENCE-DISTILLATION-POLICY.md` is current and the private-marker scan passes if private reference material influenced the package.
- `dist/GPTsAgent-working-directory.zip` exists.
- `dist/SHA256SUMS.txt` exists.
- `dist/RELEASE-MANIFEST.json` exists.

## Publish Order

1. Merge the PR into `GPTsAgent/GPTsAgent`.
2. Sync missing GitHub labels if community templates changed and maintainer credentials are available.
3. Re-check `docs/OFFICIAL-DOCS-BASIS.md` and `docs/PILOT-LAUNCH-CHECKLIST.md` if Builder settings or public claims changed.
4. Re-check `docs/REFERENCE-DISTILLATION-POLICY.md` if private reference material influenced the package.
5. Re-check `docs/BOUNDARY-AND-STATE-CONTRACT.md` if repository zones, canonical write targets, or release-state rules changed.
6. Tag or release the canonical workspace when the update is a versioned release.
7. Publish the release ZIP from `dist/` if a downloadable artifact is needed.
8. Sync `GPTsAgent/.github` only if profile or community files changed.

## Release Evidence

Record:

- commit SHA;
- validation output;
- ZIP SHA256;
- release manifest;
- prepublish audit output;
- label sync result;
- pilot launch checklist result if Builder settings changed;
- GPT Builder Preview tests that ran;
- anything marked `NOT RUN`, `NOT VERIFIED`, or `TIMEOUT`.
