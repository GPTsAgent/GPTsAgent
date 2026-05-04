# Pull Request

## Summary

Describe the change and why it is needed.

## Scope

- [ ] Root 20-file Knowledge package
- [ ] GPT Builder Instructions
- [ ] Safety or refusal policy
- [ ] ZIP/archive workflow
- [ ] Artifact or validation contract
- [ ] GitHub/community automation
- [ ] Local helper scripts

## Safety Checklist

- [ ] No real secrets, tokens, keys, cookies, sessions, or credential bodies are included.
- [ ] No local filesystem, CI, cloud, host, or production access is overclaimed.
- [ ] Root Markdown file count remains intentional.
- [ ] Secret-sensitive paths are handled by path name only.
- [ ] Unsafe archive behavior fails closed.
- [ ] New or changed behavior has matching evaluation coverage.

## Validation

- [ ] `python3 _codex-session/validate_v4_package.py`
- [ ] `python3 -m py_compile scripts/github_access.py _codex-session/validate_v4_package.py`
- [ ] GPT Builder Preview test, if behavior changed
- [ ] Not run, with reason:

## Notes

Add limitations, follow-up work, or `NOT VERIFIED` claims here.
