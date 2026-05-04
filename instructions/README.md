# GPTsAgent Instructions

Canonical system instructions for the GPTsAgent Sandbox File Operator Custom GPT.

Use `SYSTEM-INSTRUCTIONS.txt` when you need the exact instruction text without Markdown wrapping. Use `INSTRUCTIONS.md` when reviewing the same instructions in GitHub.

These instructions are designed to work together with the 20 Knowledge files in `../config/`. The instructions define behavior; the configuration files provide retrieval-friendly policy, examples, templates, and evaluation criteria.

## Boundary

This is an operating layer for ChatGPT.com sandbox workflows. It does not give ChatGPT direct access to a user's local filesystem, private repositories, CI, cloud account, or production host.
