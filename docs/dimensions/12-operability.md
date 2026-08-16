# Observability, operability, and deployment

## Purpose

Operable software can be understood, controlled, deployed, and recovered by the
people responsible for it. Observability supplies evidence for answering new
questions about runtime behavior; logging alone is not observability.

## Criteria

- Useful logging, metrics, tracing, and correlation.
- Diagnosability, alertability, actionable alerts, and ownership.
- Safe configuration and feature-flag lifecycle.
- Deployment, readiness, rollback, and progressive delivery.
- Administrative and operational controls, runbooks, and audit trails.

## Review questions

- How will an operator distinguish success, degradation, dependency failure, and bad input?
- Which signal triggers action, and who owns that action?
- Can configuration be validated before it affects traffic?
- How is the change rolled back when data or protocol changes are involved?

## Warning signals and failure modes

Unstructured sensitive logs, high-cardinality labels, unactionable alerts,
process-only health checks, permanent flags, and untested rollback can cause
blind incidents, alert fatigue, unsafe deployments, and prolonged recovery.

## Strong evidence

Dashboards tied to SLOs, trace examples, alert tests, game days, deployment
records, rollback rehearsals, runbooks, and incident feedback.

## Related dimensions

[Reliability](08-reliability.md), [performance](09-performance.md),
[security](07-security.md), and [change quality](15-pr-scope.md).
