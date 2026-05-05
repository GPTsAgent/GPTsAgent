# Agent Operating Patterns

Version: `v0.2.0`

Purpose: Capture public-safe maintainer-agent patterns distilled from private local agent tooling without copying private paths, project names, logs, or source text.

Use this file when: improving GPTsAgent contributor workflows, AI-agent maintenance rules, review processes, or validation discipline.

Related files: `AGENTS.md`, `CONTRIBUTING.md`, `docs/CONTRIBUTOR-WORKFLOW.md`, `docs/MAINTAINER-REVIEW.md`

## Core Rule

Private maintainer tooling may inspire GPTsAgent's public process, but only general operating patterns may enter the repository. Do not publish private paths, project names, session logs, shell history, local runtime state, credentials, or copied instruction text.

## Patterns To Adopt

| Pattern | Public GPTsAgent form |
|---|---|
| Layered read order | Start with repo `AGENTS.md`, then `README.md`, contributor docs, and only the files relevant to the change. |
| Short session card | Keep a compact task brief: scope, source, protected surfaces, intended outputs, validation, and unknowns. |
| Safe-surface map | Separate human-readable docs from runtime state, caches, logs, credentials, generated outputs, and release artifacts. |
| Boundary contract | Define which repository zones are canonical write targets and fail closed when placement is unclear. |
| Curated skills | Prefer a small list of named workflows over a dump of every possible agent behavior. |
| Historical evidence boundary | Treat old logs, old reports, and previous sessions as evidence, not current truth. |
| Targeted validation | Validate the changed surface early and narrowly before running broader release checks. |
| Opposite-lane review | Use adversarial review for safety-sensitive changes without letting the reviewer edit the work under review. |
| Bounded lanes | Split work only when lanes are concrete, disjoint, and have clear return contracts. |
| Distill, do not sprawl | Move durable lessons into the right public doc and delete or ignore scratch detail. |

## Safe Session Card

Use this compact shape for non-trivial maintainer or AI-agent work:

```text
Task:
Scope:
Files likely touched:
Protected surfaces:
Private references:
Open PR overlap:
Validation:
Artifacts:
Unknowns:
```

Rules:

- `Private references` should say `none`, `public`, or `private pattern-only`.
- `Protected surfaces` should include secrets, auth, logs, caches, generated dependency folders, and any open PR-owned files.
- File placement should follow `docs/BOUNDARY-AND-STATE-CONTRACT.md`.
- `Unknowns` should use `NOT VERIFIED` when the evidence is missing.

## Skill Contract Shape

Reusable workflows should have:

- trigger;
- allowed inputs;
- blocked inputs;
- read order;
- allowed tools or commands;
- prohibited tools or commands;
- output contract;
- validation gate;
- handoff rule.

This keeps agent behavior testable without pretending the repository contains autonomous subagents.

## Private Reference Intake

When a private local directory, archive, log, or tool cache is used only for inspiration:

1. Inspect filenames and safe documentation surfaces first.
2. Skip credentials, auth files, database files, logs, session transcripts, shell snapshots, caches, and raw histories unless the user explicitly asks for targeted forensic inspection.
3. Read only the minimum safe material needed to extract patterns.
4. Rewrite from scratch in public-safe language.
5. Validate that no private names, paths, source text, logs, or provenance were introduced.
6. Record the work as `private pattern-only` if mentioned in public-facing handoff.

## Review Lanes

Use these lanes for larger changes:

| Lane | Purpose | Must not do |
|---|---|---|
| Primary edit | Make the bounded change. | Expand into unrelated files. |
| Validation | Run deterministic checks and package artifacts. | Treat skipped checks as `PASS`. |
| Adversarial review | Search for failures, overclaims, missing tests, and private leaks. | Edit files or rubber-stamp the work. |
| Release evidence | Confirm ZIP, manifest, checksum, and Preview matrix state. | Publish without maintainer approval. |

## Operational Rule

Adopt local agent practice as public process only after it is rewritten, bounded, validated, and stripped of private provenance.
