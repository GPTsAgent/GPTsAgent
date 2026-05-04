# Contributing

GPTsAgent contributions should improve the Sandbox File Operator package without weakening sandbox honesty, archive safety, secret hygiene, or validation discipline.

## Ground Rules

- Keep `config/` at exactly 20 Markdown Knowledge files unless the manifest and validator are deliberately changed.
- Do not add real secrets, tokens, private keys, cookies, sessions, or credential bodies.
- Keep local-machine, production, CI, cloud, and host claims honest. Use `NOT VERIFIED` when evidence is missing.
- Prefer bounded changes over broad rewrites.
- Preserve the GPT Builder boundary: this project configures ChatGPT sandbox behavior; it does not give ChatGPT direct access to a user's computer.

## Community Path

- For quick discussion or coordination, use the public Telegram group: https://t.me/GPTsAgentChat
- For tracked work, open a GitHub Issue with sanitized details.
- If an idea starts in Telegram, use the Contribution Idea issue template to turn it into a durable GitHub record.
- For implementation, open a Pull Request against `GPTsAgent/GPTsAgent`.
- Keep Telegram messages and GitHub reports free of secrets and private data.
- If the change touches issue labels, keep them aligned with `.github/labels.json`.

## Easy Starts

- Fix unclear README, contributor, support, or profile wording.
- Improve safe examples in `config/EXAMPLES.md`.
- Add Preview or red-team cases to `config/EVALUATION-CHECKLIST.md`.
- Improve issue or PR templates so contributors provide better evidence.
- Improve local validation without adding runtime dependencies.
- Sync missing labels or improve label descriptions through the label taxonomy file.
- Improve the pilot launch checklist and official docs basis after real Builder runs.

## Change Types

- Documentation and examples: update the relevant Knowledge file and validation checklist if behavior changes.
- Safety policy: update tests, refusal examples, and artifact language together.
- Builder instructions: keep the ready-to-copy Instructions block compact enough for GPT Builder editing.
- Automation: keep workflows read-only by default and avoid actions that require repository secrets unless clearly justified.

## Local Checks

Run:

```bash
python3 scripts/validate_workspace.py
python3 -m py_compile scripts/*.py
python3 scripts/sync_labels.py
```

If network access is unavailable, label GitHub/API checks as `NOT RUN` or `TIMEOUT`.
