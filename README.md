# GPTsAgent

Canonical development workspace for GPTsAgent.

GPTsAgent is an open project for building a disciplined GPT Builder wrapper around ChatGPT.com sandbox work. The current flagship package is **Sandbox File Operator**: a Custom GPT configuration that makes uploaded file and ZIP archive work more agent-like while staying honest about sandbox boundaries.

Current package version: `v0.3.0`.

This repository is a public pilot. It is intended to be cloneable, reviewable, and easy for contributors to improve without confusing it with a private host-level project.

## One-Click Download

Download the full working directory as a ZIP:

```text
https://github.com/GPTsAgent/GPTsAgent/archive/refs/heads/main.zip
```

Or clone it:

```bash
git clone https://github.com/GPTsAgent/GPTsAgent.git
cd GPTsAgent
python3 scripts/validate_workspace.py
```

No dependency installation is required for the core checks. Python 3.10+ and Git are enough. `make` targets are provided as shortcuts, but they are optional.

## Repository Map

| Path | Purpose |
|---|---|
| `config/` | The exact 20 Markdown Knowledge files for GPT Builder. |
| `instructions/` | The canonical system Instructions block extracted from `config/GPT-BUILDER-CONFIG.md`. |
| `profile/` | Organization profile README source for `GPTsAgent/.github`. |
| `scripts/` | Local PR coordination, validation, instruction extraction, and release ZIP helpers. |
| `docs/` | Contributor workflow, community playbook, boundary/state contract, agent operating patterns, command/session patterns, skill catalog, model selection, roadmap, architecture, release, and maintainer documentation. See `docs/BOUNDARY-AND-STATE-CONTRACT.md`, `docs/COMMAND-SESSION-PATTERNS.md`, and `docs/SKILL-CATALOG.md`. |
| `eval/` | Machine-readable Preview and red-team scenario fixtures. |
| `.github/` | PR/issue templates, label taxonomy, Dependabot, CODEOWNERS placeholder, and CI for contributions. |
| `AGENTS.md` | Repo-local rules for AI agents and contributor automation. |

## Published Repositories

GPTsAgent intentionally keeps the public surface small:

| Repository | Role |
|---|---|
| `GPTsAgent/GPTsAgent` | Canonical development workspace and contribution target. |
| `GPTsAgent/.github` | Public organization profile and community health files. |

The 20-file configuration and system instructions live inside this repository as `config/` and `instructions/`.

## Pilot Status

- Public open-source pilot for ChatGPT.com Custom GPT configuration work.
- Validated as a 20-file Knowledge pack plus local release tooling.
- Builder and publishing choices should be rechecked at release time because OpenAI docs and GPT Builder constraints can change.

## Static Package Model

From the user's perspective, the deployed GPT is a static configuration package. The 20 Knowledge files and the GPT Builder Instructions are uploaded by a maintainer or admin during a release, then used as versioned runtime guidance inside ChatGPT.com.

End users do not edit those 20 files from inside the GPT session. When behavior needs to change, the maintainer updates the repository package, regenerates the Instructions export, and publishes a new reviewed release.

## Community

- Public Telegram group for discussion and coordination: https://t.me/GPTsAgentChat
- Use Telegram for quick, sanitized discussion, idea triage, and contributor coordination.
- Use GitHub Issues for tracked bugs, safety reports, and documentable change requests.
- Use the Contribution Idea issue template when a Telegram discussion should become tracked work.
- Use Pull Requests for actual changes.
- Do not post secrets, private keys, cookies, sessions, tokens, or private data in Telegram or GitHub.

## Contributor Quickstart

Pick one small lane:

| Lane | Best files | Validation |
|---|---|---|
| Docs clarity | `README.md`, `CONTRIBUTING.md`, `docs/` | `python3 scripts/validate_workspace.py` |
| Boundary/state contract | `docs/BOUNDARY-AND-STATE-CONTRACT.md`, `docs/REPOSITORY-ARCHITECTURE.md` | Validator plus release artifact validation |
| Examples | `config/EXAMPLES.md`, `config/PROMPT-LIBRARY.md` | Validator plus doc review |
| Evaluation | `config/EVALUATION-CHECKLIST.md`, `eval/`, `docs/PREVIEW-TEST-MATRIX.md` | `python3 scripts/validate_eval_fixtures.py` plus Preview note if run |
| Agent operations | `AGENTS.md`, `docs/AGENT-OPERATING-PATTERNS.md`, `docs/MAINTAINER-REVIEW.md` | Open PR check plus validator |
| Model selection | `docs/MODEL-SELECTION.md`, `docs/PILOT-LAUNCH-CHECKLIST.md` | Builder settings record plus Preview note if run |
| Reference distillation | `docs/REFERENCE-DISTILLATION-POLICY.md`, `config/FILE-WORKFLOW.md`, `config/EXAMPLES.md` | `python3 scripts/validate_workspace.py` plus private-marker scan |
| Templates | `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md` | Validator plus template review |
| Labels | `.github/labels.json` | `python3 scripts/sync_labels.py` |

## Contribution Flow

1. Fork `GPTsAgent/GPTsAgent`.
2. Create a branch.
3. Run `python3 scripts/check_open_prs.py` and avoid overlapping open PRs.
4. Change files in `config/`, `instructions/`, `profile/`, `docs/`, or `scripts/`.
5. Run `python3 scripts/validate_workspace.py`.
6. Open a Pull Request and use the checklist.

The maintainer reviews the PR, confirms validation, and merges accepted changes into the canonical project.

## Development Commands

```bash
python3 scripts/check_open_prs.py
python3 scripts/validate_workspace.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/extract_instructions.py
python3 scripts/build_release_zip.py
python3 scripts/validate_release_artifacts.py
python3 scripts/prepublish_audit.py
python3 scripts/sync_labels.py
make prework
make check
make prepublish-audit
```

`scripts/validate_workspace.py` checks:

- `config/` contains exactly the expected 20 Markdown files.
- `instructions/SYSTEM-INSTRUCTIONS.txt` matches the Instructions block in `config/GPT-BUILDER-CONFIG.md`.
- the profile README exists and names the project correctly.
- contributor/community surfaces are present and aligned.
- repo-local `AGENTS.md` and the open PR checker are present.
- public-safe agent operating patterns are present.
- boundary/state contract is present and aligned with repository zones.
- eval fixtures, Preview matrix, and threat model are present.
- the private-reference distillation policy is present and connected to eval coverage.
- release ZIP artifacts can be validated after packaging.
- prepublish audit can combine PR coordination, validation, release checks, private-marker scans, secret-like scans, and git-history scan.
- issue-template labels are defined in `.github/labels.json`.
- no obvious secret-like token was introduced.

## GPT Builder Install

1. Copy the contents of `instructions/SYSTEM-INSTRUCTIONS.txt` into GPT Builder Instructions.
2. Upload exactly the 20 Markdown files from `config/` as Knowledge.
3. Choose the current available GPT Builder model and re-check it before publishing.
4. Enable file uploads and Code Interpreter/Data Analysis.
5. If you enable Apps/connectors, do not enable Actions in the same GPT.
6. Run the Preview tests in `config/EVALUATION-CHECKLIST.md`, `docs/PREVIEW-TEST-MATRIX.md`, and `docs/PILOT-LAUNCH-CHECKLIST.md`.

## Accepting Contributions

Contributions should come through Pull Requests against `GPTsAgent/GPTsAgent`. A contributor should be able to say: "I made a focused change, validation passes, please review." The maintainer can then review the diff, run the same checks, request changes, or merge.

## Boundary

GPTsAgent does not give ChatGPT direct access to a user's local computer, private repositories, CI, cloud account, or production host. It is an operating layer for uploaded files, sandbox artifacts, and scoped tools inside ChatGPT.com.

Private archives, projects, or transcripts can be used only as temporary pattern input under `docs/REFERENCE-DISTILLATION-POLICY.md`. Public files must not preserve private names, paths, examples, logs, source text, or provenance.
