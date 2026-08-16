# Software Quality Knowledge Base

Practical, evidence-first guidance for reviewing software changes and systems.
Use it to ask better questions, choose stronger evidence, and distinguish an
observable signal from a defensible engineering judgment.

> **Guiding principle:** automate facts; assist inference; escalate judgment.

[Start the review workflow](process/review-workflow.md){ .md-button .md-button--primary }
[Browse quality dimensions](dimensions/01-correctness.md){ .md-button }

## How to use this wiki

1. **Establish intent.** Understand the outcome, constraints, and affected users.
2. **Select relevant lenses.** Choose dimensions connected to credible failure modes.
3. **Follow the evidence.** Match each claim to the strongest available evaluator.
4. **Make the judgment explicit.** State mechanism, consequence, confidence, and decision.
5. **Escalate when needed.** Pull system-level or specialist decisions out of ordinary line review.

The dimensions are lenses, not quotas. A reviewer should not manufacture one
comment per category.

## Quality dimensions

<div class="dimension-grid" markdown>

<div markdown>
### Behavior

[Correctness](dimensions/01-correctness.md) ·
[Test quality](dimensions/06-test-quality.md) ·
[Data integrity](dimensions/11-data-integrity.md)
</div>

<div markdown>
### Structure

[Readability](dimensions/02-readability.md) ·
[Design](dimensions/03-design.md) ·
[Architecture](dimensions/04-architecture.md) ·
[Maintainability](dimensions/05-maintainability.md)
</div>

<div markdown>
### Adversity

[Security and privacy](dimensions/07-security.md) ·
[Reliability](dimensions/08-reliability.md) ·
[Concurrency](dimensions/10-concurrency.md) ·
[Safety and compliance](dimensions/14-safety.md)
</div>

<div markdown>
### Runtime and change

[Performance](dimensions/09-performance.md) ·
[Operability](dimensions/12-operability.md) ·
[Compatibility](dimensions/13-compatibility.md) ·
[Change quality](dimensions/15-pr-scope.md)
</div>

</div>

## Review process

- [Review workflow](process/review-workflow.md): intent through feedback loop.
- [Evidence and confidence](process/evidence-and-confidence.md): match claims to evaluators.
- [Severity and decisions](process/severity-and-decisions.md): calibrate consequence and action.
- [Escalation](process/escalation.md): recognize when ordinary PR review is insufficient.

## Knowledge model

Every concern should move through a transparent reasoning chain:

> intent → observation → criterion → risk mechanism → failure mode → evidence → question → judgment → severity

The chain prevents a familiar pattern from being reported as a proven defect
without context. It also makes disagreement productive: reviewers can identify
which observation, assumption, mechanism, or decision differs.
