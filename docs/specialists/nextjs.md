<!-- generated-from: a3-code-quality; do not edit -->

# Next.js

Next.js quality begins with an explicit server/client trust boundary and a version-pinned rendering and caching model. Server Components reduce client code, but data passed to a Client Component must be treated as browser-visible.

## Failure mechanisms

- Secrets or privileged records become serialized into client payloads.
- A Server Action checks authentication but not authorization for the requested object.
- Cache scope or invalidation serves stale or cross-tenant data.
- Dynamic APIs unexpectedly change rendering and caching behavior.
- Server Components call internal Route Handlers and add avoidable network hops.

## Review questions and evidence

Ask which code and data reach the browser, who authorizes every mutation, what cache key/scope/invalidation applies, and which Next.js major version was tested. Inspect built output, network payloads, cache tests, and production-like builds.

## Counterexample

Dynamic rendering is not inherently poor quality; personalized or request-bound data may require it. The defect is an accidental or unmeasured choice.

## Worked case

A Server Component passes an entire user record to a Client Component that needs only a display name. A data-transfer object narrows the payload, an authorization test guards the Server Action, and a browser/network assertion proves no secret field is serialized.

## Tool-assisted review

Static profiling can locate client boundaries, public environment variables, and actions. AI may explain the architecture only with versioned documentation and observed build/runtime evidence.

## References

- `next-production`
- `next-security`
- `react-purity`

---

Canonical knowledge ID: `nextjs`  
Reference IDs: `next-production`, `next-security`, `react-purity`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
