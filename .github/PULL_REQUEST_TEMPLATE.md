# Pull Request

## Summary

Describe the change and why it is needed.

If this PR came from a Telegram discussion, include the sanitized context or link the GitHub issue that tracks it.

## Scope

- [ ] Root 20-file Knowledge package
- [ ] GPT Builder Instructions
- [ ] Safety or refusal policy
- [ ] ZIP/archive workflow
- [ ] Artifact or validation contract
- [ ] GitHub/community automation
- [ ] Issue labels or templates
- [ ] Local helper scripts

## Safety Checklist

- [ ] No real secrets, tokens, keys, cookies, sessions, or credential bodies are included.
- [ ] No local filesystem, CI, cloud, host, or production access is overclaimed.
- [ ] Root Markdown file count remains intentional.
- [ ] Secret-sensitive paths are handled by path name only.
- [ ] Unsafe archive behavior fails closed.
- [ ] New or changed behavior has matching evaluation coverage.

## Validation

- [ ] `python3 scripts/validate_workspace.py`
- [ ] `python3 -m py_compile scripts/*.py`
- [ ] `python3 scripts/build_release_zip.py`, if packaging changed
- [ ] `python3 scripts/sync_labels.py`, if labels or issue templates changed
- [ ] GPT Builder Preview test, if behavior changed
- [ ] Not run, with reason:

## Notes

Add limitations, follow-up work, or `NOT VERIFIED` claims here.
