# Compatibility, portability, and dependencies

## Purpose

Compatibility preserves useful behavior across versions, clients, data, and
environments. Portability limits accidental dependence on one runtime.
Dependency management treats external code and services as evolving contracts.

## Criteria

- Backward and forward API, protocol, and data compatibility.
- Portability, adaptability, and explicit platform/environment assumptions.
- Dependency necessity, health, licensing, and update policy.
- Build reproducibility and verifiable inputs.

## Review questions

- Can old clients read new responses and new clients tolerate old servers?
- What happens during mixed-version deployment and rollback?
- Is this dependency worth its transitive code, privilege, and update burden?
- Can the same source and declared inputs reproduce the artifact?

## Warning signals and failure modes

Required-field additions, enum assumptions, destructive schema changes,
unpinned inputs, hidden platform behavior, and abandoned dependencies can cause
client breakage, lock-in, supply-chain exposure, and unreproducible releases.

## Strong evidence

Contract tests across versions, compatibility matrices, migration tests,
dependency inventories, SBOMs, reproducible-build checks, and deprecation telemetry.

## Related dimensions

[Architecture](04-architecture.md), [data integrity](11-data-integrity.md),
[security](07-security.md), and [maintainability](05-maintainability.md).
