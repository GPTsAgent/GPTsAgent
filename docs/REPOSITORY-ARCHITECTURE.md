# Repository Architecture

GPTsAgent uses one canonical development repository plus one organization profile repository.

## Canonical Development Repository

`GPTsAgent/GPTsAgent` is the source of truth for development, issues, pull requests, validation, and releases.

It contains:

- `config/`: 20 GPT Builder Knowledge files.
- `instructions/`: system Instructions extracted from `config/GPT-BUILDER-CONFIG.md`.
- `profile/`: organization profile source.
- `scripts/`: PR coordination, validation, and packaging tools.
- `docs/`: contributor and maintainer guidance.
- `eval/`: machine-readable Preview and red-team scenario fixtures.
- `.github/labels.json`: source-of-truth label taxonomy for issue templates and triage.
- `AGENTS.md`: repo-local operating rules for AI agents and contributor automation.

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
| `AGENTS.md` | AI-agent preflight, ownership, validation, and safety rules. |
| `docs/AGENT-OPERATING-PATTERNS.md` | Public-safe patterns for AI-assisted maintainer work, skill contracts, and private-reference intake. |
| `docs/COMMAND-SESSION-PATTERNS.md` | Public-safe distillation of mode catalogs, session maps, task states, and permission ladders. |
| `docs/SKILL-CATALOG.md` | Public-safe catalog of named skills, prompt contracts, and selection rules. |
| `docs/BOUNDARY-AND-STATE-CONTRACT.md` | Repository zone contract, canonical write targets, generated surfaces, and release state rules. |
| `docs/CONTRIBUTOR-WORKFLOW.md` | Step-by-step first contribution path. |
| `docs/COMMUNITY-PLAYBOOK.md` | Channel rules, Telegram-to-GitHub conversion, label model, and triage. |
| `docs/OFFICIAL-DOCS-BASIS.md` | Official OpenAI source notes for Builder, Knowledge, Actions, Data Analysis, and publishing assumptions. |
| `docs/GPTS-CURRENT-DOCS-DOSSIER.md` | Current official OpenAI GPTs documentation dossier for Builder fields, capabilities, Apps, Actions, privacy, and publishing. |
| `docs/GPTS-PROFESSIONAL-CONTEXT-REVIEW.md` | Professional, academic, security, governance, and enterprise-adoption context for GPTs roadmap and eval design. |
| `docs/MODEL-SELECTION.md` | Maintainer guidance for Codex-local model preferences versus public ChatGPT Builder evidence. |
| `docs/PILOT-LAUNCH-CHECKLIST.md` | First public GPT Builder pilot checklist and evidence record. |
| `docs/PREVIEW-TEST-MATRIX.md` | Manual Preview worksheet tied to machine-readable eval scenarios. |
| `docs/REFERENCE-DISTILLATION-POLICY.md` | Rules for learning from private references without copying, naming, or preserving private source material. |
| `docs/THREAT-MODEL.md` | Safety assumptions, trust boundaries, abuse cases, and mitigations. |
| `docs/ROADMAP.md` | Public-safe backlog themes and good-first-issue shape. |
| `.github/ISSUE_TEMPLATE/` | Structured bug, safety, validation, package, docs, and contribution idea reports. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Required safety and validation checklist. |
| `.github/labels.json` | Desired public issue label set. |
| `scripts/check_open_prs.py` | Read-only GitHub PR coordination check. |
| `scripts/prepublish_audit.py` | Maintainer prepublish audit combining PR coordination, validators, release artifact checks, private-marker scans, secret-like scans, and git-history scan. |
| `scripts/validate_eval_fixtures.py` | Dependency-free validator for `eval/preview-scenarios.jsonl`. |
| `scripts/validate_release_artifacts.py` | Dependency-free validator for release ZIP, checksum, and release manifest. |

## Invariant

The `config/` directory must remain a clean 20-file Knowledge package. Tooling, profile files, contributor docs, and release machinery must stay outside `config/`.

Private reference material must also stay outside `config/`, `eval/`, release artifacts, examples, and public issue/PR text. Only rewritten public-safe patterns may enter the repository.
