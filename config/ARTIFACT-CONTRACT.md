# Artifact Contract

Version: `v0.3.0`

Purpose: Define artifact types, required metadata, validation statuses, integrity checks, and handoff standards.

Use this file when: the GPT creates or returns reports, diffs, manifests, checksums, updated files, or ZIP artifacts.

Related files: `FILE-WORKFLOW.md`, `REPORT-TEMPLATES.md`, `MANIFEST.md`, `EVALUATION-CHECKLIST.md`

## Artifact Types

| Type | Purpose |
|---|---|
| Safety scan | Archive and input risk report before extraction or edits. |
| Sandbox session report | Source evidence, mode, assumptions, allowed operations, blocked operations. |
| Project audit | Tree summary, technologies, entry points, configs, docs, tests, risks. |
| Patch plan | Objective, target files, protected files, edit strategy, validation plan. |
| Updated file | Direct edited document or source file. |
| Updated ZIP | Repackaged project or file set for user download. |
| Unified diff | Exact text changes. |
| Change manifest | Machine-readable or structured summary of added, modified, removed, unchanged files. |
| Validation report | Checks run, status labels, evidence, limitations. |
| Checksum | SHA256 for major downloadable artifacts when possible. |
| Release manifest | Machine-readable package version, archive name, wrapper root, file count, checksum, and included file list. |
| Recovery report | Explanation of discarded partial artifacts, rebuilt outputs, and remaining limitations after a packaging or validation issue. |
| Reference distillation report | Pattern-only summary proving private material was not copied, named, or retained. |
| Final handoff | Human-readable closeout with next best move. |

## Required Metadata

Major artifact handoffs should include:

- source file or archive name;
- output artifact name;
- date if available;
- selected mode;
- wrapper root before and after;
- target files;
- protected files;
- added files;
- modified files;
- removed files;
- checksum for major ZIPs;
- validation status;
- limitations.
- private-reference boundary and marker-scan result when private material influenced the work.

Release artifacts should also include `dist/RELEASE-MANIFEST.json` when the repository tooling builds `dist/GPTsAgent-working-directory.zip`.

## Status Labels

Use exactly:

- `PASS`;
- `PARTIAL`;
- `FAILED`;
- `SKIPPED`;
- `NOT RUN`;
- `NOT VERIFIED`;
- `TIMEOUT`.

## Updated ZIP Requirements

Before returning an updated ZIP, verify when possible:

- ZIP exists;
- ZIP opens;
- expected wrapper root exists;
- expected files exist;
- no unexpected removals occurred;
- diff exists for text changes;
- manifest exists;
- validation report exists;
- checksum exists;
- changed text contains no obvious secret-like material.

For repository release ZIPs, also verify `dist/RELEASE-MANIFEST.json` and `dist/SHA256SUMS.txt`.

## Manifest Contract

A manifest should include:

```json
{
  "status": "PASS",
  "source_archive": "<PROJECT_ZIP>",
  "output_archive": "project-updated.zip",
  "wrapper_root_before": "project/",
  "wrapper_root_after": "project/",
  "mode": "PATCH_ONLY",
  "added": [],
  "modified": ["README.md"],
  "removed": [],
  "unchanged_count": 0,
  "validation": ["zip opens", "diff exists", "checksum created"],
  "limitations": ["Host tests NOT VERIFIED"]
}
```

## Diff Contract

- Generate unified diffs for text changes.
- Do not pretend binary changes have a meaningful text diff.
- Mention binary changes in the manifest.
- Preserve line endings where practical.
- Report if no diff could be generated.

## Artifact Recovery

If artifact creation, copying, validation, or packaging partially fails:

- do not present partial artifacts as `PASS`;
- discard or quarantine partial outputs when possible;
- rebuild from the original readable uploaded source or validated working copy;
- rerun the smallest deterministic integrity check;
- report which artifacts were discarded, rebuilt, validated, or left `PARTIAL`;
- mark blocked outputs `FAILED`, `NOT RUN`, `NOT VERIFIED`, or `TIMEOUT` as appropriate.

If a full diff is too large or slow, generate a selected-file diff and explicitly mark the full diff `PARTIAL` or `NOT RUN`.

## Atomic Publish

For updated ZIP or release bundles, treat publication as atomic:

1. Build into a candidate path.
2. Validate openability, wrapper root, expected files, checksum, and manifest.
3. Only then present the candidate as the final artifact.
4. If validation fails, do not reuse the failed candidate name as if it passed.

## Handoff Standard

Final artifact handoff should include:

1. OPERATING VERDICT
2. WHAT CHANGED
3. VERIFICATION PERFORMED
4. FILES UPDATED OR ARTIFACTS CREATED
5. BLOCKED / NOT RUN
6. NEXT BEST MOVE

## Integrity Standard

Use SHA256 checksums for major ZIPs and important bundled artifacts when possible. A checksum proves artifact identity, not semantic correctness.

## Operational Rule

Never return an artifact as PASS unless the required artifact checks actually passed.
