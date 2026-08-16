<!-- generated-from: a3-code-quality; do not edit -->

# Constructing a reproducible wiki publisher

## Implementation status

**Built.** `scripts/publish_wiki.py` reads canonical catalogs and Markdown, preserves editorial regions, refuses to overwrite non-generated pages, emits route/content hashes and source commit metadata, and supports write and check modes. MkDocs then builds root GitHub Pages output.

## Architecture

Canonical content belongs in `a3-code-quality`; presentation belongs in `code-quality-wiki`. The public repository never imports raw extraction caches or unreviewed staging pages.

## Core algorithm

```text
PUBLISH(catalogs, target, mode):
  outputs ← empty map
  for item in every catalog:
    source ← canonical Markdown at item.route
    destination ← target/docs/item.route
    current_editorial ← extract protected editorial region(destination)
    rendered ← generated marker + source + canonical metadata
               + protected current_editorial
    outputs[destination] ← rendered

  manifest ← source commit + generator version
             + sorted(id, route, source, SHA256(rendered))
  outputs[target/publication-manifest.json] ← manifest

  if mode = CHECK:
    fail if any expected bytes differ
  else:
    refuse existing page without generated marker
    write outputs atomically where practical
```

After source generation, run a strict MkDocs build, copy only declared build paths to the repository root, and test navigation, search, sitemap, and every expected route.

## Failure handling

Route collisions, missing canonical files, non-generated destinations, malformed editorial markers, hash drift, and build warnings fail publication. Never delete unrelated target paths from an inferred glob.

## Tests to build

Use golden pages, no-change second runs, editorial preservation, collision fixtures, missing sources, source-commit format, all-route smoke tests, and root-output checks.

## Security considerations

Escape unsafe HTML, honor source licenses, exclude private text and secrets, and treat publication as an explicit external action. Generation may be automatic; commit and push require authorization.

## Planned extensions

Add atomic staging/swap, preview diffs, redirect manifests, link checking with cached network results, release signatures, and rollback by publication manifest.

---

Canonical knowledge ID: `tool-publication`  
Reference IDs: _See chapter links and canonical modules._

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
