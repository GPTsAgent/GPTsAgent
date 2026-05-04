# User Onboarding

Version: `v4.0.0`

Purpose: Explain how normal users should use the GPT, what to upload, what not to upload, how to request artifacts, and how to interpret statuses.

Use this file when: writing first-run copy, help text, or user guidance for Sandbox File Operator.

Related files: `README.md`, `PROMPT-LIBRARY.md`, `REPORT-TEMPLATES.md`, `LIMITATIONS-AND-DISCLAIMERS.md`

## First-Run Welcome

```text
Upload a file or ZIP archive and tell me your goal. I can inspect uploaded files inside ChatGPT, safety-scan archives before extraction, map projects, make bounded patches, and return artifacts such as updated ZIPs, diffs, manifests, checksums, validation reports, and final handoffs. I cannot directly access or edit files on your computer unless you upload them here or connect a scoped tool that is available in this GPT.
```

## What To Upload

Good inputs:

- project ZIPs without secrets;
- documentation files;
- prompt packs;
- manifests;
- sanitized logs;
- before/after archives for comparison;
- screenshots or images when visual analysis is relevant;
- small representative samples when the full project is too large.

## What Not To Upload

Do not upload:

- secrets;
- private keys;
- `.env` files;
- production credentials;
- customer data you are not authorized to share;
- private logs with tokens;
- malware for execution;
- huge generated dependency folders unless they are essential.

## How To Ask For Work

Use:

```text
Goal:
Uploaded files:
Do not touch:
Desired outputs:
Validation needed:
```

Example:

```text
Goal: Improve the documentation in this project ZIP.
Uploaded files: <PROJECT_ZIP>
Do not touch: code, secrets, generated files, CI, package files.
Desired outputs: updated ZIP, diff, manifest, validation report, checksum.
Validation needed: archive opens, wrapper preserved, no unexpected removals, no secret-like additions.
```

## If You Upload A ZIP

Expect the GPT to:

1. treat the ZIP as immutable source evidence;
2. safety-scan before extraction;
3. report wrapper root and risks;
4. avoid secret bodies;
5. choose a safe mode;
6. return a project map or patch plan before broad edits.

## If You Want Edits

State:

- target files or allowed areas;
- protected files;
- desired output format;
- validation requirements.

If the request is broad, the GPT should make a conservative bounded pass and report assumptions.

## How To Interpret Status Labels

| Status | Meaning |
|---|---|
| PASS | The check ran and passed in the available environment. |
| PARTIAL | Useful work completed, but important caveats remain. |
| FAILED | A check or operation was attempted and failed. |
| SKIPPED | The GPT intentionally skipped a step as unnecessary or unsafe. |
| NOT RUN | The step was not attempted. |
| NOT VERIFIED | The available evidence cannot prove the claim. |
| TIMEOUT | The operation started but exceeded the available budget. |

## Artifact Meanings

- Report: what was found.
- Diff: exact text changes.
- Manifest: structured change summary.
- Updated ZIP: downloadable package produced from sandbox work.
- Validation report: checks that ran and what remains unverified.
- Checksum: SHA256 identity proof for an artifact.
- Handoff: final summary and next best move.

## Boundary Reminder

The GPT works with uploaded copies and enabled scoped tools. It does not browse or edit your local computer directly from ChatGPT.com.

## Operational Rule

Upload the smallest non-secret file set that can support the requested work and ask for explicit artifacts when you need a handoff.
