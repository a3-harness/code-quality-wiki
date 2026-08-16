# Maintainability, evolvability, and technical debt

## Purpose

Maintainability is the cost and risk of understanding, correcting, extending,
and retiring software. Technical debt is a deliberate or accidental compromise
whose future carrying cost matters; a TODO marker alone does not establish it.

## Criteria

- Change locality and predictable impact.
- Modifiability and extensibility aligned with plausible change.
- Explicit debt rationale, ownership, and exit conditions.
- Codebase consistency where consistency reduces surprise.
- Knowledge durability beyond individual memory.

## Review questions

- What is the next likely change, and how many places must it touch?
- Is this compromise necessary now, and who owns its removal trigger?
- Does the change introduce a second way to solve the same problem?
- Which essential decision exists only in conversation or tribal knowledge?

## Warning signals and failure modes

Shotgun edits, copied policy, abandoned toggles, version forks, undocumented
workarounds, and ownerless debt can cause rising lead time, regression risk,
dependency paralysis, and loss of critical knowledge.

## Strong evidence

Change-coupling history, lead-time trends, ownership data, dependency graphs,
debt registers tied to triggers, and small representative change exercises.

## Related dimensions

[Readability](02-readability.md), [design](03-design.md), and
[compatibility](13-compatibility.md).
