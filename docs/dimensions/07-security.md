# Security and privacy

## Purpose

Security preserves intended confidentiality, integrity, availability, and
control under malicious or accidental misuse. Privacy governs justified data
collection and use across its lifecycle, not only access control.

## Criteria

- Trust boundaries and safe input/output handling.
- Authentication, session, and identity semantics.
- Authorization and least privilege at every resource boundary.
- Secrets and cryptography across key and credential lifecycles.
- Sensitive-data minimization, retention, deletion, and disclosure.
- Supply-chain integrity, secure failure, and auditability.

## Review questions

- Which data or actor crosses a trust boundary, and who validates the transition?
- Can one user act on another user's resource by changing an identifier?
- Where do secrets originate, rotate, expire, and appear in logs or history?
- What data is collected, why is it needed, and when is it deleted?

## Warning signals and failure modes

Client-enforced authorization, dynamic execution, broad credentials, disabled
verification, unsafe deserialization, sensitive logging, and unpinned build
inputs can lead to account takeover, injection, data disclosure, tampering, and
supply-chain compromise.

## Strong evidence

Threat models, abuse cases, data-flow diagrams, authorization matrices, SAST/SCA
and secret scanning, penetration tests, audit trails, and privacy review.

## Related dimensions

[Safety](14-safety.md), [data integrity](11-data-integrity.md),
[architecture](04-architecture.md), and [operability](12-operability.md).
