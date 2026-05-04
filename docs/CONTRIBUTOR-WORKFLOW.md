# Contributor Workflow

This is the normal path for external contributors.

## Quick Path

```bash
git clone https://github.com/GPTsAgent/GPTsAgent.git
cd GPTsAgent
python3 scripts/validate_workspace.py
```

You can clone into any directory. The helper scripts derive the project root from their own location and do not depend on a personal local path.

## Discussion First

If you want to talk through an idea before coding, use the public Telegram group:

https://t.me/GPTsAgentChat

Use Telegram for sanitized discussion and coordination. Do not paste secrets or private data. If the idea becomes concrete, move it into a GitHub Issue or Pull Request.

Then:

1. Fork the repository on GitHub.
2. Create a branch from `main`.
3. Make a bounded change.
4. Run `python3 scripts/validate_workspace.py`.
5. Open a Pull Request.
6. Wait for review.

## Fast Conversion Path

| Starting point | Best next step |
|---|---|
| Telegram discussion | Open the Contribution Idea issue template with a sanitized summary. |
| Small docs fix | Open a Pull Request after validation. |
| Safety or validation gap | Open a GitHub Issue first, then patch it. |
| Unclear scope | Ask in Telegram, then write the narrowest issue possible. |

For the full public channel and label model, see `docs/COMMUNITY-PLAYBOOK.md`.

## Good First Contributions

- Improve examples in `config/EXAMPLES.md`.
- Add Preview test cases to `config/EVALUATION-CHECKLIST.md`.
- Clarify sandbox boundary wording.
- Improve contributor docs.
- Add safe, sanitized report templates.
- Improve validation scripts without adding dependencies.
- Add or refine tasks from `docs/ROADMAP.md`.

## Change Rules

- Keep `config/` at exactly 20 Markdown files.
- Do not paste secrets, private keys, cookies, sessions, tokens, or private data.
- Do not claim ChatGPT can directly access a user's local computer.
- Update `instructions/` with `python3 scripts/extract_instructions.py` when the Instructions block changes.
- Use `NOT VERIFIED` for claims that were not actually tested.
- Keep issue-template labels aligned with `.github/labels.json`.

## Pull Request Review

A maintainer should confirm:

- The change is scoped.
- CI passes.
- The PR checklist is complete.
- The change does not weaken archive safety or secret hygiene.
- Any behavior change has evaluation coverage.

## Before Opening A PR

Run the baseline checks:

```bash
python3 scripts/validate_workspace.py
python3 -m py_compile scripts/*.py
python3 scripts/build_release_zip.py
```

If the PR changes labels or issue templates, also run:

```bash
python3 scripts/sync_labels.py
```
