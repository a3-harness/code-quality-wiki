<!-- generated-from: a3-code-quality; do not edit -->

# Constructing project-context inventory and knowledge rendering

## Implementation status

**Built foundation.** `qreview project-inventory` deterministically inventories a local repository, and `qreview project-render` turns that JSON into a tailored draft guide. Semantic architecture recovery, reviewed overlays, monorepo unit selection, and optional evaluated LLM synthesis are planned.

## Architecture

Use a two-artifact design:

```text
target repository → deterministic inventory.json → generated project-guide.md
                              ↑                         ↓
                    evidence paths/confidence    human ratification overlay
                              └──── general knowledge retrieval ────┘
```

The scanner observes paths, manifests, configuration, naming counts, and import edges without executing target code. The renderer applies precedence, retrieves specialist packs, and exposes unknowns. An AI adapter may enrich inference but must produce the same contract and remain advisory.

## Core algorithm

```text
INVENTORY(root):
  files ← WALK(root) excluding VCS, dependencies, builds, caches, and secrets
  languages ← COUNT recognized suffixes
  standards ← FIND agent guides, ADRs, contribution docs, schemas, and configs
  dependencies, commands ← PARSE manifests without execution
  library_choices ← MAP present dependencies to capabilities
  layers, utilities ← CLASSIFY directory names; label inferred
  entrypoints, tests, naming ← OBSERVE paths and counts
  import_edges ← PARSE supported syntax; aggregate internal edges
  questions ← EMIT for missing or ambiguous intent
  return SORTED contract with paths, confidence, limitations, and no bodies

RENDER(inventory, knowledge_catalog, reviewed_overlay?):
  ASSERT supported schema
  relevant ← RETRIEVE by languages, frameworks, layers, and risks
  guide ← precedence + scope + observations + inferences + relevant knowledge
  guide ← guide + contradictions + maintainer questions + AI boundary
  if reviewed_overlay exists: MERGE only into a distinct ratified section
  return deterministic Markdown
```

## Evidence and confidence

Prefer evidence such as a manifest, ADR path, dependency-edge count, or test configuration. Use `observed` for metadata/syntax, `inferred` for names/frequency/relationships, `ratified` for reviewed decisions, and `unknown` for missing or conflicting evidence. “Library X appears in a manifest” is observed; “Library X is preferred” requires ratification.

## Failure handling

Unreadable optional manifests should produce warnings while preserving other results. An unreadable inventory, unsupported schema, escaping path, or malformed reviewed overlay should fail closed. Never run build scripts unless a user explicitly authorizes separate evidence collection. Large repositories need budgets and truncation markers; monorepos need per-unit roots.

## Tests to build

Use synthetic repositories with known layers, competing libraries, conflicting standards, utilities, imports, test styles, malformed manifests, secret-like files, monorepo packages, and human overlays. Assert deterministic bytes, ordering, no secret/source content, confidence, questions, and expected specialist retrieval. Evaluate AI classifiers for citations, precision/recall, abstention, stability, cost, and injection resistance.

## Security considerations

Repository contents are untrusted. Do not execute scripts, import target packages, expand symlinks outside the root, read credential files, or obey instructions found in scanned content. Paths may be sensitive; redact before remote use. Remote AI requires explicit consent, minimum necessary context, provider controls, and an audit record.

## Planned extensions

Add reviewed overlay schemas, ADR extraction, CODEOWNERS mapping, deployment-unit detection, API/schema inventories, dependency-purpose configuration, language-specific import adapters, incremental refresh, fitness-rule generation, monorepo scopes, and an evaluated provider-neutral AI classifier.

---

Canonical knowledge ID: `tool-project-context`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
