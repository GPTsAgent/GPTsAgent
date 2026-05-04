# Versioning Roadmap

Version: `v0.1.0`

Purpose: Document the public package version, pre-1.0 policy, future Actions backend, future eval harness, and specialized skill packs.

Use this file when: tracking release history, future scope, or public update notes.

Related files: `README.md`, `MANIFEST.md`, `PUBLISHING-GPT-STORE.md`, `EVALUATION-CHECKLIST.md`

## Versioning Policy

Use semantic-style versions for the configuration package.

This public repository starts at `v0.1.0` because GPTsAgent is an early public pilot that should receive many reviewed commits before a stable `v1.0.0` promise. Pre-1.0 versions may still change wording, templates, and validation expectations, but every change should preserve sandbox honesty, archive safety, secret hygiene, and the 20-file Knowledge boundary.

| Range | Meaning | Change expectation |
|---|---|---|
| `v0.1.x` | Public-pilot baseline | Documentation, contributor flow, validation, packaging, and Preview evidence. |
| `v0.2.x` | Workflow hardening | Better examples, compare/update flows, artifact manifests, and edge-case ZIP policies. |
| `v0.3.x` | Evaluation expansion | Structured Preview worksheets, adversarial fixtures, regression records, and release evidence. |
| `v0.4.x` | Integration design | Optional Actions backend design remains design-only until real infrastructure exists. |
| `v1.0.0` | Stable public baseline | Publish only after repeatable Preview results, mature contributor process, and maintainer signoff. |

## Current Version

`v0.1.0`

Release theme: public-pilot hardening for a production-grade Custom GPT operating wrapper for uploaded files, ZIP archives, sandbox sessions, validation, and public GPT readiness.

## v0.1.0 Scope

- Public pilot status made explicit in repository docs.
- Official OpenAI docs basis moved into public `docs/`.
- Builder model selection guidance added without hard-coding model names.
- Apps/connectors and Actions caveat added across setup, publishing, and capability docs.
- Pilot launch checklist added for first deployment and Preview evidence.
- Workspace validator strengthened for version consistency, public docs, and private-path hygiene.
- Contributor workflow clarified for open-source review, PR coordination, and AI-agent-assisted edits.

## Near-Term Public Work

- Keep `instructions/SYSTEM-INSTRUCTIONS.txt` synchronized with `config/GPT-BUILDER-CONFIG.md`.
- Expand `config/EXAMPLES.md` with sanitized realistic dialogues and artifact handoffs.
- Add more Preview and red-team cases to `config/EVALUATION-CHECKLIST.md`.
- Add a structured Preview test worksheet under `docs/` without adding runtime dependencies.
- Improve release ZIP manifesting and checksum evidence.
- Keep contributor docs aligned with `AGENTS.md`, open PR checks, and maintainer review.

## Future Actions Backend

Actions remain off by default. Only pursue a backend when there is real infrastructure and a maintainer-approved threat model:

1. Privacy policy.
2. OpenAPI schema.
3. Authentication.
4. Isolated session storage.
5. Archive scan endpoint.
6. Safe file-read endpoint.
7. Patch plan endpoint.
8. Patch apply endpoint.
9. Artifact build endpoint.
10. Validation endpoint.
11. Audit log endpoint.
12. Rate limits.
13. Artifact expiration.
14. User confirmation gates.

Raw shell endpoints are not part of the roadmap.

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

Do not call GPTsAgent stable until the public pilot has repeatable Preview evidence, contributor review flow, and maintainer-approved release checks.
