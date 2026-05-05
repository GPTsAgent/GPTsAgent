# GPTs Current Documentation Dossier

Accessed: `2026-05-05`

Purpose: Capture the current official OpenAI documentation baseline for ChatGPT GPTs, Custom GPT configuration, Builder fields, Knowledge, capabilities, Apps, Actions, sharing, privacy, and operational limits.

Use this file when: updating GPT Builder setup fields, reviewing GPTsAgent capability claims, planning public publishing, or deciding whether to add Apps or Actions.

Related files: `docs/GPTS-PROFESSIONAL-CONTEXT-REVIEW.md`, `docs/OFFICIAL-DOCS-BASIS.md`, `config/GPT-BUILDER-CONFIG.md`, `config/CAPABILITIES-MAP.md`, `config/PUBLISHING-GPT-STORE.md`, `docs/PILOT-LAUNCH-CHECKLIST.md`

## Scope And Method

This dossier intentionally uses official OpenAI sources only:

- `help.openai.com`
- `platform.openai.com`
- `openai.com` policy pages only when linked from official product docs

Third-party blog posts, forum threads, social media, screenshots, and cached snippets are not treated as authoritative configuration evidence. They may help discover changed surfaces, but live Builder UI and official OpenAI docs remain the source of truth.

OpenAI Help Center URLs can redirect between older article slugs and consolidated articles. Treat the final loaded page and current Builder UI as authoritative at release time.

For broader professional, academic, security, governance, and enterprise-adoption context, use `docs/GPTS-PROFESSIONAL-CONTEXT-REVIEW.md`. That context can inform GPTsAgent roadmap and evals, but it does not override official OpenAI product documentation.

## Source Index

| Area | Official source | URL |
|---|---|---|
| GPTs overview | GPTs in ChatGPT | `https://help.openai.com/en/articles/8554407-gpts-in-chatgpt` |
| Creating/editing | Creating and editing GPTs | `https://help.openai.com/en/articles/8554397` |
| Builder collection | Building GPTs collection | `https://help.openai.com/en/collections/8475422-building-gpts` |
| GPTs collection | GPTs collection | `https://help.openai.com/en/collections/8475420-gpts` |
| Instructions | Key Guidelines for Writing Instructions for Custom GPTs | `https://help.openai.com/en/articles/9358033` |
| Sharing/publishing | Sharing and publishing GPTs | `https://help.openai.com/en/articles/8798878-sharing-and-publishing-gpts` |
| Troubleshooting | Troubleshooting GPTs | `https://help.openai.com/en/articles/11325361-troubleshooting-gpts` |
| Data privacy | GPTs Data Privacy FAQ | `https://help.openai.com/en/articles/8554402-gpts-data-privacy-faqs` |
| Memory | Does memory function with GPTs? | `https://help.openai.com/en/articles/8983148-does-memory-function-with-gpts` |
| Free-tier use | Using GPTs FAQ (Free Version) | `https://help.openai.com/en/articles/9300383` |
| Business GPTs | GPTs (ChatGPT Business version) | `https://help.openai.com/en/articles/8798620` |
| Enterprise/Edu GPTs | GPTs (ChatGPT Enterprise version) | `https://help.openai.com/en/articles/8555535` |
| Workspace controls | Managing GPT access in Enterprise and Edu workspaces | `https://help.openai.com/en/articles/9083988-how-to-share-gpts-within-workspaces` |
| Shared editing | Shared edit access for custom GPTs | `https://help.openai.com/en/articles/10658904` |
| GPTs vs API assistants | GPTs vs Assistants | `https://help.openai.com/en/articles/8673914` |
| Data Analysis | Data analysis with ChatGPT | `https://help.openai.com/en/articles/8437071-code-interpreter` |
| Search | ChatGPT search | `https://help.openai.com/en/articles/9237897-chatgpt-search` |
| Canvas | What is the canvas feature in ChatGPT and how do I use it? | `https://help.openai.com/en/articles/9930697` |
| Images | Creating images in ChatGPT | `https://help.openai.com/en/articles/8932459-creating-images-in-chatgpt` |
| Actions overview | GPT Actions | `https://platform.openai.com/docs/actions/introduction` |
| Actions auth | GPT Action authentication | `https://platform.openai.com/docs/actions/authentication` |
| Actions getting started | Getting started with GPT Actions | `https://platform.openai.com/docs/actions/getting-started` |
| Actions production | Production notes on GPT Actions | `https://platform.openai.com/docs/actions/production` |
| Actions files | Sending and returning files with GPT Actions | `https://platform.openai.com/docs/actions/sending-files/openapi-example` |
| Actions retrieval | Data retrieval with GPT Actions | `https://platform.openai.com/docs/actions/data-retrieval/data-retrieval-using-relational-databases` |
| Policy index | Terms and policies | `https://platform.openai.com/policies` |

## Current GPT Definition

A GPT, also called a custom GPT, is a configured version of ChatGPT for a specific purpose. It can combine:

- Instructions;
- conversation starters;
- Knowledge files;
- selected capabilities;
- Apps;
- Actions.

GPTs live inside ChatGPT. They are not embeddable website widgets or API assistants. For a product or website integration outside ChatGPT, OpenAI directs builders to use the API rather than a GPT.

GPTs are no-code ChatGPT assistants. API assistants or agentic applications are developer-built integrations that run inside a separate product or service.

## Availability

Current official docs consistently indicate:

- Users must be signed in to chat with GPTs.
- Public GPT pages may be visible before sign-in, but chatting requires sign-in.
- Creating or editing GPTs requires a paid subscription and, for managed workspaces, the right workspace role/permission.
- Mobile apps can use GPTs, but building/editing GPTs is web-only.
- Free users can use GPTs with tighter limits but cannot create/edit GPTs.
- Rate limits are shared between normal ChatGPT use and GPT use.
- Tool-specific limits can block a GPT's advanced features independently, such as file upload, data analysis, or search.

Plan names in older docs may still mention Team; current product naming uses Business for the former Team plan. Treat plan names as live UI evidence at launch time.

## GPT Builder Field Map

| Builder field or surface | Official meaning | GPTsAgent implication |
|---|---|---|
| Name | Public/user-facing title shown in Store, links, search, and chat header. | Must be clear and not imply local computer control. |
| Description | Short public summary of purpose, audience, and tasks. | Must say uploaded files/sandbox, not local filesystem access. |
| Conversation starters | Example prompts shown when users open the GPT. | Use realistic, high-value prompts that teach safe workflow. |
| Instructions | Behavior, tone, goals, boundaries, decision-making. Applied to every conversation. | Canonical behavior belongs here, not only in Knowledge. |
| Knowledge | Uploaded reference files used during answers. | Keep as reference material; do not rely on Knowledge as the behavior authority. |
| Recommended model | Suggested model when users start a conversation; availability varies. | Select from live Builder UI and record it; do not hard-code stale models. |
| Capabilities | Built-in tools and external tool surfaces. Availability varies by plan, workspace, model, and region. | Record exact enabled state during pilot. |
| Apps | User/workspace connected tools and services. | Optional for Business/Enterprise-style workspace use; not for public Store-first GPTs. |
| Actions | Builder-defined external APIs. | Off by default until backend, schema, auth, privacy, logging, rate limits, and tests exist. |
| Share/publish | Access level and public Store publication. | Public publication needs policy compliance and, for Actions, privacy policy URL. |
| Version history | Builder can restore older versions. | If Actions are restored from an older version, authentication may need reconfiguration. |

## Instructions Guidance

Official guidance says instructions should define behavior and avoid ambiguous broad policy. Strong current patterns:

- Use explicit step structure for multi-step workflows.
- Use trigger/instruction pairs when a process has state transitions.
- Use delimiters and headings.
- Prefer concrete positive instructions where possible.
- Include examples for classification or output consistency.
- Put rules, tone, and workflow behavior in Instructions rather than uploaded Knowledge.
- Add explicit instructions for tool use, including Knowledge, web/search, Actions, or Apps.
- When a GPT is unreliable, tighten instructions and examples before adding more tools.

For GPTsAgent, this supports keeping `instructions/SYSTEM-INSTRUCTIONS.txt` as the canonical behavior layer and treating `config/` files as retrieval/reference support.

## Knowledge

Current official Builder documentation says:

- Knowledge is uploaded reference material.
- Knowledge is best for documentation, guides, handbooks, and internal content.
- Instructions define behavior; Knowledge gives source material.
- A GPT can attach up to 20 Knowledge files.
- Each file can be up to 512 MB.
- Supported file types include common documents, spreadsheets, images, text, and code, but accepted types can vary by model and by whether Code Interpreter/Data Analysis is enabled.
- Prefer clear text-forward files.
- Complex PDFs, slides, or image-heavy files can be less reliable.
- Test in Preview after upload.

Important distinction: current consolidated Builder docs confirm 20 files and 512 MB per file. Older/search-indexed Knowledge article text may mention additional token limits, but this dossier only treats the currently loaded official Builder page as release evidence.

## Capabilities

Current official GPT Builder capability list includes:

- Web search: retrieve current web information.
- Image generation: create images from text prompts.
- Canvas: draft, edit, and refine longer or structured content.
- Code Interpreter/Data Analysis: run calculations, analyze data, and generate charts.
- Apps (Beta): use external tools and services connected by users/workspaces.

Availability varies by account, workspace, region, model, and admin policy. A missing capability is not automatically a bug in the GPT configuration.

## Data Analysis / Code Interpreter

Official Data Analysis docs are important for GPTsAgent because they define the safest file/artifact surface:

- ChatGPT can analyze uploaded files such as Excel, CSV, PDF, and JSON.
- It can create tables, charts, summaries, and analytical outputs.
- It uses Python execution for data analysis.
- The code execution environment has access to files attached to the prompt and files retrieved through GPT Actions.
- The environment cannot generate outbound network requests directly.
- Code execution is isolated from the rest of ChatGPT hosting.
- A code execution instance is conversation-scoped and is destroyed after inactivity.
- Up to 10 files can be uploaded to a given conversation.
- Up to 20 files can be attached to a GPT as Knowledge.
- File size is generally 512 MB per file, with lower practical limits for CSV/spreadsheets.

GPTsAgent implication: Code Interpreter/Data Analysis should stay ON for Sandbox File Operator because it is the main safe surface for ZIP inspection, diffs, checksums, artifact generation, and validation.

## Search

Official Search docs say ChatGPT search provides timely web results with links, and may send rewritten search queries to search providers.

GPTsAgent implication:

- Enable web search if the public product promises current docs, current security guidance, current API facts, prices, schedules, or citations.
- Do not use web search as a substitute for uploaded source evidence.
- Current facts should be cited, not answered from memory.

## Canvas

Official Canvas docs describe Canvas as a writing/coding workspace for longer documents, editing, revisions, inline feedback, and version restoration.

GPTsAgent implication:

- Canvas is useful for long reports, policies, instructions, or review documents.
- Canvas is not the primary artifact packaging surface.
- Do not place secrets in Canvas.
- Treat Canvas availability as plan/workspace/model dependent.

## Image Generation

Official image docs say GPTs with Image Generation enabled can create images. Image generation is available according to GPT settings and plan/tool limits.

GPTsAgent implication:

- Keep image generation OFF by default for Sandbox File Operator because image generation is not needed for archive safety, file diffs, checksums, validation, or packaging.
- Enable only if visual assets, diagrams, or illustrations become an explicit product feature.

## Apps

Official docs describe Apps as a beta capability for eligible managed workspaces. Key current constraints:

- Apps allow GPTs to use external services users/workspaces have connected.
- Apps and Actions are mutually exclusive in a GPT.
- If Apps are enabled, Actions are replaced or disabled for that GPT.
- GPTs with Apps cannot be published to the public GPT Store; they can be shared within the company/workspace store.
- End users cannot change which apps are configured by the GPT creator unless they have edit access.
- Users may need to connect an app before a GPT can use it.
- Admins can control whether apps are allowed in workspace-created GPTs.

GPTsAgent implication:

- Apps are not a first public-pilot dependency.
- If Apps are enabled later, document exact app names in the GPT description because end users may not otherwise see the configured app list before use.
- Do not combine Apps with Actions.

## Actions

Actions connect a GPT to external REST APIs defined by the builder. Official OpenAI docs split Actions into:

- an OpenAPI schema;
- an authentication configuration;
- API endpoint behavior;
- user confirmations and privacy controls.

### Actions Setup

Current official setup requirements:

- Actions require API details and an OpenAPI schema in JSON or YAML.
- The schema defines servers, endpoints, parameters, and operation IDs.
- Schema can be pasted, imported from a URL, or started from built-in examples.
- Test each action in Preview.
- Apps and Actions cannot be used together in the same GPT.

### Actions Authentication

Supported authentication choices:

- None;
- API key;
- OAuth.

API key auth can use Basic, Bearer, or Custom header configuration in the GPT editor. OAuth requires client ID, client secret, authorization URL, token URL, scope, token exchange method, and approved callback URLs.

### Actions Production Constraints

Current production notes include:

- Use TLS 1.2 or later on port 443 with a valid public certificate.
- API calls time out after about 45 seconds.
- Request and response payloads must be less than 100,000 characters each.
- Requests and responses are text-only; images/video are not supported in action payloads.
- Custom headers are not supported.
- Implement rate limiting; ChatGPT respects 429 responses and backs off after repeated 429/500 responses.
- Use the `x-openai-isConsequential` flag for operations that should always require user confirmation.
- If a GPT calls a custom action, relevant parts of the conversation may be sent to that action endpoint.

### Actions Files

Official file handling notes:

- POST action requests can include up to 10 files from the conversation through `openaiFileIdRefs`.
- File URLs sent to an action are short-lived.
- Actions may return up to 10 files.
- Returned files can be up to 10 MB each.
- Returned files cannot be images or videos.

### Actions Privacy

Official docs say public GPTs shared by link or in the GPT Store with Actions must include a valid Privacy Policy URL. Users may be asked to approve Actions before they run. OAuth users can review/manage connected accounts.

GPTsAgent implication:

- Keep Actions OFF for the current public pilot.
- Do not add raw shell, broad file API, credential relay, production deployment, or unrestricted mutation endpoints.
- Before enabling Actions, require a real backend, OpenAPI schema, authentication model, privacy policy, audit logging, rate limits, artifact retention/expiration, user confirmation gates, and Preview/eval coverage.

## Sharing, Publishing, And Store

Official sharing levels vary by plan/workspace and can include:

- invite-only/private;
- specific users or groups in managed workspaces;
- workspace link;
- whole workspace;
- anyone with link;
- GPT Store.

Public publishing may be blocked if:

- public publishing is disabled by workspace policy;
- the GPT uses Apps;
- the GPT uses Actions without a valid Privacy Policy URL;
- sharing or policy checks restrict the GPT;
- account/workspace restrictions prevent marketplace publishing.

For GPT Store publication, builders may need:

- category selection;
- complete Builder Profile;
- verified domain or profile details where required;
- policy/product compliance confirmation.

Published public surface can include:

- GPT name;
- icon/profile image;
- description;
- category;
- capabilities;
- conversation starters;
- ratings, if available;
- Builder Profile details.

GPTsAgent implication:

- Public description must avoid local filesystem, production automation, or guaranteed security claims.
- Category and visibility must be recorded from live UI.
- Apps block public GPT Store publication.
- Actions require Privacy Policy URL for public sharing/publication.

## Privacy, Data, And Conversation Access

Official GPTs docs say:

- Whether GPT conversations can be used to improve OpenAI models depends on the user's plan and data-control settings.
- Business, Enterprise, and Edu data is not used for training by default.
- Consumer-plan conversations may be used for training unless the user opts out where available.
- GPT builders cannot view individual conversations users have with their GPTs.
- If a GPT uses Apps or external APIs, relevant parts of the user's input may be sent to the third-party service.
- OpenAI does not audit or control how third-party services use or store data.

GPTsAgent implication:

- Do not promise that the builder can inspect user chats.
- Do not promise third-party privacy if Apps or Actions are used.
- For Actions, publish a privacy policy before public sharing.
- Continue warning users not to upload secrets.

## Memory And State

Official docs say custom GPTs do not use saved memory, custom instructions, or previous conversations. Each conversation starts fresh. Memory is not currently supported for GPTs created with GPT Builder.

GPTsAgent implication:

- Do not claim durable memory, background execution, persistent state, or cross-chat continuity.
- Use session maps and handoffs inside the current conversation.
- Treat any long-term package changes as maintainer/admin release work, not user-session mutation.

## Workspace Governance

Managed workspace admins/owners can control:

- who can create/edit GPTs;
- GPT sharing levels;
- access to third-party GPTs;
- whether Apps can be used in GPTs;
- which Action domains are allowed;
- owner/editor permissions and reassignment;
- audit/compliance surfaces where available.

Shared edit access lets GPT owners/admins add editors. Editors can change configuration, Knowledge files, Apps, and Actions. Admins/owners can manage ownership and permissions.

GPTsAgent implication:

- Any Builder setup record should include workspace plan and role.
- If a capability is missing, check plan/workspace policy before treating it as a package bug.

## Troubleshooting Rules

Official troubleshooting guidance maps directly to GPTsAgent validation:

- If instructions are not followed, remove conflicting or duplicate rules, shorten where possible, add explicit structure, and test small changes in Preview.
- If Knowledge is weak, confirm needed information exists, use cleaner text-forward files, simplify complex PDFs/slides, and avoid relying on images alone.
- Put behavior rules in Instructions, not uploaded Knowledge.
- If downloads fail, confirm Code Interpreter/Data Analysis is enabled, retry smaller artifacts, and test in Preview.
- Missing capabilities can be caused by plan, workspace settings, or role permissions.
- Apps and Actions cannot both be enabled.
- Public publishing issues often involve Builder Profile, category, Apps, Actions privacy policy, or policy review.

## Current Model Guidance

OpenAI docs repeatedly warn that model options can be updated or retired. Current Builder docs include retirement notices for older ChatGPT models and say unavailable GPT models may be automatically moved to similar current models.

GPTsAgent implication:

- Do not hard-code a model name into public package promises.
- Record the selected live Builder model during pilot.
- If the model changes, rerun Preview and safety tests.
- Use `NOT VERIFIED` when the model setting was not visible in the current Builder session.

## GPTsAgent Configuration Recommendations

For Sandbox File Operator, the current official docs support this default setup:

| Field | Recommended setting | Reason |
|---|---|---|
| Name | `Sandbox File Operator` | Clear uploaded-file/product boundary. |
| Description | Short description that says uploaded files and ChatGPT sandbox. | Avoid local filesystem overclaim. |
| Instructions | Paste full `instructions/SYSTEM-INSTRUCTIONS.txt`. | Behavior-critical layer. |
| Conversation starters | Use realistic ZIP/file/artifact prompts. | Helps users start safe workflows. |
| Knowledge | Upload exactly 20 Markdown files from `config/`. | Fits Knowledge limit and package design. |
| Recommended model | Select current best live Builder option and record it. | Model availability changes. |
| File uploads | ON if visible as separate setting. | Core input path. |
| Code Interpreter/Data Analysis | ON. | Main sandbox/artifact surface. |
| Web search | ON if current docs/facts/citations are a product promise. | Supports current source-backed answers. |
| Canvas | OPTIONAL. | Useful for long drafts/reports. |
| Image generation | OFF by default. | Not core to file safety. |
| Apps | OFF for public pilot; optional only for scoped workspace GPT. | Apps block public Store publication and are mutually exclusive with Actions. |
| Actions | OFF by default. | No backend/privacy/schema currently exists. |
| Privacy policy URL | N/A while Actions are off. | Required for public GPTs with Actions. |
| Category | Choose live closest available: Productivity, Programming, Research, Writing, or Education. | Category options are UI-controlled. |
| Visibility | Start private/link pilot before public Store. | Allows Preview and red-team evidence collection. |

## Gaps To Track For GPTsAgent

Priority gaps:

1. Keep the v0.3.1 Builder Field Map aligned with the live Builder UI before every public release.
2. Record exact live Builder settings after the next manual GPT Builder setup.
3. Keep explicit Apps public-store caveats wherever Apps are discussed.
4. Keep Actions design-only until backend, schema, auth, privacy policy, logging, rate limits, and retention exist.
5. Continue expanding Preview cases for missing capability, Apps disabled, Actions privacy-policy block, Knowledge-vs-Instructions authority, and model auto-transition.

## Release-Time Verification Checklist

Before publishing a GPTsAgent/Sandbox File Operator update:

- Reopen the live GPT Builder UI.
- Confirm current field names and available capability toggles.
- Confirm the selected model from the live model menu.
- Paste complete Instructions.
- Upload exactly the 20 Knowledge files.
- Enable only intended capabilities.
- Confirm Apps and Actions are not both enabled.
- If Actions are enabled, confirm Privacy Policy URL and action tests.
- Run Preview with normal and adversarial prompts.
- Save the Builder settings record.
- Mark anything unobserved as `NOT VERIFIED`.

## Operational Rule

Treat official OpenAI docs and the live GPT Builder UI as release inputs, not permanent facts. If the docs, UI, and package disagree, update the package or mark the affected claim `NOT VERIFIED` before publishing.
