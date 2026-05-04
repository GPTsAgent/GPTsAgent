# Maintainer Review

Use this checklist before accepting contributions.

## Review Checklist

- The change has a clear purpose.
- Root package structure remains intentional.
- `config/` still has exactly 20 Markdown files.
- `instructions/SYSTEM-INSTRUCTIONS.txt` matches `config/GPT-BUILDER-CONFIG.md`.
- No secrets or private data are present.
- Sandbox boundaries are not overclaimed.
- Unsafe archive behavior still fails closed.
- Evaluation coverage matches behavior changes.
- CI passes.
- If the change came from Telegram discussion, the durable context is summarized in the issue or PR.
- Issue-template labels are defined in `.github/labels.json`.
- New contributor tasks have clear files, constraints, and validation.

Local command:

```bash
python3 scripts/validate_workspace.py
python3 scripts/sync_labels.py
```

## Merge Decision

Use:

- `accepted`: ready to merge.
- `needs changes`: contributor should revise.
- `out of scope`: useful idea, wrong repository or timing.
- `unsafe`: weakens secret hygiene, archive safety, or sandbox honesty.

## Label Sync

Before or after merging community/template changes, run a dry run:

```bash
python3 scripts/sync_labels.py
```

If labels are missing and maintainer credentials are available:

```bash
GH_TOKEN=<TOKEN> python3 scripts/sync_labels.py --apply
```

Do not paste token values into issues, pull requests, logs, or release notes.

## After Merge

Run the release process if a public release ZIP or organization profile update is needed.
