# Severity and decisions

## Factors

Assign severity after understanding the mechanism. Consider consequence,
likelihood, exposure, reversibility, detectability, and confidence. Category
alone is insufficient: the same timeout defect has different impact in an
offline script and a saturated request path.

| Level | Meaning | Default decision |
| --- | --- | --- |
| P0 — Critical | Credible catastrophic, widespread, exploitable, safety-critical, or irreversible harm | Block and escalate immediately |
| P1 — High | Likely serious correctness, security, privacy, reliability, concurrency, contract, or architectural harm | Normally block |
| P2 — Medium | Meaningful bounded risk or material future cost | Fix now or explicitly accept |
| P3 — Suggestion | A clearly preferable approach when current behavior is adequate | Non-blocking |
| P4 — Nit | Optional style, naming, or wording preference | Never block |

## Decision types

- **Fix:** evidence establishes an unacceptable problem in the current change.
- **Accept risk:** an authorized owner understands the consequence and records
  rationale, duration, and follow-up trigger.
- **Investigate:** consequence could be material but decisive context is missing.
- **Defer:** work is valuable but not required for the current outcome; create a
  traceable owner and trigger when the cost is real.
- **Reject finding:** the mechanism is absent, unreachable, already controlled,
  or based on an incorrect assumption.

## Calibration rules

Do not raise severity to force attention. Do not lower it because a fix is
expensive. Separate confidence from consequence. Calibrate against incidents,
accepted risks, user harm, and team policy—not comment tone or reviewer rank.
