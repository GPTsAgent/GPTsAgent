# Skill Catalog

Version: `v0.3.1`

Purpose: Define public-safe named workflow skills for GPTsAgent, including the trigger, input, output, and validation shape of each reusable skill.

Use this file when: designing, reviewing, or evaluating named workflows, prompt contracts, or skill-like operating patterns for the public GPT.

Related files: `docs/COMMAND-SESSION-PATTERNS.md`, `docs/AGENT-OPERATING-PATTERNS.md`, `config/PROMPT-LIBRARY.md`, `config/EVALUATION-CHECKLIST.md`, `config/CAPABILITIES-MAP.md`

## Core Rule

A skill is a named, bounded workflow contract. It is not a hidden subagent, a background daemon, or an excuse to widen authority.

Public GPTsAgent uses skill-like workflows as a clarity device: the user sees what kind of work is happening, what inputs are allowed, what is blocked, what artifacts to expect, and how the result will be validated.

The public catalog should feel like a visible command menu: small, stable, grouped by user job, and easy to browse. Heavy or experimental behavior belongs behind an explicit trigger or a future reviewed backend design, not hidden inside an unnamed catch-all.

## Instruction Stack

Use this stack when explaining how GPTsAgent operates:

| Layer | Role | Example |
|---|---|---|
| System instructions | Canonical behavior layer. | GPT Builder Instructions. |
| Knowledge files | Retrieval and reference support. | Prompt library, safety policy, examples, skill catalog. |
| User request | The task the user wants done. | "Scan this ZIP." |
| Uploaded evidence | Files, ZIPs, screenshots, or text the user provided. | Source material to inspect. |
| Selected skill | The named workflow contract that fits the task. | `ZIP_PREFLIGHT` or `PROJECT_AUDIT`. |
| Generated artifacts | Reports, diffs, manifests, ZIPs, or handoff notes. | Outputs to download and review. |

## Skill Contract Shape

Every skill should define:

- trigger;
- allowed inputs;
- blocked inputs;
- output contract;
- validation gate;
- handoff rule.

If a skill cannot define those items clearly, it is not ready for public use.

## Public Skill Catalog

| Skill | Trigger | Primary outputs | Validation gate |
|---|---|---|---|
| `READ_ONLY` | The user wants an answer, map, or diagnosis without edits. | Summary, session map, next safe move. | No mutation occurred. |
| `ZIP_PREFLIGHT` | The user uploads or references an archive. | Wrapper root, risk scan, safe mode recommendation. | Unsafe archives fail closed. |
| `PROJECT_AUDIT` | The user wants to understand a project or archive. | Project map, entry points, docs, tests, risks. | Source and assumption boundaries are explicit. |
| `PATCH_ONLY` | The user requests bounded edits. | Patch plan, edited files, diff, manifest. | Only approved files changed. |
| `LIGHT_EXTRACTION` | A safe subset of archive contents is needed. | Safe extracted surfaces, project map, artifact notes. | Secret-sensitive paths stay path-only. |
| `FULL_EXTRACTION` | The archive is safe and broad context is necessary. | Full sandbox working copy and artifact outputs. | Structural safety was checked first. |
| `TEST_ONLY` | The user wants validation without edits. | Test results, status labels, evidence notes. | Tests label what actually ran. |
| `ARTIFACT_BUILD` | The user needs deliverables. | Updated ZIP, diff, manifest, checksum, handoff. | Candidate artifacts validate before release. |
| `REFERENCE_DISTILLATION` | A private reference is supplied for pattern extraction. | Public-safe distilled patterns, no source identity. | No private names, paths, or provenance retained. |
| `REFUSAL_NARROWING` | The request is unsafe, secret-exposing, or over-scoped. | Refusal plus safe alternative. | Unsafe portion is refused first. |

## Selection Rules

1. Choose the least-powerful sufficient skill.
2. Use `READ_ONLY` or `ZIP_PREFLIGHT` before mutation whenever possible.
3. If the task crosses skills, state the primary skill and the supporting checks.
4. If no skill fits, narrow the request or refuse the unsafe portion.
5. Never invent hidden skills, hidden subagents, or background continuation.

## Relationship To Commands And Prompts

- `PROMPT-LIBRARY.md` gives users ready-to-copy requests that select a skill cleanly.
- `COMMAND-SESSION-PATTERNS.md` explains how skills sit inside session state and mode selection.
- `AGENT-OPERATING-PATTERNS.md` explains the public-safe maintainer workflow that inspired this structure.

## Operational Rule

Treat every skill as a testable contract, not as an invisible capability claim.
