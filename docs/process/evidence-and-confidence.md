# Evidence and confidence

## Evidence hierarchy

Choose evidence matched to the claim:

| Claim | Strong evaluators |
| --- | --- |
| Syntax and types | Compiler, type checker |
| Deterministic convention | Formatter, linter |
| Known unsafe pattern or data flow | SAST, SCA, secret scanner, focused inspection |
| Selected behavior | Unit, integration, contract, property, fuzz, mutation tests |
| Performance and capacity | Benchmark, profiler, load/soak test, production telemetry |
| Runtime reliability | SLOs, metrics, traces, fault injection, incident history |
| Architecture fitness | Dependency analysis, fitness rules, ADRs, failure models |
| Intent and tradeoffs | Requirements, domain expertise, accountable decision maker |

Evidence is scoped. A passing unit test does not establish safe deployment; a
production metric does not prove behavior for an unobserved edge case.

## Observation versus inference

An observation is directly supported: “the added request has no timeout
argument.” An inference explains a plausible mechanism: “if no outer deadline
exists, a stalled dependency can retain the worker.” A judgment requires enough
context to decide whether that risk is present and unacceptable.

## Confidence

Confidence describes confidence in the finding, not severity of its impact.
Increase confidence with direct reproduction, complete control/data flow,
explicit requirements, and corroborating evidence. Reduce it for missing
context, unfamiliar frameworks, unreachable paths, ambiguous intent, or
assumptions about deployment.

Use plain language—high, medium, low—or a calibrated numeric scale. Never use
false precision to hide uncertainty. A low-confidence catastrophic possibility
may justify investigation without justifying a categorical accusation.

## Missing and conflicting evidence

State what is absent and why it matters. When evidence conflicts, compare its
scope, recency, representativeness, and evaluator strength. Preserve dissent and
uncertainty rather than averaging incompatible claims into confidence.
