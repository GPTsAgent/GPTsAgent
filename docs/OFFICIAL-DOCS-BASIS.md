# Official OpenAI Docs Basis

Version: `v4.1.0`

Purpose: Record the official OpenAI sources checked when aligning GPTsAgent with current GPT Builder, Knowledge, Actions, Data Analysis, and publishing guidance.

Use this file when: updating Builder fields, package capabilities, public launch criteria, Actions guidance, or validation rules.

Related files: `config/GPT-BUILDER-CONFIG.md`, `config/CAPABILITIES-MAP.md`, `config/PUBLISHING-GPT-STORE.md`, `docs/PILOT-LAUNCH-CHECKLIST.md`

## Sources Checked

Accessed: `2026-05-04`

| Source | URL | Principle extracted | Integrated into |
|---|---|---|---|
| Creating and editing GPTs | `https://help.openai.com/en/articles/8554397-creating-a-gpt` | GPT Builder settings, model availability, Knowledge, capabilities, and Apps/Actions options are live product surfaces that can change. | `GPT-BUILDER-CONFIG.md`, `PILOT-LAUNCH-CHECKLIST.md`, `EVALUATION-CHECKLIST.md` |
| Knowledge in GPTs | `https://help.openai.com/en/articles/8843948-knowledge-in-gpts` | Knowledge is uploaded reference material with file limits; this package keeps a deliberate 20-file Knowledge architecture and validates it. | `MANIFEST.md`, `README.md`, `validate_workspace.py` |
| Configuring Actions in GPTs | `https://help.openai.com/en/articles/9442513-configuring-actions-in-gpts` | Actions require a real API design, OpenAPI schema, authentication choices, and privacy-policy handling before public use. | `ACTIONS-API-BLUEPRINT.md`, `PUBLISHING-GPT-STORE.md`, `GPT-BUILDER-CONFIG.md` |
| Data Analysis with ChatGPT | `https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt` | Data Analysis is the right capability for uploaded-file analysis, file transformation, charts, and generated artifacts; do not treat it as a general external-network or production host. | `CAPABILITIES-MAP.md`, `SANDBOX.md`, `GPT-BUILDER-CONFIG.md` |
| Sharing and publishing GPTs | `https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt` | Public sharing and GPT Store readiness require accurate public description, appropriate capability choices, and policy compliance. | `PUBLISHING-GPT-STORE.md`, `EVALUATION-CHECKLIST.md`, `README.md` |

## Integration Notes

- Keep behavior-critical rules in GPT Builder Instructions. Knowledge files support retrieval, examples, templates, and evaluation.
- Re-check the live Builder model menu before public release; do not hard-code a model name that may be retired or unavailable.
- Keep Actions off by default. If Actions are ever enabled, require backend ownership, OpenAPI schema, authentication, privacy policy, logging, rate limits, and explicit confirmation gates.
- Keep the public pilot file-upload-first. If Apps/connectors are enabled, do not also enable Actions unless current Builder docs explicitly allow that combination and the package is revalidated.
- Use Data Analysis for sandbox file/archive work and artifact generation. Use web search for current public facts and citations.
- Treat OpenAI docs as a current release input, not as permanent truth. Re-run this review before each public launch.

## Operational Rule

When OpenAI docs and package text conflict, update the package or mark the affected launch claim `NOT VERIFIED` before publishing.
