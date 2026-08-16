# Change and pull-request quality

## Purpose

A reviewable change communicates intent, bounds risk, supplies evidence, and
can be deployed or reversed coherently. Small line count is useful only when the
change remains conceptually complete.

## Criteria

- Scope and coherence around one outcome.
- Rationale, requirement, and decision traceability.
- Risk assessment, rollout, migration, and rollback.
- Review coverage, specialist ownership, and evidence provenance.

## Review questions

- What user or system outcome changes, and what is explicitly unchanged?
- Can unrelated refactoring be separated without hiding essential context?
- Which tests, analyses, and observations support the claims?
- Who must review security, privacy, data, operations, accessibility, or architecture?

## Warning signals and failure modes

Mixed objectives, unexplained generated changes, missing migration plans,
screenshots without executable evidence, stale descriptions, and reviewer
selection by availability alone can cause missed risk, rubber-stamping, unsafe
rollout, and changes nobody can confidently reverse.

## Strong evidence

Linked requirements, focused diffs, test and analysis results, rollout plans,
specialist approvals, demo artifacts, and explicit residual-risk acceptance.

## Related dimensions

Every dimension can affect change quality; prioritize those connected to the
change's intent and credible failure modes.
