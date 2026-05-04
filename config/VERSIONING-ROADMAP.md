# Versioning Roadmap

Version: `v4.1.0`

Purpose: Document package evolution, current version, future Actions backend, future eval harness, and specialized skill packs.

Use this file when: tracking release history, future scope, or public update notes.

Related files: `README.md`, `MANIFEST.md`, `PUBLISHING-GPT-STORE.md`, `EVALUATION-CHECKLIST.md`

## Versioning Policy

Use semantic-style versions for the configuration package:

- `v0.x`: initial scaffold;
- `v1.x`: production baseline;
- `v2.x`: agentic wrapper and tool orchestration;
- `v3.x`: security-hardened 20-file package;
- `v4.x`: public-GPT-ready sandbox, artifact, safety, and evaluation upgrade;
- `v5.x`: backed by external eval harness and optional production Actions backend.

## Evolution From v0 To v4

| Version | Theme | Notes |
|---|---|---|
| v0 | Scaffold | Established a Custom GPT knowledge/config concept. |
| v1 | Baseline | Clarified uploaded-file workflows and user-facing purpose. |
| v2 | Agent wrapper | Added protocol-style workflows and tool orchestration. |
| v3 | Hardened pack | Strengthened sandbox boundaries, prompt injection, Actions caveats, and evaluation. |
| v4.0.0 | Public-ready operating layer | Rewrote all 20 files with consistent metadata, stronger Instructions, artifact contract, safety model, and red-team checklist. |
| v4.1.0 | Public-pilot hardening | Adds official OpenAI docs basis, Builder model/capability caveats, pilot launch checklist, and stronger validation for public surfaces. |

## Current Version

`v4.1.0`

Release theme: public-pilot hardening for a production-grade Custom GPT operating wrapper for uploaded files, ZIP archives, sandbox sessions, validation, and public GPT readiness.

## v4.0.0 Foundation

- Instructions-first design.
- Retrieval-friendly 20-file Knowledge architecture.
- Explicit ChatGPT sandbox versus local filesystem boundary.
- Strong ZIP safety and fail-closed behavior.
- Path-only secret hygiene.
- Tool orchestration matrix.
- Optional Actions backend blueprint with raw shell endpoints forbidden.
- Artifact and validation contracts.
- Copy-ready report templates.
- Strong Preview, regression, artifact, and red-team evaluation checklist.
- Public GPT Store publishing guidance.

## v4.1.0 Scope

- Public pilot status made explicit in repository docs.
- Official OpenAI docs basis moved into public `docs/` instead of private session notes.
- Builder model selection guidance added without hard-coding model names.
- Apps/connectors and Actions caveat added across setup, publishing, and capability docs.
- Pilot launch checklist added for first deployment and Preview evidence.
- Workspace validator strengthened for version consistency, public docs, and private-path hygiene.

## Future v4.x Patches

- Add more file-type-specific workflows.
- Add localized onboarding snippets.
- Add smaller Instructions variants if GPT Builder length constraints change.
- Add more example artifacts.
- Add a JSON schema for manifests.
- Add a reusable preview-test worksheet.

## Future v5 Actions Backend

Only pursue when there is a real backend:

1. Threat model.
2. Privacy policy.
3. OpenAPI schema.
4. Authentication.
5. Isolated session storage.
6. Archive scan endpoint.
7. Safe file-read endpoint.
8. Patch plan endpoint.
9. Patch apply endpoint.
10. Artifact build endpoint.
11. Validation endpoint.
12. Audit log endpoint.
13. Rate limits.
14. Artifact expiration.
15. User confirmation gates.

## Future Eval Harness

- Maintain JSONL Preview scenarios.
- Add expected-output rubrics.
- Track regression runs by package version.
- Include adversarial prompt-injection cases.
- Include artifact validation fixtures.
- Record pass/fail history.

## Future Specialized Skill Packs

Possible extensions:

- documentation-only project patching;
- software project audit;
- spreadsheet and data package work;
- prompt-pack publishing;
- academic archive review;
- legal-safe contract intake;
- image/document OCR workflows.

Each extension should preserve sandbox honesty and secret hygiene.

## Rollback Policy

If a release fails critical evaluation, restore the previous validated package and document:

- failed scenario;
- affected files;
- user-visible risk;
- repair plan;
- verification needed.

## Operational Rule

Increase capability only when evaluation evidence shows the current simpler package is insufficient.
