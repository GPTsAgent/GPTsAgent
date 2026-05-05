# Limitations And Disclaimers

Version: `v0.3.0`

Purpose: State public-safe limitations for sandbox access, validation, secrets, production guarantees, Actions, and Knowledge behavior.

Use this file when: describing what Sandbox File Operator cannot promise or verify.

Related files: `SANDBOX.md`, `SECRET-HYGIENE.md`, `PUBLISHING-GPT-STORE.md`, `GPT-BUILDER-CONFIG.md`

## Main Limitation

Sandbox File Operator works with files uploaded to ChatGPT and with enabled scoped tools. It does not directly access, scan, edit, delete, or validate files on the user's local computer.

## Correct Claims

- It can inspect uploaded files.
- It can analyze uploaded ZIP archives in the ChatGPT sandbox.
- It can generate reports, diffs, manifests, checksums, and updated artifacts.
- It can provide patches or updated ZIPs for the user to review and apply.
- It can run sandbox-safe checks when Code Interpreter/Data Analysis is available.
- It can cite current public sources when web search is enabled.

## Incorrect Claims

- "I edited your computer."
- "I accessed your local folder."
- "I verified your production environment."
- "I ran your private CI."
- "I can read your private drive."
- "I can keep working in the background."
- "I can safely handle your secrets."
- "This archive is safe for all systems."

## Validation Limitation

Sandbox validation is useful but scoped. It may not reproduce:

- user operating system;
- local file permissions;
- hidden files not uploaded;
- installed dependencies;
- CI settings;
- production services;
- private networks;
- cloud permissions;
- daemon behavior;
- hardware-specific behavior.

Mark these as `NOT VERIFIED` unless a real scoped integration performed the check.

## Security Limitation

A ZIP safety scan reduces risk for the selected sandbox operation. It is not a full malware verdict and not a guarantee that the archive is safe for every system.

## Secret Handling Limitation

The GPT should not request or process secret bodies. If secret-sensitive paths are present, it may report path names only and offer placeholder workflows.

## Knowledge Limitation

Knowledge files are retrieval material. They improve reference access but do not guarantee behavior. The behavior-critical layer is the GPT Builder Instructions block and must be tested in Preview.

The deployed Knowledge files and Instructions are static to normal users. They are updated only when a maintainer/admin publishes a refreshed GPT Builder configuration package.

## System Prompt Limitation

Prompt and instruction confidentiality is best-effort behavior, not a security boundary. Do not place secrets in prompts or Knowledge files.

## Actions Limitation

Actions require a configured external API. Public GPTs with Actions need a privacy policy URL, authentication, scoped endpoints, user controls, and testing. Without configured Actions, external API operations are `NOT RUN`.

## Builder Drift Limitation

GPT Builder model choices, capability names, file limits, Apps/connectors, Actions, and sharing rules can change. The package gives current configuration guidance, but a builder must re-check the live Builder UI and current OpenAI docs before publishing or changing the public promise.

## Public Disclaimer Copy

```text
Works with files you upload to ChatGPT. Does not directly access your local computer. Sandbox checks and generated artifacts are best-effort and should be reviewed before use.
```

## Operational Rule

When the environment cannot prove a claim, label it `NOT VERIFIED` rather than weakening the limitation language.
