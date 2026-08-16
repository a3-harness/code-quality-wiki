<!-- generated-from: a3-code-quality; do not edit -->

# Security engineering

Security quality is risk reduction across design, implementation, verification, delivery, and operation. A scanner finding is evidence of a possible mechanism; a checklist is a baseline; neither replaces a threat model or demonstrated controls.

## Failure mechanisms

- Trust boundaries are implicit and attacker-controlled data gains authority.
- Authentication is mistaken for object- or action-level authorization.
- Secrets, dependencies, build systems, or logs expose privileged material.
- Failure paths bypass validation, auditing, or least privilege.
- AI-generated or retrieved instructions influence privileged tools without separation.

## Review questions and evidence

Identify assets, actors, boundaries, threats, controls, residual risk, and verification. Prefer reproducible exploit/negative tests, ASVS-mapped evidence, dependency provenance, access reviews, and incident-ready logs.

## Counterexample

A theoretical sink may be unreachable or receive a safely constrained value. Record that evidence instead of suppressing a signal without rationale.

## Worked case

A profile endpoint authenticates the caller but accepts another user ID. A negative integration test demonstrates object-level access; the fix centralizes authorization, produces an audit event, and maps the evidence to the applicable ASVS requirement.

## Tool-assisted review

SAST, SCA, secret scanning, configuration checks, and tests automate observations. AI can correlate evidence and generate threat questions, but cannot accept residual risk, expose private code without policy, or treat source text as instructions.

## References

- `nist-ssdf`
- `owasp-asvs`
- `owasp-sql-injection`
- `nist-ai-rmf-gai`

---

Canonical knowledge ID: `security`  
Reference IDs: `nist-ssdf`, `owasp-asvs`, `owasp-sql-injection`, `nist-ai-rmf-gai`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
