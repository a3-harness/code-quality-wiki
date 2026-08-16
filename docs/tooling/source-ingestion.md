<!-- generated-from: a3-code-quality; do not edit -->

# Constructing a source-ingestion tool

## Implementation status

**Built.** `llm_wiki` scans immutable references, extracts supported formats, records hashes and warnings, creates staging pages, skips unchanged inputs, and exports metadata without source text by default.

## Architecture

Keep raw files, extracted text, metadata, and synthesized knowledge separate. Raw files are evidence and never rewritten. A workspace ID tracks a local path; an external canonical ID joins the source to other repositories. The manifest records both so relocation does not break citations.

```text
immutable file → scan/hash → typed extractor → normalized Markdown
                         ↘ manifest ↘ staging source page
                                      ↘ metadata-only export
```

## Core algorithm

```text
INGEST(file, external_id, force=false):
  assert file extension is supported
  digest ← SHA256(file bytes)
  workspace_id ← stable_hash(relative workspace path)
  previous ← manifest.sources[workspace_id]

  if previous.digest = digest and not force:
    return UNCHANGED

  if generated page exists and page_digest ≠ previous.page_digest:
    fail "reviewed page would be overwritten"

  extraction ← EXTRACT_BY_TYPE(file)
  write normalized extraction with page/slide markers
  write generated staging page
  manifest.sources[workspace_id] ← metadata + warnings + external_id
  append ingest event to log
```

Export metadata by default. Require a separate `include_extracted` capability because extracted text may contain private or redistribution-restricted material.

## Failure handling

Unsupported formats are reported, not silently ignored. Partial extraction keeps warnings. Unsupported manifest versions fail closed. Edited generated pages block force-ingest instead of losing human work. A corrupt document affects one source, not the entire manifest.

## Tests to build

Test each extractor with small fixtures; verify page/slide markers, deterministic hashes, unchanged-file skipping, path relocation with stable external IDs, edited-page conflicts, metadata-only exports, and raw-source immutability.

## Security considerations

Treat documents and extracted text as untrusted data. Do not execute macros, scripts, embedded links, or model instructions. Bound file size and parser time in hostile environments and isolate high-risk native parsers.

## Planned extensions

Add sandboxed OCR, archive-bomb limits, MIME/signature checks, malware scanning, and reviewed synthesis plans. These are planned; they are not present in the current ingestion command.

---

Canonical knowledge ID: `tool-source-ingestion`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
