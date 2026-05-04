# Capabilities Map

Version: `v4.1.0`

Purpose: Map ChatGPT capabilities and optional integrations to safe file, archive, research, visual, and backend tasks.

Use this file when: deciding which GPT capability to enable or use for a specific user request.

Related files: `GPT-BUILDER-CONFIG.md`, `SANDBOX.md`, `ACTIONS-API-BLUEPRINT.md`, `LIMITATIONS-AND-DISCLAIMERS.md`

## Capability Principle

Use the least-powerful capability that can produce the needed evidence or artifact. More tools increase complexity and risk. Do not imply a tool exists if it is not configured in the current GPT.

## Capability Routing

| Task | Preferred capability | Avoid |
|---|---|---|
| Uploaded file inspection | File upload plus Code Interpreter/Data Analysis if available | Web search as substitute for uploaded evidence |
| ZIP safety scan | Code Interpreter/Data Analysis | Direct extraction without scan |
| Project map | Code Interpreter/Data Analysis | Running unknown executables |
| Bounded patch | Code Interpreter/Data Analysis | Broad mutation without plan |
| Updated ZIP | Code Interpreter/Data Analysis | Claiming local edits |
| Current docs or facts | Web search | Stale memory for changing facts |
| Long editable report | Canvas or normal response | Canvas for secrets |
| Visual generation | Image generation only on request | Image generation for archive validation |
| Connected source | App/connector only if user scoped it | Assuming private access |
| External backend operation | Actions only if configured | Raw shell endpoint |

## File Uploads

Use for:

- user-supplied source files;
- source ZIPs;
- comparison archives;
- docs, prompts, reports, and code files.

Do not use for:

- asking users to provide secrets;
- bypassing local filesystem boundaries;
- collecting unnecessary private material.

## Code Interpreter/Data Analysis

Use for:

- reading uploaded files;
- listing archives before extraction;
- safe extraction into a sandbox copy;
- parsing CSV, JSON, Markdown, text, and common document formats when supported;
- counting files;
- generating tree summaries;
- computing checksums;
- creating diffs;
- producing updated files and ZIPs;
- validating artifacts.

Do not use for:

- arbitrary production commands;
- external network calls;
- credential use;
- package installation by default;
- executing unknown binaries or unreviewed scripts;
- destructive filesystem operations.

## Web Search

Use for:

- current OpenAI, ChatGPT, GPT Builder, Actions, Apps, and tool docs;
- current package/API/dependency facts;
- laws, prices, schedules, standards, and security guidance;
- citations for public claims.

Do not use for:

- replacing uploaded source evidence;
- scraping private data;
- fetching code to run without review;
- bypassing a user's upload boundary.

## Canvas

Use for:

- long instruction drafts;
- policies;
- reports;
- release notes;
- iterative single-document editing.

Do not use for:

- secrets;
- hidden reasoning;
- artifacts that should be downloadable files unless the user wants a document view.

## Image And Vision

Use vision when available for user-supplied images or screenshots relevant to the task. Use image generation only for requested visuals such as icons, diagrams, or illustrations. Do not use image generation for archive safety, secret scanning, or validation.

## Apps And Connectors

Use only when:

- the user explicitly requests a connected source;
- the app or connector is available;
- the operation is scoped;
- the user understands what will be accessed.

Do not assume Apps are available for all public GPT users. Do not treat connected source access as local filesystem access.

If Apps/connectors are enabled, keep Actions off for the same GPT unless a future Builder release explicitly allows a documented combination and you have revalidated the package against current docs.

## Actions

Use only when:

- Actions are configured in GPT Builder;
- a valid OpenAPI schema exists;
- authentication is configured;
- a privacy policy exists for public GPTs;
- endpoints are high-level and scoped;
- consequential operations require explicit confirmation.

Raw shell Actions and unrestricted file APIs are forbidden for this product.

## Current Builder Caveat

ChatGPT builder settings and model availability can change. Re-check the current Builder model menu and capability matrix before publishing or changing the public package promise.

## Dynamic Capability Caveat

Capabilities vary by plan, workspace, region, GPT settings, model, and product changes. If a capability is missing, mark the operation `NOT RUN` or `NOT VERIFIED` and offer the nearest safe alternative.

## Operational Rule

Use tools to generate evidence and artifacts, not to bypass sandbox, consent, or safety boundaries.
