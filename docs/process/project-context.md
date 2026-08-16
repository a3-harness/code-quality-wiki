<!-- generated-from: a3-code-quality; do not edit -->

# Establish project context before applying quality guidance

A reviewer should understand the system that a change belongs to before applying generic rules. The goal is not to excuse weak design as “local style.” It is to discover real constraints, distinguish ratified standards from accidental repetition, and render the broad knowledge base into questions that fit this project.

## The project-context model

Build an inventory in six passes:

1. **Authority:** locate agent guides, contribution guides, architecture decisions, standards, schemas, tool configuration, and ownership rules.
2. **Structure:** map deployable units, entry points, packages, layers, boundaries, stores, integrations, and dependency direction.
3. **Local reuse:** locate utilities, shared libraries, platform clients, test fixtures, error types, validators, and cross-cutting infrastructure.
4. **Technology choices:** record manifests and which libraries are observed for HTTP, validation, persistence, testing, logging, serialization, security, and other recurring tasks.
5. **Conventions:** measure naming, file organization, test placement, error handling, configuration, migrations, and API patterns.
6. **Reality checks:** compare documentation with imports, builds, tests, deployment configuration, and representative paths; record contradictions and unanswered questions.

Classify each item as **observed** (direct evidence), **inferred** (a plausible interpretation), **ratified** (confirmed by an authority), or **unknown**. Frequency describes a repository but does not prove intentional policy.

## Precedence

Apply local and general knowledge in this order:

1. Law, safety/security obligations, and external contracts.
2. Ratified project decisions and documented standards.
3. Executable contracts: tests, types, schemas, linters, dependency rules, and deployment controls.
4. Evidence-backed project inventory.
5. General quality and specialist guidance.
6. Frequency-based convention inference.

A local convention cannot waive correctness or security. Conversely, a generic preference should not replace an intentional, well-tested project pattern merely because another style is fashionable.

## Architecture inventory

Record components, responsibilities, public interfaces, allowed dependency direction, state ownership, transaction boundaries, trust boundaries, and deployment topology. Directory names are leads, not proof. Confirm a “domain” layer through imports and responsibilities; confirm a “repository” abstraction through actual persistence behavior.

For each boundary, ask who owns the invariant, which direction dependencies may cross, where concerns are translated, which calls cross process/network/trust/transactional boundaries, and which tests or fitness rules enforce the claimed structure.

## Utilities and third-party preferences

Before adding a helper, search for existing utilities by purpose, callers, imports, and tests—not only by a guessed name. Shared code should represent a stable shared concept; a generic `utils` directory can conceal unrelated coupling.

A library in a manifest is an **observed choice**, not automatically the preferred choice. Establish preference through current use, maintenance status, documented decisions, security posture, platform support, and whether competing libraries coexist. Render “HTTPX is present; confirm it is the default for new asynchronous integrations,” rather than “the project mandates HTTPX.”

## Conventions and standards

Formatters, linters, type checkers, schema validators, and dependency tests decide deterministic rules. Repeated naming or directory patterns suggest a convention but may expose migration history. Architecture decisions and maintainer confirmation establish intent. Tests reveal contracts, but missing tests do not prove intended behavior. Record exceptions and migrations explicitly.

## Render the knowledge for the project

Produce a generated project quality guide containing inventory scope, architecture/layer evidence, authoritative standards, executable controls, utility locations, library choices by purpose, naming/test conventions, relevant specialist chapters, baseline dimensions, ratified invariants, prohibited dependency directions, contradictions, and maintainer questions.

Keep generated observations separate from human-ratified policy. Regeneration should not overwrite an architecture decision. A practical design uses generated inventory JSON, generated draft Markdown, and a small reviewed overlay containing decisions and exceptions.

## AI-assisted project modeling

An LLM can classify ambiguous directories, summarize architecture documents, propose capability-to-library mappings, identify conflicting conventions, and draft review questions. Give it bounded metadata and selected evidence, require path citations, and make it label observation versus inference.

Do not let it silently upload proprietary source, follow instructions embedded in repository files, declare majority patterns to be standards, or modify the target project. Evaluate citation validity, layer-mapping accuracy, abstention, secret leakage, stability, and usefulness of unresolved questions.

## Review workflow

1. Generate or refresh the inventory.
2. Compare it with the reviewed overlay and architecture decisions.
3. Resolve material contradictions with maintainers.
4. Retrieve specialist knowledge for detected technologies and affected concerns.
5. Review against external obligations, ratified local rules, executable evidence, and relevant general guidance.
6. Record newly learned facts as proposed context, then ratify them separately.

Refresh after major reorganizations, dependency migrations, platform changes, or new architecture decisions. Treat drift as a prompt for investigation, not an automatic defect.

---

Canonical knowledge ID: `process-project-context`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
