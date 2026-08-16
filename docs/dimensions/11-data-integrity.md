# Data, state, and resource management

## Purpose

Data integrity means stored and transmitted state remains valid, attributable,
and consistent with domain rules. Resource management ensures finite resources
have clear acquisition, ownership, release, and failure semantics.

## Criteria

- Data models, constraints, and ownership.
- Transactions, migrations, and partial updates.
- Serialization, units, time, numeric precision, and versioning.
- File, socket, handle, memory, and lifecycle management.
- Persistence, retention, deletion, backup, and restoration semantics.

## Review questions

- Which invariants belong in code, schema constraints, or both?
- What happens if a migration stops halfway or old and new versions overlap?
- Are time zones, units, rounding, nullability, and encoding explicit?
- Who releases each resource on success, failure, timeout, and cancellation?

## Warning signals and failure modes

Read-modify-write races, non-atomic multi-record updates, lossy conversion,
naive timestamps, irreversible migrations, and leaked resources can cause
corruption, inconsistency, unrecoverable deletion, exhaustion, and legal risk.

## Strong evidence

Schema constraints, migration rehearsals, transaction tests, serialization
round trips, restore drills, resource-leak tests, and data-quality telemetry.

## Related dimensions

[Correctness](01-correctness.md), [concurrency](10-concurrency.md),
[compatibility](13-compatibility.md), and [security](07-security.md).
