# Repository Architecture

GPTsAgent uses one canonical development repository plus one organization profile repository.

## Canonical Development Repository

`GPTsAgent/GPTsAgent` is the source of truth for development, issues, pull requests, validation, and releases.

It contains:

- `config/`: 20 GPT Builder Knowledge files.
- `instructions/`: system Instructions extracted from `config/GPT-BUILDER-CONFIG.md`.
- `profile/`: organization profile source.
- `scripts/`: validation and packaging tools.
- `docs/`: contributor and maintainer guidance.
- `.github/labels.json`: source-of-truth label taxonomy for issue templates and triage.

## Organization Profile Repository

`GPTsAgent/.github` exists for the public organization profile and community health defaults.

## Why This Way

The project is easier to develop when everything lives in one cloneable workspace. Users get the full working directory from `GPTsAgent/GPTsAgent`; the organization profile stays in `GPTsAgent/.github` because GitHub requires that repository name for organization profiles.

Contributors should open PRs against `GPTsAgent/GPTsAgent`.

## Community Channel

Public discussion and quick contributor coordination happen in the Telegram group:

https://t.me/GPTsAgentChat

Use it for sanitized conversation, not for secrets or unreviewed production claims. GitHub Issues and Pull Requests remain the permanent record for tracked work.

## Contributor Surfaces

| Surface | Purpose |
|---|---|
| `CONTRIBUTING.md` | Short rules and baseline commands. |
| `docs/CONTRIBUTOR-WORKFLOW.md` | Step-by-step first contribution path. |
| `docs/COMMUNITY-PLAYBOOK.md` | Channel rules, Telegram-to-GitHub conversion, label model, and triage. |
| `docs/ROADMAP.md` | Public-safe backlog themes and good-first-issue shape. |
| `.github/ISSUE_TEMPLATE/` | Structured bug, safety, validation, package, docs, and contribution idea reports. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Required safety and validation checklist. |
| `.github/labels.json` | Desired public issue label set. |

## Invariant

The `config/` directory must remain a clean 20-file Knowledge package. Tooling, profile files, contributor docs, and release machinery must stay outside `config/`.
