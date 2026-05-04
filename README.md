# GPTsAgent

Canonical development workspace for GPTsAgent.

GPTsAgent is an open project for building a disciplined GPT Builder wrapper around ChatGPT.com sandbox work. The current flagship package is **Sandbox File Operator**: a Custom GPT configuration that makes uploaded file and ZIP archive work more agent-like while staying honest about sandbox boundaries.

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
| `scripts/` | Local validation, instruction extraction, and release ZIP helpers. |
| `docs/` | Contributor workflow, community playbook, roadmap, architecture, release, and maintainer documentation. |
| `.github/` | PR/issue templates, label taxonomy, Dependabot, CODEOWNERS placeholder, and CI for contributions. |

## Published Repositories

GPTsAgent intentionally keeps the public surface small:

| Repository | Role |
|---|---|
| `GPTsAgent/GPTsAgent` | Canonical development workspace and contribution target. |
| `GPTsAgent/.github` | Public organization profile and community health files. |

The 20-file configuration and system instructions live inside this repository as `config/` and `instructions/`.

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
| Examples | `config/EXAMPLES.md`, `config/PROMPT-LIBRARY.md` | Validator plus doc review |
| Evaluation | `config/EVALUATION-CHECKLIST.md` | Validator plus Preview note if run |
| Templates | `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md` | Validator plus template review |
| Labels | `.github/labels.json` | `python3 scripts/sync_labels.py` |

## Contribution Flow

1. Fork `GPTsAgent/GPTsAgent`.
2. Create a branch.
3. Change files in `config/`, `instructions/`, `profile/`, `docs/`, or `scripts/`.
4. Run `python3 scripts/validate_workspace.py`.
5. Open a Pull Request and use the checklist.

The maintainer reviews the PR, confirms validation, and merges accepted changes into the canonical project.

## Development Commands

```bash
python3 scripts/validate_workspace.py
python3 scripts/extract_instructions.py
python3 scripts/build_release_zip.py
python3 scripts/sync_labels.py
```

`scripts/validate_workspace.py` checks:

- `config/` contains exactly the expected 20 Markdown files.
- `instructions/SYSTEM-INSTRUCTIONS.txt` matches the Instructions block in `config/GPT-BUILDER-CONFIG.md`.
- the profile README exists and names the project correctly.
- contributor/community surfaces are present and aligned.
- issue-template labels are defined in `.github/labels.json`.
- no obvious secret-like token was introduced.

## GPT Builder Install

1. Copy the contents of `instructions/SYSTEM-INSTRUCTIONS.txt` into GPT Builder Instructions.
2. Upload exactly the 20 Markdown files from `config/` as Knowledge.
3. Enable file uploads and Code Interpreter/Data Analysis.
4. Run the Preview tests in `config/EVALUATION-CHECKLIST.md`.

## Accepting Contributions

Contributions should come through Pull Requests against `GPTsAgent/GPTsAgent`. A contributor should be able to say: "I made a focused change, validation passes, please review." The maintainer can then review the diff, run the same checks, request changes, or merge.

## Boundary

GPTsAgent does not give ChatGPT direct access to a user's local computer, private repositories, CI, cloud account, or production host. It is an operating layer for uploaded files, sandbox artifacts, and scoped tools inside ChatGPT.com.
