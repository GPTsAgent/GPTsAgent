# Contributor Workflow

This is the normal path for external contributors.

## Quick Path

```bash
git clone https://github.com/GPTsAgent/GPTsAgent.git
cd GPTsAgent
python3 scripts/check_open_prs.py
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
3. Check open Pull Requests and avoid overlapping work.
4. Make a bounded change.
5. Run `python3 scripts/validate_workspace.py`.
6. Open a Pull Request.
7. Wait for review.

## Fast Conversion Path

| Starting point | Best next step |
|---|---|
| Telegram discussion | Open the Contribution Idea issue template with a sanitized summary. |
| Small docs fix | Open a Pull Request after validation. |
| New file or directory | Check `docs/BOUNDARY-AND-STATE-CONTRACT.md` before adding it. |
| Safety or validation gap | Open a GitHub Issue first, then patch it. |
| Private reference input | Follow `docs/REFERENCE-DISTILLATION-POLICY.md`; do not paste the reference or source identity into public issues. |
| AI-agent workflow change | Check `docs/AGENT-OPERATING-PATTERNS.md` and keep the workflow bounded, validated, and public-safe. |
| Mode or session-state change | Check `docs/COMMAND-SESSION-PATTERNS.md` and add Preview coverage when behavior changes. |
| Skill catalog or named workflow change | Check `docs/SKILL-CATALOG.md` and add prompt and eval coverage. |
| Unclear scope | Ask in Telegram, then write the narrowest issue possible. |
| GPT Builder or launch change | Check `docs/OFFICIAL-DOCS-BASIS.md` and update `docs/PILOT-LAUNCH-CHECKLIST.md` if needed. |

For the full public channel and label model, see `docs/COMMUNITY-PLAYBOOK.md`.

## Good First Contributions

- Improve examples in `config/EXAMPLES.md`.
- Add Preview test cases to `config/EVALUATION-CHECKLIST.md`.
- Add machine-readable Preview scenarios to `eval/preview-scenarios.jsonl`.
- Improve the Preview worksheet in `docs/PREVIEW-TEST-MATRIX.md`.
- Clarify sandbox boundary wording.
- Improve contributor docs.
- Clarify mode catalog, session map, or permission-boundary wording in `docs/COMMAND-SESSION-PATTERNS.md`.
- Add safe, sanitized report templates.
- Improve validation scripts without adding dependencies.
- Add or refine tasks from `docs/ROADMAP.md`.
- Improve skill catalog or named workflow contracts in `docs/SKILL-CATALOG.md`.
- Improve the pilot launch checklist after real GPT Builder Preview runs.

## Change Rules

- Keep `config/` at exactly 20 Markdown files.
- Place new files only in the zone defined by `docs/BOUNDARY-AND-STATE-CONTRACT.md`.
- Check open PRs before editing and stop or narrow the work if another PR owns the same files.
- Do not paste secrets, private keys, cookies, sessions, tokens, or private data.
- Do not paste private reference source text, names, paths, logs, examples, or provenance into public issues, PRs, fixtures, or docs.
- Do not paste local agent logs, shell snapshots, model caches, auth state, or runtime databases into public issues, PRs, fixtures, or docs.
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
python3 scripts/check_open_prs.py
python3 scripts/validate_workspace.py
python3 scripts/validate_eval_fixtures.py
python3 -m py_compile scripts/*.py
python3 scripts/build_release_zip.py
python3 scripts/validate_release_artifacts.py
python3 scripts/prepublish_audit.py
```

If the PR changes labels or issue templates, also run:

```bash
python3 scripts/sync_labels.py
```
