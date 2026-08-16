<!-- generated-from: a3-code-quality; do not edit -->

# Node.js

Node.js services rely on short event-loop tasks, bounded worker-pool work, explicit asynchronous failure handling, and controlled dependency/runtime exposure. Non-blocking APIs do not make CPU work or unbounded input harmless.

## Failure mechanisms

- CPU-heavy callbacks or pathological regular expressions deny fair scheduling.
- Promises reject without an owned recovery path.
- Streams ignore backpressure and accumulate memory.
- Cancellation, timeouts, and shutdown leave work or resources behind.
- Dependency scripts, prototype pollution, or unsafe configuration expand the attack surface.

## Review questions and evidence

Ask what runs on the event loop, how input size is bounded, where deadlines and cancellation propagate, and how overload is rejected. Use event-loop delay, heap, load, dependency, and hostile-input evidence.

## Counterexample

Moving work to a worker thread can add serialization and operational cost; bounded small work may be safer on the event loop.

## Worked case

An endpoint parses an unbounded JSON body and applies a costly regular expression. Input limits plus a linear parser keep event-loop delay within budget under hostile load; the test records p95 delay and rejection behavior rather than relying on asynchronous syntax.

## Tool-assisted review

Tools should measure delay, memory, dependency provenance, and static sinks. AI can connect observations across async flows but cannot declare absence of denial-of-service or supply-chain risk.

## References

- `node-event-loop`
- `node-security`
- `owasp-asvs`

---

Canonical knowledge ID: `node`  
Reference IDs: `node-event-loop`, `node-security`, `owasp-asvs`

## Editorial notes

<!-- editorial:start -->
_No publication-specific notes._
<!-- editorial:end -->
