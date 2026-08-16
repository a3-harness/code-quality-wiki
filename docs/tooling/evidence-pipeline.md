<!-- generated-from: a3-code-quality; do not edit -->

# Constructing repository profilers and evidence adapters

## Implementation status

**Built foundation.** `qreview profile`, `evidence-import`, and `bundle` create low-content repository metadata, normalized observations, deterministic findings, and a review bundle. Compiler, coverage, query-plan, and SAST-specific adapters are planned.

## Architecture

Evidence adapters translate tool-specific output into observations; they do not translate observations directly into verdicts. Preserve the original tool, location, raw record when permitted, and a stable evidence ID.

## Core algorithms

```text
PROFILE(root):
  for file in recursive_files(root):
    skip .git, environments, dependencies, and build output
    count known language extensions
    inspect dependency manifests for framework names
  return counts and framework tags, never source contents

NORMALIZE(tool_name, records):
  for index, record in records:
    require non-empty observation
    id ← hash(tool_name, index, observation)
    emit {id, tool_name, kind, observation, path, line, raw}

BUNDLE(diff, profile):
  deterministic ← scan added lines with bounded rules
  knowledge_ids ← retrieve(profile, deterministic)
  return profile + deterministic + knowledge_ids
         + {untrusted_content: diff, human_judgment_required: true}
```

## Failure handling

Malformed manifests add an “unknown framework” fact rather than aborting profiling. Malformed evidence fails with the record index. Unknown file types are counted only as files. Never turn parser failure into “no findings.”

## Tests to build

Test ignored directories, malformed manifests, stable evidence IDs, absent locations, oversized input, rule deduplication, mixed-stack retrieval, and serialization without source leakage.

## Security considerations

Paths, diffs, tool output, and diagnostics may contain secrets or prompt injection. Redact before remote use, keep raw evidence optional, and render it as quoted data—not executable control text.

## Planned extensions

Add adapters for SARIF, pytest/JUnit, coverage, dependency inventories, migration tools, database plans, and telemetry snapshots. Each adapter needs fixtures and an explicit trust/provenance label.

---

Canonical knowledge ID: `tool-evidence-pipeline`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
