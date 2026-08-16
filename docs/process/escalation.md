# Escalation and specialist review

Ordinary pull-request review is not the right decision forum for every change.
Escalate when local evidence cannot responsibly establish system-level safety.

## Architecture or design review

Escalate changes to service boundaries, shared state ownership, public or
cross-team APIs, protocols, deployment topology, consistency models, or major
platform dependencies. Require alternatives, tradeoffs, migration, and rollback.

## Specialist review

Seek accountable expertise when the risk centers on security, privacy,
cryptography, concurrency, databases, accessibility, performance, operations,
legal obligations, regulated behavior, or physical safety. Specialist review
supplements rather than replaces normal ownership.

## Operational escalation

Escalate when a change can affect SLOs, irreversible data, incident controls,
regional failover, high-cardinality telemetry, or emergency access. Require an
operator-readable rollout and recovery path.

## How to escalate well

State the decision needed, deadline, known facts, uncertainty, credible failure
modes, affected parties, and existing evidence. Name the accountable decision
maker. Avoid vague “needs security review” labels with no described boundary.

Escalation is complete when the decision, rationale, residual risk, owner, and
follow-up trigger are recorded where future maintainers can find them.
