# AGENTS.md

Purpose: Repo-local operating guide for AI coding agents and human contributors working on GPTsAgent.

Use this file when: an AI agent, maintainer, or contributor is about to inspect, edit, validate, package, or publish this repository.

Related files: `README.md`, `CONTRIBUTING.md`, `docs/CONTRIBUTOR-WORKFLOW.md`, `docs/MAINTAINER-REVIEW.md`, `scripts/check_open_prs.py`

## Project Boundary

GPTsAgent is a public open-source project for Custom GPT configuration work. Its flagship package, Sandbox File Operator, is an operating wrapper for ChatGPT.com uploaded-file and ZIP workflows.

This repository is not a trained model, not a local desktop agent, not a remote shell, and not a production automation backend. Do not add claims that ChatGPT.com can directly access a user's local filesystem.

## First Steps Before Any Edit

Before changing files, perform this coordination preflight:

1. Confirm the repository root with `git rev-parse --show-toplevel`.
2. Inspect local state with `git status --short --branch`.
3. Refresh read-only remote state with `git fetch --prune origin` when network access is available.
4. Check open Pull Requests with `python3 scripts/check_open_prs.py`.
5. Compare open PR touched files with the files you intend to edit.
6. If an open PR owns the same files or tightly related surfaces, stop, narrow the work, or report the conflict before editing.
7. If GitHub or network access is unavailable, mark the PR check as `NOT RUN`, `TIMEOUT`, or `NOT VERIFIED` in the handoff.

Open PRs are not automatically blockers. They are coordination evidence. The blocker is overlapping ownership, especially on safety policy, Builder Instructions, validation scripts, release tooling, and GitHub workflows.

## Current Ownership Rules

- Keep `config/` at exactly 20 Markdown files.
- Treat `config/GPT-BUILDER-CONFIG.md` as the source for the canonical Instructions block.
- Run `python3 scripts/extract_instructions.py` after changing `config/GPT-BUILDER-CONFIG.md`.
- Keep `instructions/SYSTEM-INSTRUCTIONS.txt` and `instructions/INSTRUCTIONS.md` synchronized.
- Do not edit `.github/workflows/validate.yml` when an open dependency or workflow PR already touches GitHub Actions unless the task is explicitly about workflows.
- Keep contributor docs, PR templates, and validation scripts aligned when changing contribution flow.
- Do not create commits, tags, pushes, releases, or label mutations unless the maintainer explicitly requested that operation.

## Safety Rules

- Do not add secrets, tokens, private keys, cookies, sessions, credential bodies, or private data.
- Do not add examples that look like real credentials. Use placeholders such as `<API_KEY>`, `<PROJECT_ZIP>`, and `<SANDBOX_ROOT>`.
- Do not mention private host paths, personal token-file paths, or private project names.
- Do not weaken archive fail-closed behavior, prompt-injection resistance, secret hygiene, or sandbox boundary wording.
- Do not tell users to upload secrets.
- Do not introduce runtime dependencies unless the maintainer explicitly accepts the tradeoff.

## Expected Read Path

For normal repository work, read:

1. `README.md`
2. `CONTRIBUTING.md`
3. `docs/AGENT-OPERATING-PATTERNS.md`
4. `docs/BOUNDARY-AND-STATE-CONTRACT.md`
5. `docs/CONTRIBUTOR-WORKFLOW.md`
6. `docs/REPOSITORY-ARCHITECTURE.md`
7. the specific `config/`, `docs/`, `scripts/`, `instructions/`, or `.github/` files you will touch

For safety-sensitive behavior, also read:

- `config/SANDBOX.md`
- `config/ZIP-SAFETY-POLICY.md`
- `config/SECRET-HYGIENE.md`
- `config/SAFETY-REFUSAL-POLICY.md`
- `config/EVALUATION-CHECKLIST.md`

## Validation

Run the narrowest useful checks before handoff:

```bash
python3 scripts/check_open_prs.py
python3 scripts/validate_workspace.py
python3 -m py_compile scripts/*.py
python3 scripts/build_release_zip.py
```

If labels or issue templates changed, also run:

```bash
python3 scripts/sync_labels.py
```

Use only these status labels in reports: `PASS`, `PARTIAL`, `FAILED`, `SKIPPED`, `NOT RUN`, `NOT VERIFIED`, `TIMEOUT`.

## Done Means

A repository update is done only when:

- open PR coordination was checked or explicitly marked;
- changed files are scoped and documented;
- the 20-file Knowledge package remains intact;
- generated instructions are synchronized when needed;
- validation ran or limitations are reported honestly;
- no secrets or private host references were introduced;
- the maintainer has enough evidence to review the final diff.

## Operational Rule

Coordinate before editing, preserve the sandbox boundary, validate before handoff, and leave final project direction to maintainer review.
