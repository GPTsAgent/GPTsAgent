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

Local command:

```bash
python3 scripts/validate_workspace.py
```

## Merge Decision

Use:

- `accepted`: ready to merge.
- `needs changes`: contributor should revise.
- `out of scope`: useful idea, wrong repository or timing.
- `unsafe`: weakens secret hygiene, archive safety, or sandbox honesty.

## After Merge

Run the release process if a public release ZIP or organization profile update is needed.
