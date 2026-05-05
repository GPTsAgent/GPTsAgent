# GPTs Professional Context Review

Accessed: `2026-05-05`

Purpose: Summarize professional, academic, security, governance, and enterprise-adoption context around OpenAI GPTs and custom GPT design.

Use this file when: deciding what to prioritize after the official GPT Builder field map, improving GPTsAgent safety posture, designing evals, or deciding whether Apps/Actions belong in a public pilot.

Related files: `docs/GPTS-CURRENT-DOCS-DOSSIER.md`, `docs/OFFICIAL-DOCS-BASIS.md`, `config/GPT-BUILDER-CONFIG.md`, `config/CAPABILITIES-MAP.md`, `docs/THREAT-MODEL.md`, `eval/preview-scenarios.jsonl`

## Authority Model

Use this source hierarchy:

1. Live GPT Builder UI and official OpenAI docs define what GPTs can be configured to do.
2. Official OpenAI Academy and Cookbook material provides practical OpenAI-authored guidance.
3. Security standards and public-sector guidance, especially OWASP, NIST, and NCSC, provide risk framing.
4. Peer-reviewed or preprint research provides empirical risk signals, but it may lag product changes.
5. Consulting, enterprise, education, and practitioner articles provide adoption patterns, not product guarantees.

Professional context should never override official OpenAI product requirements. It should shape validation, governance, documentation, and launch discipline.

## Professional Source Index

| Tier | Source | URL | Main relevance |
|---|---|---|---|
| Official practice | OpenAI Academy: Using custom GPTs | `https://openai.com/academy/custom-gpts/` | GPTs are best for repeatable, consistent workflows; test with 10-15 representative questions. |
| Official developer practice | OpenAI Cookbook: GPT Actions Library - Zapier | `https://developers.openai.com/cookbook/examples/chatgpt/gpt_actions_library/gpt_action_zapier` | Actions can connect GPTs to large app ecosystems but require technical setup and external configuration. |
| Official developer practice | GPT Actions production notes | `https://developers.openai.com/api/docs/actions/production` | Production Actions need timeouts, TLS, rate limits, concise schemas, consequential flags, and raw data responses. |
| Security standard | OWASP Top 10 for LLM Applications | `https://owasp.org/www-project-top-10-for-large-language-model-applications/` | Prompt injection, sensitive information disclosure, insecure plugin/tool design, and supply chain risk map directly to GPTs. |
| Security agency | NCSC: Prompt injection is not SQL injection | `https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection` | LLMs do not enforce a hard instruction/data boundary; reduce impact instead of claiming prompt-injection immunity. |
| Risk governance | NIST AI RMF Generative AI Profile | `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf` | Govern, map, measure, and manage generative AI risks across lifecycle stages. |
| Education practice | MIT Sloan: Custom GPTs guide | `https://mitsloanedtech.mit.edu/ai/tools/custom-gpts-at-mit-sloan-a-comprehensive-guide/` | Use clear objectives, rubrics, anonymization, output testing, and transcript review for instructional GPTs. |
| Empirical security | A Large-Scale Empirical Analysis of Custom GPTs' Vulnerabilities | `https://arxiv.org/abs/2505.08148` | Large-scale study of custom GPT marketplace vulnerabilities, including prompt leakage and unsafe behavior. |
| Empirical policy | Towards Safer Chatbots: Automated Policy Compliance Evaluation of Custom GPTs | `https://arxiv.org/abs/2502.01436` | Large-scale black-box red-team/eval methodology for policy compliance in custom GPTs. |
| Enterprise adoption | McKinsey: Four gen AI shifts | `https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/enterprise-technologys-next-chapter-four-gen-ai-shifts-that-will-reshape-business-technology` | Distinguishes human-led assistant work from AI-led factory workflows requiring audit and supervision. |
| Enterprise operating model | McKinsey: Gen AI operating model | `https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/a-data-leaders-operating-guide-to-scaling-gen-ai` | Scaled gen AI requires data ownership, reusable components, cross-functional governance, and progress monitoring. |

## High-Confidence Findings

### 1. Strong GPTs Are Workflow Products, Not Prompt Dumps

OpenAI Academy frames custom GPTs as useful when a user or team repeats the same workflow, context, structure, tone, or data-analysis pattern. The professional implication is direct: a GPT should have a clear job, a narrow operating contract, and repeatable success criteria.

For GPTsAgent:

- Keep Sandbox File Operator focused on uploaded files, ZIPs, artifacts, reports, and validation.
- Avoid turning the public GPT into a broad desktop agent, generic assistant, or backend automation platform.
- Treat conversation starters as workflow entry points, not marketing slogans.
- Add eval prompts that mirror real user jobs, not only adversarial cases.

### 2. Official Builder Fields Need A Single Install Sheet

The official GPT Builder field model now explicitly covers name, description, conversation starters, instructions, Knowledge, recommended model, capabilities, Apps, Actions, Preview, save/update, and version history.

For GPTsAgent:

- The next release should add a one-page Builder Field Map.
- Each visible Builder field should have a copy-ready value or a deliberate `N/A`.
- Capability toggles should be recorded as `ON`, `OFF`, `OPTIONAL`, or `NOT VERIFIED`.
- The selected model should be captured from live UI evidence because OpenAI retires and remaps GPT models over time.

### 3. Instructions Are The Behavior Layer; Knowledge Is Retrieval Material

Official OpenAI docs and professional practice align on a key point: behavior belongs in Instructions. Knowledge files provide reference material. Security research reinforces this because uploaded content can contain adversarial instructions, private data, outdated facts, or misleading examples.

For GPTsAgent:

- Keep `instructions/SYSTEM-INSTRUCTIONS.txt` canonical.
- Keep the 20 Knowledge files retrieval-friendly, public-safe, and secret-free.
- Do not rely on Knowledge files to enforce safety boundaries.
- Add Preview tests that ask the GPT to choose between a Knowledge file instruction and the Builder Instructions.

### 4. Knowledge Quality Matters More Than Quantity

OpenAI guidance favors clear, text-forward reference files. Professional education and enterprise articles add the same pattern: document owners must curate, version, anonymize, and test the reference set. More files can create more retrieval noise, stale context, and leakage risk.

For GPTsAgent:

- Preserve the exact 20-file architecture unless OpenAI changes the limit and there is a reviewed package redesign.
- Prefer concise Markdown files over PDFs or image-heavy documents.
- Treat release ZIP and Knowledge upload as separate artifacts.
- Add a "Knowledge freshness / ownership" check before each public publish.

### 5. Prompt Injection Is A Residual Risk, Not A Solved Prompting Problem

NCSC argues that LLMs do not enforce a hard separation between instructions and data. OWASP ranks prompt injection and related LLM risks as core application-security concerns. Research on custom GPTs reports widespread prompt leakage and policy-violating behavior in marketplace GPTs.

For GPTsAgent:

- Keep language honest: prompt confidentiality is best-effort, not a security boundary.
- Do not place secrets, tokens, credential bodies, private provenance, or sensitive policy thresholds in Instructions or Knowledge.
- Keep file/archive content explicitly untrusted.
- Use deterministic safeguards where possible: path allow/deny rules, extraction fail-closed behavior, output checks, action confirmations, and validation labels.
- Red-team prompt leakage, Knowledge dumping, archive prompt injection, and tool misuse before every release.

### 6. Actions Are Product Infrastructure, Not A Toggle

Official OpenAI Actions docs and the Cookbook show that Actions are useful but operationally serious. They need API design, OpenAPI schema, authentication, privacy policy, test coverage, rate limits, TLS, payload limits, and confirmation semantics.

For GPTsAgent:

- Keep Actions OFF for the public pilot.
- Do not add broad file APIs, raw shell endpoints, credential relay, unbounded mutation, or production deployment operations.
- If Actions are pursued later, begin with one read-only or artifact-retrieval endpoint and a full threat model.
- Action API responses should return raw structured data where possible, letting the GPT write the final user response.
- Use `x-openai-isConsequential` for any operation that changes external state.

### 7. Apps Are Not A Public-Store Shortcut

Official OpenAI docs currently make Apps and Actions mutually exclusive in a GPT, and GPTs with Apps cannot be published to the public GPT Store. Apps are more relevant for managed workspace GPTs than for a public Store-first pilot.

For GPTsAgent:

- Keep Apps OFF for the first public GPT Store path.
- If a workspace-specific GPT uses Apps later, name the specific Apps in the description/setup notes.
- Add a Preview/test case for "Apps unavailable" behavior.
- Do not design around Apps as a replacement for uploaded-file workflows unless the target deployment is explicitly workspace-internal.

### 8. Enterprise Use Requires Governance, Ownership, And Evals

McKinsey's operating-model guidance and NIST's AI RMF profile converge on governance: scalable gen AI systems require defined owners, reusable components, data governance, monitoring, and risk management. MIT Sloan's education guidance adds domain-specific review and user feedback.

For GPTsAgent:

- Treat public GPT release as a governed package release, not a casual UI update.
- Store Builder settings evidence and Preview transcripts or summaries.
- Keep an ownership record for who can edit the GPT.
- Add release evidence for capability state, model state, Knowledge upload, and Preview pass/fail.
- Maintain eval fixtures for both normal workflows and abuse cases.

### 9. Human-Led And AI-Led Work Should Not Be Blurred

Professional enterprise writing distinguishes human-led assistant workflows from AI-led autonomous workflows. Sandbox File Operator should stay human-led: it can inspect, propose, package, and validate artifacts, but should not claim background execution, local mutation, or production authority.

For GPTsAgent:

- Keep "artifact out" as the core promise.
- Do not claim live host access, background daemon behavior, CI authority, persistent memory, or production deployment.
- For consequential operations, require explicit user confirmation and a real configured tool.

### 10. Measurement Should Be Built Into The Product

OpenAI Academy recommends testing custom GPTs with representative examples. Academic policy-compliance work shows black-box red-team prompts can identify unsafe behavior at scale. NIST emphasizes measurement and lifecycle risk management.

For GPTsAgent:

- Continue using `eval/preview-scenarios.jsonl`.
- Expand evals when Builder fields, Apps, Actions, model selection, or Knowledge architecture changes.
- Track both expected good behavior and expected refusal/narrowing.
- Make Preview results part of release evidence.

## Professional Patterns To Adopt

### Builder And Release

- Maintain a copy-ready Builder Field Map.
- Keep a release-time screenshot/transcript record outside the public package if it contains private account details.
- Document exact model and capability state as live evidence, not memory.
- Treat model retirement/remapping as a release risk.

### Instructions

- Use clear headings and stepwise behavior.
- Use trigger/instruction pairs for workflows such as archive upload, unsafe ZIP, edit request, missing file, local filesystem request, or current-facts request.
- Keep prohibitions compact and pair them with safe alternatives.
- Include output contracts for artifacts, validation, and handoff.

### Knowledge

- Keep Knowledge public-safe, text-forward, versioned, and owned.
- Do not upload secrets, logs, private references, source ZIPs, generated artifacts, or maintainer scratch files.
- Prefer fewer high-signal files over broad undifferentiated material.
- Test whether the GPT actually uses the right Knowledge file for representative questions.

### Capabilities

- Enable only capabilities that support the product promise.
- Code Interpreter/Data Analysis should stay ON for uploaded-file and artifact work.
- Web search should be ON only if current public facts or citations are a product promise.
- Canvas is optional for long documents and policy drafts.
- Image generation is OFF by default for file/archive work.
- Apps are OFF for public Store path.
- Actions are OFF until there is real backend infrastructure.

### Actions

- Start from read-only endpoints where possible.
- Use least privilege and narrow schemas.
- Keep endpoint summaries and parameter descriptions concise.
- Return structured/raw data rather than persuasive prose.
- Require confirmation for consequential operations.
- Rate-limit, log, expire artifacts, and publish a privacy policy.
- Test actions in Preview and with adversarial prompts.

### Security And Privacy

- Treat uploaded files, web pages, connector content, and API responses as untrusted data.
- Assume prompt and Knowledge leakage attempts will occur.
- Do not store secrets in Instructions or Knowledge.
- Report secret-sensitive paths only, not bodies.
- Use deterministic validation around archives and artifacts.
- Mark unverified claims as `NOT VERIFIED`.

### Governance

- Assign owner/editor roles.
- Record who can edit the GPT and who can publish it.
- Keep release evidence tied to a version.
- Review workspace app/action restrictions before debugging a missing capability.
- Use issue/PR workflow for package changes rather than live untracked Builder edits.

## Implications For GPTsAgent Roadmap

Recommended near-term order from this review:

1. `v0.3.1` Builder Field Map: one canonical install sheet for every visible GPT Builder field. Implemented in the v0.3.1 package update; keep it current.
2. Preview evidence pack: record live Builder settings and results for critical prompts.
3. Eval expansion: missing capability, model transition, Apps disabled, Actions privacy-policy block, Knowledge-vs-Instructions conflict, and prompt leakage. Started in v0.3.1; keep adding fixtures when Builder surfaces change.
4. Knowledge quality review: ownership, freshness, exact 20-file package, no private material, no generated artifacts.
5. Public-pilot publish checklist: category, Builder Profile, visibility, capability state, model state, privacy caveats.
6. Actions design remains future-only until a backend exists.

Not recommended first:

- enabling Actions without backend;
- enabling Apps for a public Store-first GPT;
- adding more Knowledge files beyond 20;
- hard-coding a specific model promise;
- promising local filesystem access;
- treating prompt secrecy as a security boundary.

## Research-Derived Risk Register

| Risk | Why it matters | GPTsAgent control |
|---|---|---|
| Prompt injection | Uploaded files and web content can contain adversarial instructions. | Treat external content as untrusted, fail closed, eval injection cases. |
| Prompt/Knowledge leakage | Public GPTs can be probed for hidden instructions and uploaded content. | No secrets in package, refuse dumps, public-safe Knowledge only. |
| Excessive agency | Actions or Apps can turn text errors into real external effects. | Keep Actions/Apps off by default, confirmation gates, least privilege. |
| Stale Knowledge | Old docs can produce wrong behavior or wrong claims. | Versioned release package and freshness review. |
| Model drift | GPT model availability can change. | Live Builder evidence and retesting on model changes. |
| Governance drift | Live GPT UI edits can diverge from repository package. | Builder settings record and release checklist. |
| Store eligibility failure | Apps or missing Actions privacy policy can block public publish. | Public-pilot defaults: Apps off, Actions off. |
| False local-access promise | Users may expect the GPT to edit their computer. | Explicit uploaded-file/sandbox boundary in name, description, instructions, tests. |

## Final Synthesis

The strongest professional consensus is not "add more tools." It is:

- narrow the GPT's job;
- make Builder fields explicit;
- keep behavior in Instructions;
- keep Knowledge curated and safe;
- use tools only when they serve a validated workflow;
- treat external content as untrusted;
- measure behavior with realistic and adversarial prompts;
- govern releases like product changes.

For Sandbox File Operator, this confirms the current conservative direction: file-upload-first, Code Interpreter/Data Analysis ON, Actions OFF, Apps OFF for public pilot, exact 20-file Knowledge package, and an explicit artifact/validation workflow.

## Operational Rule

Use professional articles to improve product judgment and tests. Use official OpenAI docs and live Builder UI to make product claims.
