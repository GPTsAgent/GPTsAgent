# Manifest

Version: `v4.0.0`

Purpose: List the exact 20 root Markdown files, package identity, intended GPT name, recommended capabilities, upload order, and validation summary.

Use this file when: checking package completeness or uploading Knowledge to GPT Builder.

Related files: `README.md`, `GPT-BUILDER-CONFIG.md`, `EVALUATION-CHECKLIST.md`, `PUBLISHING-GPT-STORE.md`

## Package Identity

- Package name: Sandbox File Operator GPT Config Pack
- Version: `v4.0.0`
- Date: `2026-05-04`
- Intended GPT name: Sandbox File Operator
- Package type: 20-file Custom GPT Knowledge/configuration package
- Behavior-critical file: `GPT-BUILDER-CONFIG.md`
- Root Knowledge file count: 20

## Exact Root File List

| Slot | File | Role |
|---:|---|---|
| 1 | `README.md` | Overview, installation, safe defaults, and architecture. |
| 2 | `GPT-BUILDER-CONFIG.md` | Copy-ready GPT Builder fields and canonical Instructions. |
| 3 | `AGENTS.md` | Maintainer constitution for future package edits. |
| 4 | `SANDBOX.md` | ChatGPT sandbox mental model and boundary language. |
| 5 | `FILE-WORKFLOW.md` | ZIP-in, sandbox-work, artifact-out workflows and modes. |
| 6 | `ZIP-SAFETY-POLICY.md` | Archive preflight gates and fail-closed behavior. |
| 7 | `SECRET-HYGIENE.md` | Secret-sensitive path, content, and artifact handling. |
| 8 | `CAPABILITIES-MAP.md` | Capability routing and tool-use limits. |
| 9 | `ACTIONS-API-BLUEPRINT.md` | Optional safe backend design with Actions off by default. |
| 10 | `ARTIFACT-CONTRACT.md` | Artifact metadata, status labels, validation, and handoff. |
| 11 | `REPORT-TEMPLATES.md` | Copy-ready report formats. |
| 12 | `PROMPT-LIBRARY.md` | User, builder, validation, and adversarial prompts. |
| 13 | `USER-ONBOARDING.md` | First-run user guidance and status explanation. |
| 14 | `LIMITATIONS-AND-DISCLAIMERS.md` | Public-safe limitations and no-overclaim language. |
| 15 | `SAFETY-REFUSAL-POLICY.md` | Refusal categories and safe narrowing. |
| 16 | `EVALUATION-CHECKLIST.md` | Preview, functional, artifact, red-team, regression, and publishing tests. |
| 17 | `PUBLISHING-GPT-STORE.md` | Public listing and release readiness. |
| 18 | `VERSIONING-ROADMAP.md` | Release history and future roadmap. |
| 19 | `EXAMPLES.md` | Expected behavior examples and bad examples. |
| 20 | `MANIFEST.md` | Canonical file list, upload order, and validation summary. |

## Recommended Upload Order

Upload in the slot order above. The order groups setup, operating model, safety, tool orchestration, artifacts, user experience, evaluation, publishing, versioning, examples, and manifest.

## Recommended Capabilities

| Capability | Recommended setting |
|---|---|
| File uploads | On |
| Code Interpreter/Data Analysis | On |
| Web search | On when current facts and citations matter |
| Canvas | Optional |
| Image generation | Off by default |
| Apps/connectors | Optional and scoped |
| Actions | Off by default |

## Validation Summary

- Exactly 20 primary root Markdown files expected.
- Every file should start with title, version, purpose, use-case, and related-files metadata.
- Every file should end with an operational rule.
- `GPT-BUILDER-CONFIG.md` should contain the complete ready-to-copy Instructions block.
- `AGENTS.md` should state that the package is an operating wrapper, not a trained model.
- The package must not claim direct local filesystem access inside ChatGPT.com.
- The package must not tell users to upload secrets.
- Actions must be optional and must forbid raw shell endpoints.
- Artifact statuses must be exactly `PASS`, `PARTIAL`, `FAILED`, `SKIPPED`, `NOT RUN`, `NOT VERIFIED`, and `TIMEOUT`.
- Evaluation must include red-team and regression tests.

## Knowledge Boundary

Do not upload `_codex-session/`, package artifacts, source archives, `.git`, caches, secrets, generated dependency folders, or validation scratch files as GPT Knowledge.

## Operational Rule

If the actual root file list differs from this manifest, update the manifest or stop publication.
