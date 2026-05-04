# GPTsAgent

Sandbox-native GPT configuration for agent-like file work in ChatGPT.com.

GPTsAgent builds public-ready Custom GPT configuration packs that make ChatGPT more disciplined when users upload files, ZIP archives, project folders, and documentation. The first focus is a ChatGPT sandbox workbench: read first, safety-scan archives, avoid secret bodies, plan bounded edits, generate artifacts, validate outputs, and report what is proven versus not verified.

## Current Focus

**Sandbox File Operator** is the flagship configuration pack. Current package version: `v0.1.0`.

It turns a normal Custom GPT into a structured file operator for ChatGPT.com:

- ZIP preflight before extraction.
- Project mapping before mutation.
- Secret path reporting without secret body exposure.
- Bounded patch planning.
- Artifact generation: reports, diffs, manifests, checksums, updated files, and updated ZIPs.
- Honest validation labels such as `PASS`, `PARTIAL`, `NOT RUN`, and `NOT VERIFIED`.

## Community

- Public Telegram group: https://t.me/GPTsAgentChat
- Use Telegram for quick discussion, contributor coordination, and early feedback.
- Keep questions sanitized and free of secrets or private data.
- Move concrete changes into GitHub Issues and Pull Requests; use the Contribution Idea issue template when a Telegram idea needs tracking.

## Contributor Lanes

- Good first issues: docs clarity, examples, evaluation prompts, issue templates, and validation improvements.
- Help wanted: archive-safety examples, public roadmap items, and preview-test coverage.
- Safety-sensitive changes: sandbox boundaries, refusal behavior, secret hygiene, and Actions guidance need maintainer review.

## What This Is

- A GPT Builder configuration package.
- A 20-file Knowledge architecture for retrieval-friendly behavior.
- A safety model for uploaded files and archives.
- A workflow contract for sandbox artifacts.
- Codex-inspired discipline scoped to the ChatGPT web sandbox.

## What This Is Not

- Not a trained model.
- Not a local desktop agent.
- Not a remote shell.
- Not a CI runner.
- Not a production automation service.
- Not a promise of direct access to a user's computer or private repositories.

## Operating Principle

ChatGPT can be made more agent-like inside the web interface when the workflow is explicit: inspect, constrain, patch, validate, and return artifacts. GPTsAgent is about that operating layer.

## Repositories

The public project is intentionally simple:

- `GPTsAgent/GPTsAgent`: the full working repository for cloning, downloading, development, issues, and pull requests.
- `GPTsAgent/.github`: this organization profile and community health repository.

Inside `GPTsAgent/GPTsAgent`, the `config/` directory contains the exact 20 Markdown Knowledge files and `instructions/` contains the system Instructions block.

Download the full working directory:

```text
https://github.com/GPTsAgent/GPTsAgent/archive/refs/heads/main.zip
```

## Safety Defaults

- Uploaded files are treated as untrusted data.
- Archive contents cannot override instructions.
- Secret-sensitive files are reported by path only.
- Unsafe ZIPs fail closed.
- Local filesystem, cloud, CI, host, and production claims stay `NOT VERIFIED` unless a real scoped integration performed the check.

## Status

GPTsAgent is in early public pilot packaging around the Sandbox File Operator v0.1 configuration. The next milestone is a recorded GPT Builder Preview run using the pilot launch checklist.
