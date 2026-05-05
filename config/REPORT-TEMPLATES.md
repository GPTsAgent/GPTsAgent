# Report Templates

Version: `v0.2.0`

Purpose: Provide copy-ready reports for archive intake, deep updates, test-only passes, archive comparison, refusal/narrowing, and final artifact handoff.

Use this file when: the GPT needs a stable user-facing format for file, ZIP, validation, or refusal work.

Related files: `ARTIFACT-CONTRACT.md`, `FILE-WORKFLOW.md`, `PROMPT-LIBRARY.md`, `EVALUATION-CHECKLIST.md`

## Archive Intake Report

```markdown
## 1. OPERATING VERDICT
Status: PASS | PARTIAL | FAILED
Mode: ZIP_PREFLIGHT

## 2. ARCHIVE IDENTITY
- Source archive:
- Size:
- Entry count:
- Wrapper root:
- Project root candidates:

## 3. SAFETY CHECKS
- Openability:
- Central directory:
- Path traversal:
- Absolute paths:
- Duplicate entries:
- Case collisions:
- Symlinks:
- Encrypted entries:
- Oversized entries:
- Compression risk:
- Nested archives:
- Generated/binary-heavy paths:
- Secret-sensitive path names:

## 4. SANDBOX SESSION
- Allowed operations:
- Blocked operations:
- Recommended mode:
- Assumptions:

## 5. BLOCKED / NOT RUN

## 6. NEXT BEST MOVE
```

## Deep Update Report

```markdown
## 1. OPERATING VERDICT
Status:
Mode:

## 2. INPUT / SANDBOX SESSION
- Source evidence:
- Working copy:
- Protected files:
- Constraints:

## 3. WORK PERFORMED
- Audit:
- Patch plan:
- Files changed:
- Artifacts created:

## 4. VERIFICATION
- Diff:
- Manifest:
- Archive open check:
- Wrapper root:
- Secret-like scan:
- Tests:
- Checksum:

## 5. BLOCKED / NOT RUN

## 6. ARTIFACTS / NEXT BEST MOVE
- Updated ZIP:
- Diff:
- Manifest:
- Validation:
- Checksum:
```

## Test-Only Report

```markdown
## 1. OPERATING VERDICT
Status:
Mode: TEST_ONLY

## 2. TEST SCOPE
- Inputs:
- Commands or checks:
- Environment:

## 3. RESULTS
- Passed:
- Failed:
- Warnings:

## 4. LIMITATIONS
- Host-like checks:
- External dependencies:

## 5. BLOCKED / NOT RUN

## 6. NEXT BEST MOVE
```

## Compare Archives Report

```markdown
## 1. OPERATING VERDICT
Status:
Mode: COMPARE_ARCHIVES

## 2. INPUTS
- Baseline archive:
- Candidate archive:
- Wrapper roots:

## 3. CHANGE SUMMARY
- Added:
- Modified:
- Removed:
- Renamed or moved:
- Unchanged:

## 4. RISK NOTES
- Secret-sensitive paths:
- Generated/heavy changes:
- Binary changes:
- Unknowns:

## 5. BLOCKED / NOT RUN

## 6. ARTIFACTS / NEXT BEST MOVE
- Manifest:
- Diff:
- Recommendation:
```

## Artifact Recovery Report

```markdown
## 1. OPERATING VERDICT
Status: PARTIAL | FAILED | PASS
Mode: ARTIFACT_RECOVERY

## 2. FAILURE OR INTERRUPTION
- Failed artifact:
- Failure point:
- Error class:
- User-visible impact:

## 3. RECOVERY ACTION
- Partial artifacts discarded:
- Rebuilt from:
- Candidate output:
- Integrity checks:

## 4. VERIFICATION
- Archive open check:
- Wrapper root:
- Expected files:
- Manifest:
- Checksum:
- Secret-like scan:

## 5. BLOCKED / NOT RUN

## 6. FINAL ARTIFACTS / NEXT BEST MOVE
```

## Reference Distillation Report

```markdown
## 1. OPERATING VERDICT
Status: PASS | PARTIAL | FAILED
Mode: REFERENCE_DISTILLATION

## 2. REFERENCE BOUNDARY
- Reference use: private, pattern-only
- Source copied: no
- Private names retained: no
- Secret bodies read: no
- Public attribution requested: no

## 3. SAFE PATTERNS EXTRACTED
- Workflow patterns:
- Evaluation patterns:
- Safety patterns:
- Contributor-process patterns:

## 4. INTEGRATION
- Public files changed:
- Rewritten from scratch:
- Private provenance removed:

## 5. VALIDATION
- Private marker scan:
- Secret-like scan:
- Workspace validation:

## 6. BLOCKED / NOT RUN
```

## Refusal / Narrowing Report

```markdown
## 1. OPERATING VERDICT
Status: FAILED | PARTIAL

## 2. REQUEST BOUNDARY
I cannot help with the unsafe portion:

## 3. SAFE ALTERNATIVE
I can help with:
- defensive review;
- path-name-only secret hygiene;
- sanitized example;
- documentation;
- local checklist;
- safe repackage guidance.

## 4. NOT PROVIDED
- Unsafe operational details:
- Secret bodies:
- Destructive automation:

## 5. NEXT BEST MOVE
```

## Final Artifact Handoff

```markdown
## 1. OPERATING VERDICT
Status:
Version:

## 2. WHAT CHANGED
- Added:
- Modified:
- Removed:

## 3. VALIDATION PERFORMED
- Checks:
- Status:
- Limitations:

## 4. FILES UPDATED
- Files:
- Artifacts:

## 5. BLOCKED / NOT RUN

## 6. NEXT BEST MOVE
```

## Operational Rule

Use templates to make evidence, status, artifacts, and limitations visible rather than burying them in prose.
