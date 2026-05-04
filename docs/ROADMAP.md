# Public Roadmap

Version: `v4.1.0`

Purpose: Give contributors a public-safe roadmap that separates current pilot work from later backend or automation ambitions.

Use this file when: opening good first issues, planning public-pilot work, or deciding whether a proposed feature belongs now, next, later, or not by default.

Related files: `README.md`, `docs/COMMUNITY-PLAYBOOK.md`, `docs/PILOT-LAUNCH-CHECKLIST.md`, `config/VERSIONING-ROADMAP.md`

This roadmap is for contributors. It describes useful public work without promising dates, background execution, production access, or unavailable ChatGPT.com capabilities.

## Current Theme

GPTsAgent is focused on making **Sandbox File Operator** easy to install, validate, review, and improve as an open GPT Builder configuration package.

## Now

These tasks are suitable for near-term issues and pull requests:

- Improve examples in `config/EXAMPLES.md` with realistic, sanitized user dialogues.
- Add Preview and red-team cases to `config/EVALUATION-CHECKLIST.md`.
- Improve contributor docs so first-time contributors can find a bounded task quickly.
- Keep `instructions/SYSTEM-INSTRUCTIONS.txt` synchronized with `config/GPT-BUILDER-CONFIG.md`.
- Improve local validation while keeping the project dependency-free.
- Keep GitHub issue templates aligned with `.github/labels.json`.
- Run the first GPT Builder pilot using `docs/PILOT-LAUNCH-CHECKLIST.md`.
- Keep official OpenAI docs assumptions current in `docs/OFFICIAL-DOCS-BASIS.md`.

## Next

These tasks need more care or maintainer coordination:

- Add a structured Preview test worksheet.
- Add a machine-readable release manifest for generated ZIP artifacts.
- Add more archive-safety examples for edge cases such as symlinks, duplicate paths, traversal, and encrypted entries.
- Add localized onboarding snippets after the English source stays stable.
- Add a small fixture set for validator tests without including private or secret-bearing payloads.

## Later

These are intentionally later because they increase maintenance or safety surface:

- Optional Actions backend design with real OpenAPI schema, authentication, privacy policy, rate limits, and artifact expiration.
- External evaluation harness with JSONL scenarios and expected-output rubrics.
- Specialized skill packs for documentation projects, spreadsheet packages, prompt packs, and software audits.
- Release automation that publishes signed artifacts after maintainer approval.

## Not Planned By Default

- Raw shell Actions.
- Direct access to a user's local filesystem from ChatGPT.com.
- Secret collection or credential inspection workflows.
- Autonomous production-host mutation.
- Package installation as a normal user workflow.
- Unreviewed ingestion of private archives into public issues.

## Good First Issue Template

Use this shape when opening tasks for new contributors:

```text
Goal: <one concrete improvement>
Files: <small file list>
Constraints: no secrets, no sandbox overclaim, no dependency install
Validation: python3 scripts/validate_workspace.py
Expected PR size: small
Labels: good first issue, help wanted, <area>
```

## Roadmap Rule

Move capability forward only when the safety boundary, validation path, and contributor ownership are clear.
