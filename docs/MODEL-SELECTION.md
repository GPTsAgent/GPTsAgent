# Model Selection Notes

Version: `v0.3.0`

Purpose: Separate Codex-local maintainer model preferences from public ChatGPT Builder runtime settings.

Use this file when: choosing a local model for repository maintenance, interpreting `models_cache.json`, or writing public-safe model guidance for GPTsAgent.

Related files: `README.md`, `docs/PILOT-LAUNCH-CHECKLIST.md`, `docs/OFFICIAL-DOCS-BASIS.md`, `config/GPT-BUILDER-CONFIG.md`

## Core Rule

`models_cache.json` is Codex-local maintainer evidence. It may inform how you work on the repository, but it does not prove which model a public GPT Builder draft uses.

## What The Local Cache Suggests

For deep repo review, archive safety, prompt-engineering work, and release validation, favor the strongest extended-reasoning profile available in the local Codex environment.

Observed maintainer-side patterns from the cache:

- `GPT-5.5` is available locally.
- The local cache shows `xhigh` as the default reasoning level for that model.
- Large context and parallel tool support are useful for multi-file review.
- Extended reasoning is better suited to policy changes, eval design, and cross-file consistency than a fast drafting lane.

If a pro or extended-thinking variant appears in the local Codex environment, treat it as maintainer-only evidence unless the live public GPT Builder UI also exposes it.

## Public GPT Rule

GPTsAgent's public product runs in ChatGPT Builder, not in Codex. For the public GPT:

- select the live Builder model from the current UI;
- record the exact selection in the launch checklist;
- use `NOT VERIFIED` for any model setting that is not visible in the current Builder session;
- do not claim a Codex-local model cache proves public GPT runtime behavior.

## Preferred Maintainer Posture

| Context | Preferred posture |
|---|---|
| Deep policy or release review | Use the strongest local extended-reasoning profile available. |
| Cross-file consistency checks | Prefer the largest practical context and tool support. |
| Simple docs cleanup | A lighter model is acceptable if the change is narrow. |
| Public GPT Builder claims | Trust only the live Builder UI and Preview evidence. |

## Public-Safe Wording

Safe:

```text
For maintainer-side review, an extended-reasoning Codex profile is preferred when available. The public GPT Builder model must still be selected and verified in the live ChatGPT Builder UI.
```

Unsafe:

```text
The public GPT definitely runs on GPT-5.5-Pro Extended Thinking for every user.
```

## Operational Rule

Use Codex-local model evidence to improve maintainer work, but keep ChatGPT Builder claims tied to live public evidence only.
