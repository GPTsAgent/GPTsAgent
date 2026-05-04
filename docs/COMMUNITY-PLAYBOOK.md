# Community Playbook

Version: `v4.1.0`

Purpose: Explain how Telegram, GitHub Issues, Pull Requests, labels, and maintainer review fit together for a public open-source GPT configuration project.

Use this file when: routing contributor questions, converting Telegram discussion into GitHub work, or training new maintainers on the public workflow.

Related files: `README.md`, `CONTRIBUTING.md`, `docs/OFFICIAL-DOCS-BASIS.md`, `docs/PILOT-LAUNCH-CHECKLIST.md`

GPTsAgent is public by default, but it is still a safety-sensitive configuration project. This playbook explains how discussion, issues, pull requests, labels, and maintainer review fit together.

## Channels

| Channel | Use it for | Do not use it for |
|---|---|---|
| Telegram `https://t.me/GPTsAgentChat` | Quick questions, idea triage, contributor coordination, public-safe feedback. | Secrets, private archives, private repository contents, credentials, production incident details. |
| GitHub Issues | Tracked bugs, safety reports, validation failures, contribution ideas, scoped proposals. | Raw secrets, credential bodies, private customer data, unredacted private code. |
| Pull Requests | Reviewed changes to docs, config, scripts, templates, workflows, and packaging. | Broad rewrites without an issue, unverifiable claims, unsafe capability expansion. |

Telegram is a discussion layer. GitHub is the durable project record.

## Contribution Lanes

| Lane | Good first issue? | Validation |
|---|---:|---|
| Docs clarity | Yes | `python3 scripts/validate_workspace.py` |
| Example prompts and reports | Yes | Validator plus targeted doc review |
| Evaluation checklist cases | Yes | Validator plus GPT Builder Preview when behavior changes |
| Issue or PR templates | Yes | Validator plus template review |
| Label taxonomy | Yes | `python3 scripts/sync_labels.py` dry run |
| Builder Instructions | Usually no | Extract instructions, validator, Preview tests |
| Safety or refusal policy | Usually no | Validator, red-team examples, maintainer review |
| Release automation | Usually no | Validator, script compile, release ZIP build |

## Telegram To GitHub

When an idea starts in Telegram:

1. Remove private data, credentials, names, and non-public repository details.
2. Summarize the problem, not the whole chat.
3. Open the `Contribution idea` issue template.
4. Add expected validation or mark it `NOT VERIFIED`.
5. Link the issue from the PR if implementation follows.

Use this sanitized summary shape:

```text
Source: Telegram discussion
Problem: <public-safe problem>
Expected improvement: <what should become easier or safer>
Suggested scope: <files or docs likely affected>
Validation: <command, Preview test, or NOT VERIFIED reason>
```

## Builder / Pilot Note

Use `docs/PILOT-LAUNCH-CHECKLIST.md` for the first GPT Builder draft and `docs/OFFICIAL-DOCS-BASIS.md` when updating settings or launch claims.

## Label Taxonomy

The desired public label set is stored in `.github/labels.json`. It exists so issue templates, triage language, and maintainer review use the same vocabulary.

Use:

- `community` for Telegram-to-GitHub handoffs and contributor coordination.
- `good first issue` for small, bounded tasks with clear files and validation.
- `help wanted` for tasks where maintainer direction is clear but implementation is open.
- `safety` for sandbox honesty, archive safety, prompt injection, refusal, and secret hygiene.
- `validation` for local validator, CI, Preview, artifact, or release evidence.
- `not verified` when a claim is useful but still lacks proof.

Maintainers can check labels with:

```bash
python3 scripts/sync_labels.py
```

Creating missing labels requires a GitHub token in `GH_TOKEN` or `GITHUB_TOKEN`:

```bash
python3 scripts/sync_labels.py --apply
```

The script does not require dependencies and does not print token values.

## Maintainer Triage

For new issues:

1. Confirm the report is public-safe.
2. Add or keep `triage`.
3. Add one area label such as `documentation`, `package`, `safety`, `validation`, `instructions`, or `github-actions`.
4. Add `good first issue` only when the expected files and validation path are obvious.
5. Ask for a sanitized reproduction instead of accepting private payloads.
6. Close or narrow anything that asks the project to overclaim ChatGPT.com sandbox capabilities.

## Public Safety Rule

If a contribution would make the GPT claim direct local filesystem access, expose secrets, bypass archive safety, or run unbounded external automation, reject or narrow it before implementation.
