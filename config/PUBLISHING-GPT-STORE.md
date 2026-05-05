# Publishing And GPT Store Readiness

Version: `v0.3.0`

Purpose: Guide public GPT readiness, name/description/category choices, capability settings, privacy caveats, and final pre-publish tests.

Use this file when: preparing Sandbox File Operator for sharing or GPT Store publication.

Related files: `README.md`, `GPT-BUILDER-CONFIG.md`, `EVALUATION-CHECKLIST.md`, `LIMITATIONS-AND-DISCLAIMERS.md`

## Readiness Checklist

- Instructions pasted from `GPT-BUILDER-CONFIG.md`.
- Exactly 20 root Markdown Knowledge files uploaded.
- No `_codex-session/` files uploaded as Knowledge.
- Code Interpreter/Data Analysis enabled.
- File uploads enabled if separate.
- Web search enabled if current facts and citations are part of the product.
- Actions off unless a real backend exists.
- Apps/connectors off unless you have explicitly scoped connected data and Actions remain off.
- Builder model selection checked against current GPT Builder options.
- Public description says uploaded files, not local filesystem control.
- Preview tests pass.
- Red-team tests pass.
- Artifact handoff tests pass.
- Knowledge files contain no secrets.

## Name Guidance

Recommended:

- Sandbox File Operator;
- ZIP Sandbox Operator;
- File Artifact Workbench.

Avoid:

- Local Filesystem Controller;
- Computer File Fixer;
- Secret Extractor;
- Shell Agent;
- Production Auto-Patcher.

## Description Guidance

Use:

```text
Safe sandbox GPT for uploaded files and ZIP projects in ChatGPT. Scan archives, map projects, avoid secret bodies, create bounded patches, validate artifacts, and return reports, diffs, manifests, checksums, and updated ZIPs. Does not directly access your local computer.
```

Avoid claims about direct computer access, guaranteed security, background execution, or production validation.

## Category Guidance

Choose the closest available category at publication time:

- Productivity;
- Programming;
- Research;
- Writing;
- Education.

## Capability Settings

| Capability | Setting | Rationale |
|---|---:|---|
| File upload | On | Core product input path. |
| Code Interpreter/Data Analysis | On | Main sandbox execution and artifact path. |
| Web search | On | Current docs and citations. |
| Canvas | Optional | Long docs and iterative edits. |
| Image generation | Off by default | Not needed for core workflows. |
| Apps/connectors | Optional | Scoped connected sources only; keep Actions off. |
| Actions | Off by default | Backend not included in this package. |

## Privacy Caveats

If Actions are off, still warn users not to upload secrets. If Actions are on, public GPTs need a valid privacy policy URL covering file uploads, retention, deletion, logging, subprocessors, user rights, and secret-handling posture.

If Apps/connectors are enabled, recheck current Builder docs before publishing because capability combinations and availability can change.

## Final Pre-Publish Tests

Run:

- local filesystem boundary prompt;
- safe ZIP prompt;
- unsafe ZIP prompt;
- `.env` path prompt;
- prompt injection prompt;
- bounded patch artifact prompt;
- Actions unavailable prompt;
- Apps/connectors unavailable prompt;
- Builder model/capability explanation prompt;
- hidden-instruction extraction prompt;
- current docs prompt requiring citations;
- final handoff prompt.

## Versioning

Use `v0.3.0` for this release. If a GPT Builder draft has version history, document the public change as "v0.3.0 command/session and skill-catalog hardening upgrade."

## Support Copy

```text
If a task fails, upload the validation report and describe the desired output. The GPT can usually produce a narrower patch, a safer repackage plan, or a clearer handoff.
```

## Operational Rule

Do not publish until the Preview behavior matches the package promise under both normal and adversarial prompts.
