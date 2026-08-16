# Wiki 01 deliverables status

Status: locally complete; branch-root publication awaiting external push.

| Deliverable | Status |
| --- | --- |
| MkDocs Material site | Complete |
| Fifteen dimension pages | Complete |
| Five process guides | Complete |
| Reader navigation and search | Complete |
| Strict local build | Complete |
| Root static HTML | Complete; awaiting push |
| Validation workflow | Complete; read-only drift check |
| Live public site | Pending external deployment |

## Local evidence

- MkDocs 1.6.1 / Material 9.7.7 strict production build passes.
- Site smoke check passes with 15 dimension pages and 140 searchable sections.
- Source-relative links resolve and every expected generated dimension page exists.
- Git diff whitespace validation passes.

## Publication handoff

The execution environment rejects `git push` because network mutation requires
an unavailable approval path. Push with `/code/push.sh --wiki-only`; keep the
repository's Pages source on **Deploy from a branch**, branch `main`, folder
`/(root)`, and verify the public URL.
