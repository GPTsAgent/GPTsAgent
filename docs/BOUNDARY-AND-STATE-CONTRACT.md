# Boundary And State Contract

Version: `v0.2.0`

Purpose: Define the public repository zones, canonical write targets, generated surfaces, release artifacts, and fail-closed placement rules for GPTsAgent.

Use this file when: adding files, moving content, deciding where a contribution belongs, reviewing generated artifacts, or preventing private/reference material from becoming public project state.

Related files: `README.md`, `AGENTS.md`, `docs/AGENT-OPERATING-PATTERNS.md`, `docs/REPOSITORY-ARCHITECTURE.md`

## Core Rule

Every file must belong to exactly one public repository zone. If a new file does not clearly fit one zone, update this contract before adding the file.

The public GPT consumes this repository as a static Builder package. End users can supply prompts, uploads, and scoped connected sources, but they do not mutate `config/` or `instructions/` from inside ChatGPT.com. Package changes happen through maintainer/admin releases.

## Zone Matrix

| Zone | Root | Purpose | Canonical writes | Do not store |
|---|---|---|---|---|
| Knowledge package | `config/` | The exact 20 Markdown files uploaded to GPT Builder as Knowledge. | Human-reviewed package content only. | Extra files, scratch notes, release ZIPs, private references, logs, caches. |
| Instructions output | `instructions/` | Extracted Builder Instructions generated from `config/GPT-BUILDER-CONFIG.md`. | `scripts/extract_instructions.py` output. | Independent instruction variants that drift from the Builder config. |
| Public docs | `docs/` | Contributor, architecture, launch, threat-model, and maintainer documentation. | Public-safe docs and reviewed process notes. | Private source text, local paths, raw transcripts, secrets, runtime databases. |
| Evaluation fixtures | `eval/` | Machine-readable Preview and red-team scenarios. | Sanitized JSONL eval cases. | Private payloads, real secrets, copied private examples. |
| Automation | `scripts/` | Dependency-free validation, extraction, PR coordination, release packaging, and label tooling. | Small reviewed helper scripts. | Credentialed API behavior by default, destructive automation, package-specific caches. |
| GitHub community | `.github/` | Templates, labels, CODEOWNERS placeholder, Dependabot, and CI. | Public contribution and validation surfaces. | Private coordination, secrets, maintainer-only logs. |
| Release artifacts | `dist/` | Generated ZIP, checksum, and release manifest. | Output from `scripts/build_release_zip.py`. | Source of truth edits, hand-written docs, private reference material. |
| Local generated state | `__pycache__/`, `.release/`, caches | Tool byproducts. | None as source material. | Public docs, Knowledge, secrets, release evidence. |
| Private references | Outside repo or temporary workspace | Pattern-only evidence supplied by a maintainer or user. | None directly. | Names, paths, copied text, logs, examples, provenance. |

## Write Rules

- `config/` stays exactly 20 Markdown files.
- `instructions/` is generated from `config/GPT-BUILDER-CONFIG.md`.
- `docs/` may explain process, but must not become a dumping ground for private reference extracts.
- `eval/` contains sanitized prompts only.
- `dist/` is generated and validated; do not hand-edit it as source truth.
- `.github/workflows/` should not be touched when open dependency workflow PRs already own that surface unless the task is explicitly about workflows.

## Evidence Rules

Treat evidence sources separately:

- current repository files are source evidence;
- open PRs are coordination evidence;
- old validation reports are historical evidence;
- generated release artifacts are candidate output until validated;
- private references are pattern-only evidence;
- user claims and AI answers are context, not proof.

Do not average contradictions. Prefer current files, validator output, release manifests, and explicit maintainer decisions over older prose.

## Placement Protocol

Before adding or moving a file:

1. Identify the zone.
2. Confirm whether the zone allows canonical writes.
3. Check whether the file changes the 20-file Knowledge package.
4. Check open PR overlap.
5. Check whether the content contains private or secret-like material.
6. Add validation coverage when behavior changes.
7. Update `docs/REPOSITORY-ARCHITECTURE.md` or this contract if the zone model changes.

If the zone is unclear, mark the placement `NOT VERIFIED` and stop before creating the file.

## Release State Contract

A release candidate is valid only when:

- `config/` still has exactly 20 Markdown files;
- extracted instructions match the Builder config;
- eval fixtures validate;
- release ZIP opens;
- release manifest matches the ZIP;
- checksum matches the ZIP;
- private-marker scan passes;
- no secret-like tokens were introduced.

## Operational Rule

Do not let generated output, historical evidence, private references, or ambiguous file placement silently become canonical project truth.
