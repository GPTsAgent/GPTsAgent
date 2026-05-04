# File Workflow

Version: `v0.1.0`

Purpose: Define the ZIP-in, sandbox-work, artifact-out process and mode selection rules for file, archive, project, and artifact tasks.

Use this file when: the GPT needs to choose a safe workflow for uploaded files, projects, or ZIP archives.

Related files: `SANDBOX.md`, `ZIP-SAFETY-POLICY.md`, `ARTIFACT-CONTRACT.md`, `REPORT-TEMPLATES.md`

## Workflow Thesis

Every serious file task should move through a visible pipeline:

```text
user goal -> input inventory -> safety classification -> mode selection -> evidence map -> bounded work -> validation -> artifact handoff
```

## Mode Catalog

| Mode | Use when | Mutation |
|---|---|---:|
| READ_ONLY_ORIENTATION | User needs explanation, summary, inventory, or plan. | No |
| SAFETY_SCAN | User uploads or references ZIP/archive. | No |
| PATCH_ONLY | Known bounded text files can be edited without broad extraction. | Yes |
| LIGHT_EXTRACTION | Context is needed but secrets, generated paths, and heavy files can be skipped. | Possible |
| FULL_EXTRACTION | Safe archive and explicit task require broad project context. | Possible |
| TEST_ONLY | Validate syntax, artifacts, or sandbox-safe checks without source changes. | No source edits |
| COMPARE_ARCHIVES | User supplies two archives or file sets. | No |
| UPDATE_ARCHIVE | User requests edited or repackaged ZIP output. | Yes, in artifact |

## Intake

Identify:

- user goal;
- available files;
- active archive if any;
- target output;
- constraints;
- protected files;
- current facts requiring web search;
- unsafe or sensitive elements;
- validation requirements.

If no file is available for file work, explain the upload or scoped-integration boundary.

## Safety Classification

Classify the request as:

- safe answer;
- safe read-only file inspection;
- archive preflight required;
- bounded edit;
- artifact build;
- current research;
- sensitive but narrowable;
- unsafe and refused.

Proceed with the safe subset. Do not let one unsafe portion block safe documentation, auditing, or placeholder work when a safe path exists.

## Evidence Map

Separate:

- user statements;
- uploaded source evidence;
- archive metadata;
- sandbox-generated evidence;
- web evidence;
- model assumptions;
- unverified host-like claims.

Use `NOT VERIFIED` when the evidence source cannot prove a claim.

## Mode Selection Rules

- Choose READ_ONLY_ORIENTATION when the goal is vague or no mutation is needed.
- Choose SAFETY_SCAN before any archive extraction or update.
- Choose PATCH_ONLY for known docs, prompts, manifests, templates, and policy files.
- Choose LIGHT_EXTRACTION when project context is needed but broad extraction is unnecessary.
- Choose FULL_EXTRACTION only after a passing safety scan and explicit need.
- Choose TEST_ONLY for validation runs that should not alter source files.
- Choose COMPARE_ARCHIVES when the user asks what changed between versions.
- Choose UPDATE_ARCHIVE only after safe scan, bounded edit plan, and artifact validation.

## Patch Plan

Before edits, define or infer:

- objective;
- selected source;
- target files;
- protected files;
- edit method;
- expected outputs;
- validation plan;
- rollback or repair path.

For broad "do your best" requests, make a conservative high-value pass and report assumptions.

## Edit Discipline

Allowed edit behavior:

- targeted;
- reversible;
- consistent with source structure;
- documented in a diff and manifest;
- validated before handoff.

Avoid:

- unrequested deletion;
- generated-file mutation;
- broad reformatting;
- dependency installation;
- unknown executable execution;
- changing security posture silently;
- reading secret bodies.

## Validation Gate

For edited output, check:

- expected files exist;
- diff exists for text changes;
- manifest matches changes;
- changed text contains no obvious secret-like material;
- archive opens if a ZIP was built;
- wrapper root is preserved or change is documented;
- no unexpected removals occurred;
- checksum exists for major ZIP outputs when possible.

## Handoff

End substantial work with:

1. OPERATING VERDICT
2. INPUT / SANDBOX SESSION
3. WORK PERFORMED
4. VERIFICATION
5. BLOCKED / NOT RUN
6. ARTIFACTS / NEXT BEST MOVE

## Operational Rule

No archive update is complete until the updated artifact, diff, manifest, validation report, and limitations are aligned.
