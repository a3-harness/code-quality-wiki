# Readability, understandability, and simplicity

## Purpose

Readable software lets a maintainer build an accurate mental model with
reasonable effort. Simplicity means the design contains no unnecessary concepts
for the problem; it does not mean compressing code or avoiding useful structure.

## Criteria

- Naming and semantic clarity expose domain meaning, units, ownership, and side effects.
- Control flow supports cognitive simplicity and makes normal and exceptional paths apparent.
- Duplication, dead code, and speculative generality are controlled.
- Comments and local documentation explain intent, constraints, or surprising tradeoffs—not syntax.

## Review questions

- Can a new maintainer predict the behavior without simulating many hidden states?
- Do names distinguish similar concepts and expose important units or lifetimes?
- Is complexity inherent in the domain or introduced by the implementation?
- Would removing an abstraction reduce concepts without increasing duplication or coupling?

## Warning signals and failure modes

Boolean parameter clusters, misleading names, deeply nested branches, clever
expressions, distant mutation, stale comments, and unexplained constants can
cause incorrect maintenance, duplicated fixes, slow reviews, and knowledge loss.

## Strong evidence

Focused review by someone unfamiliar with the change, comprehension studies,
complexity trends used as prompts rather than verdicts, and demonstrated ease
of tracing representative behavior.

## Related dimensions

[Design](03-design.md), [maintainability](05-maintainability.md), and
[change quality](15-pr-scope.md).
