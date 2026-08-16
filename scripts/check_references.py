from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "references/source-registry.json"
TOPICS = {
    "python-middle-layer", "python-functional", "python-data-layer", "sql",
    "data-architecture", "data-engineering", "react", "node", "nextjs",
    "security", "prompt-design", "agent-design", "agent-engineering",
}


data = json.loads(REGISTRY.read_text())
sources = data["sources"]
ids = [source["id"] for source in sources]
assert len(ids) == len(set(ids)), "source IDs must be unique"
covered = {topic for source in sources for topic in source["topics"]}
assert TOPICS <= covered, f"uncovered topics: {sorted(TOPICS - covered)}"
for source in sources:
    assert source["url"].startswith("https://"), source["id"]
    local = source["local_copy"]
    if local:
        path = ROOT / local
        assert path.is_file(), f"missing local copy: {local}"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert source["sha256"] == digest, f"hash mismatch: {local}"
print(f"Reference registry OK: {len(sources)} sources, {len(covered)} topics")
