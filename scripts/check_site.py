from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
DIMENSION_RE = re.compile(r"^\d{2}-[a-z0-9-]+\.md$")
LINK_RE = re.compile(r"\[[^]]+\]\(([^) #]+)(?:#[^)]+)?\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


dimensions = sorted(path for path in (DOCS / "dimensions").glob("*.md") if DIMENSION_RE.match(path.name))
if len(dimensions) != 15:
    fail(f"expected 15 dimension sources, found {len(dimensions)}")

required_processes = {
    "review-workflow.md",
    "evidence-and-confidence.md",
    "severity-and-decisions.md",
    "escalation.md",
    "contributing-knowledge.md",
}
actual_processes = {path.name for path in (DOCS / "process").glob("*.md")}
if not required_processes <= actual_processes:
    fail(f"missing process pages: {sorted(required_processes - actual_processes)}")

for page in [DOCS / "index.md", *dimensions, *((DOCS / "process").glob("*.md"))]:
    for target in LINK_RE.findall(page.read_text(encoding="utf-8")):
        if "://" in target:
            continue
        if not (page.parent / target).resolve().is_file():
            fail(f"broken source link in {page.relative_to(ROOT)}: {target}")

index_html = SITE / "index.html"
if not index_html.is_file() or "Software Quality Knowledge Base" not in index_html.read_text(encoding="utf-8"):
    fail("generated home page is missing or has the wrong title")

for page in dimensions:
    generated = SITE / "dimensions" / page.stem / "index.html"
    if not generated.is_file():
        fail(f"missing generated page for {page.name}")

search_index = SITE / "search" / "search_index.json"
if not search_index.is_file():
    fail("search index was not generated")
documents = json.loads(search_index.read_text(encoding="utf-8"))["docs"]
if len(documents) < 21:
    fail(f"search index is unexpectedly small: {len(documents)} documents")

print(f"Site smoke check passed: {len(dimensions)} dimensions, {len(documents)} searchable documents.")
