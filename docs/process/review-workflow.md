# Review workflow

## 1. Establish intent and scope

Read the requirement, change description, affected interfaces, and rollout
plan. Restate the intended observable behavior and identify what is explicitly
out of scope. Do not infer quality from the diff before understanding the goal.

## 2. Map the change

Identify changed state, trust boundaries, dependencies, public contracts,
deployment units, and operators. Select the quality dimensions that connect to
credible consequences; do not manufacture a comment for every dimension.

## 3. Review top-down and bottom-up

Top-down, ask whether the architecture, design, and product behavior are right.
Bottom-up, inspect changed expressions, branches, errors, resources, and tests.
Reconcile the two views: a safe local function can participate in an unsafe
system flow, and a sound architecture can contain a concrete line-level defect.

## 4. Form a finding

Use this chain:

> intent → observation → criterion → risk mechanism → failure mode → evidence → question → judgment → severity

Separate what is visible from what is inferred. When context is missing, ask the
smallest question that can change the judgment. Avoid style comments that a
formatter or established convention can decide.

## 5. Seek the strongest evaluator

Use compilers for types, tests for selected behavior, security tools for known
patterns and flows, benchmarks for performance, telemetry for runtime behavior,
and domain experts for intent. A weaker evaluator should not overrule stronger,
more relevant evidence without explaining why.

## 6. Decide and communicate

Classify the result as a defect, vulnerability, risk, tradeoff, question,
suggestion, or false positive. State the consequence, evidence, confidence, and
requested action. Group findings by root cause and avoid duplicating tool output.

## 7. Close the loop

Confirm the change, test, acceptance, or follow-up resolves the mechanism—not
only the cited line. Record accepted residual risk and its owner. Feed escaped
issues and rejected findings back into checklists, tests, rules, and this
knowledge base.
