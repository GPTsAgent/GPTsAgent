# Repository Architecture

GPTsAgent uses one canonical development repository plus one organization profile repository.

## Canonical Development Repository

`GPTsAgent/GPTsAgent` is the source of truth for development, issues, pull requests, validation, and releases.

It contains:

- `config/`: 20 GPT Builder Knowledge files.
- `instructions/`: system Instructions extracted from `config/GPT-BUILDER-CONFIG.md`.
- `profile/`: organization profile source.
- `scripts/`: validation and packaging tools.
- `docs/`: contributor and maintainer guidance.

## Organization Profile Repository

`GPTsAgent/.github` exists for the public organization profile and community health defaults.

## Why This Way

The project is easier to develop when everything lives in one cloneable workspace. Users get the full working directory from `GPTsAgent/GPTsAgent`; the organization profile stays in `GPTsAgent/.github` because GitHub requires that repository name for organization profiles.

Contributors should open PRs against `GPTsAgent/GPTsAgent`.

## Invariant

The `config/` directory must remain a clean 20-file Knowledge package. Tooling, profile files, contributor docs, and release machinery must stay outside `config/`.
