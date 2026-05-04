# Actions API Blueprint

Version: `v0.1.0`

Purpose: Design an optional future Actions backend with safe high-level endpoints, authentication, privacy, audit logging, rate limits, and artifact expiration.

Use this file when: planning a real backend for Sandbox File Operator Actions.

Related files: `CAPABILITIES-MAP.md`, `SECRET-HYGIENE.md`, `SAFETY-REFUSAL-POLICY.md`, `ARTIFACT-CONTRACT.md`

## Default Position

Actions are optional and OFF by default. The GPT works first as an uploaded-file sandbox assistant. Do not configure Actions until there is a real backend, threat model, OpenAPI schema, authentication model, privacy policy, test plan, audit log, rate limits, and artifact lifecycle.

Current public-pilot rule: do not combine Actions with Apps/connectors in the same GPT. Keep Actions off unless the backend exists and current Builder docs explicitly support the intended capability mix.

## Non-Negotiable Prohibition

Raw shell endpoints are forbidden. Do not expose:

- `run_shell`;
- `exec`;
- `bash`;
- `read_any_file`;
- `write_any_file`;
- `delete_path`;
- `download_and_execute`;
- unrestricted path operations;
- arbitrary network fetch plus execution;
- endpoints that infer destructive actions from natural language.

## Design Principle

Expose high-level operations with narrow parameters and structured results. The backend, not the model, enforces sandboxing, path allowlists, secret denylists, resource limits, and artifact retention.

## Authentication Model

Choose one:

- OAuth for user-owned data and account-specific access.
- API key authentication for server-to-server operations when no user account is involved.
- No auth only for intentionally public, read-only, non-sensitive endpoints.

Never place credentials in GPT Instructions, Knowledge files, examples, conversation starters, or reports.

## Privacy Policy Requirements

Public GPTs with Actions must provide a valid privacy policy URL. The policy should explain:

- what files or metadata are sent to the backend;
- retention period;
- deletion behavior;
- logging;
- who can access artifacts;
- subprocessors if any;
- training/data-use posture;
- secret-handling policy;
- user deletion request path.

## Backend Controls

- per-user isolated sessions;
- storage and time limits;
- no privileged containers;
- no network by default unless endpoint requires it;
- archive safety scanning before extraction;
- secret path denylist;
- safe text encoding handling;
- malware scanning where appropriate;
- artifact expiration;
- signed short-lived artifact URLs;
- audit logs;
- rate limits;
- abuse monitoring;
- human confirmation for consequential actions.

## Endpoint Families

| Family | Example endpoints | Notes |
|---|---|---|
| Sessions | `POST /sessions`, `GET /sessions/{session_id}`, `DELETE /sessions/{session_id}` | Create and expire isolated workspaces. |
| Archive intake | `POST /sessions/{session_id}/archives`, `POST /sessions/{session_id}/archives/{archive_id}/scan` | Upload/register and scan before extraction. |
| Tree and metadata | `GET /sessions/{session_id}/archives/{archive_id}/tree` | Return metadata, not secret bodies. |
| Safe file read | `POST /sessions/{session_id}/files/read_safe_text` | Enforce allowlists and deny secret-sensitive paths. |
| Patch planning | `POST /sessions/{session_id}/patches/plan` | Validate bounded plan before mutation. |
| Patch apply | `POST /sessions/{session_id}/patches/apply` | Apply only approved bounded patches. |
| Artifact build | `POST /sessions/{session_id}/artifacts/build_zip` | Generate ZIP, diff, manifest, validation, checksum. |
| Validation | `POST /sessions/{session_id}/validate` | Return structured status and evidence. |
| Audit | `GET /sessions/{session_id}/audit-log` | User-visible session audit. |

## Safe Endpoint Response Pattern

```json
{
  "status": "PASS",
  "summary": "Archive metadata scanned successfully.",
  "evidence": [
    {"kind": "scan", "name": "zip-safety", "status": "PASS"}
  ],
  "artifacts": [
    {"name": "validation.md", "url": "<ARTIFACT_URL>", "sha256": "<SHA256>"}
  ],
  "limitations": ["Sandbox-only validation."]
}
```

## OpenAPI Schema Rules

- Use clear operation IDs.
- Use precise endpoint descriptions.
- Use typed request bodies.
- Use enums for modes and status labels.
- Use explicit confirmation fields for consequential operations.
- Return structured `status`, `evidence`, `artifacts`, and `limitations`.
- Avoid vague endpoints such as "do_task" or "run_command".

## Consequential Operation Rule

Any operation that deletes, publishes, sends, submits, modifies external state, changes permissions, rotates secrets, spends money, or consumes scarce resources must require explicit user confirmation and backend-side enforcement.

## Operational Rule

Do not enable Actions for this GPT until the backend makes unsafe actions structurally impossible, not merely discouraged by prompt text.
