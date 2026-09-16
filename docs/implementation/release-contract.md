# Production release contract

This is an implementation specification. `scripts/security-gate.sh` returns **2** until your application implements it. A generic script cannot establish your organization's trusted build identity, required test coverage, deployment permissions or approval authority from this folder alone.

## Inputs from trusted systems

| Input | Required checks |
| --- | --- |
| Candidate | Full immutable image digest, intended platform and source commit |
| Build | Trusted pipeline/run identity; successful real build and mandatory tests |
| Source scans | Completed mandatory secret, dependency, code and configuration scans for that source/run |
| Artifact assessment | Image scan and inventory refer to the approved digest/platform |
| Intelligence | Tool versions, rules revisions, actual advisory snapshot time and refresh outcome |
| Staging | Deployment record names the digest; health, authenticated DAST and required API tests completed |
| Signature | Cryptographic verification passes for the expected key or identity and issuer, with the expected subject digest |
| Provenance | Verified subject, approved builder and required source/material claims |
| Policy | Versioned thresholds, required scope and freshness rules from a protected location |
| Exceptions | Authenticated approvals with exact scope, owner, ticket, mitigation and unexpired UTC expiry |

Generate reports inside trusted CI. Do not accept arbitrary pull-request uploads or user-editable Boolean fields as proof of completion, signature verification or approval. A report's filesystem modification time is not trusted scan provenance.

## Decision logic

```text
load the protected policy and candidate identity
require every mandatory result and its authentic origin
reject failed, skipped, malformed or incomplete assessments
reject stale evidence and unsupported scope under the chosen policy
require consistent commit, build run, artifact digest and platform
verify signatures, expected identity and provenance claims independently
evaluate findings against policy
validate each needed exception against the authentic approval record
reject any unresolved blocking condition
record pass with reasons, policy version and exact approved digest
allow deployment only of that digest
```

This sequence is intentionally stricter than checking whether JSON parses. Parsing protects structure; it does not establish the truth or authenticity of the contents. A scanner can return a syntactically valid empty report after assessing the wrong directory.

## DAST acceptance contract

Before replacing `scripts/dast-scan.sh`, define:

- The explicitly authorized staging target and the candidate digest deployed there.
- Account roles, login/session validation, secret handling and required route coverage.
- Baseline/passive versus active mode; test-data reset, exclusions and request limits.
- Scanner version, add-on versions and alert-to-policy mapping.
- A report artifact and a machine-readable completion status.
- Handling for scan FAIL, WARN, operational error, timeout and authentication failure.
- Business-aware API assertions, including cross-user object access.

For ZAP packaged scripts, [baseline documentation](https://www.zaproxy.org/docs/docker/baseline-scan/) explains the exit statuses. A WARN is not a scanner crash; decide whether it blocks and preserve the original status in evidence. Do not use blanket failure suppression.

## Deployment binding

The deploy job must depend on the gate and consume its approved digest. Do not rebuild after approval or resolve a mutable tag again. Restrict who can edit workflow definitions, policy and approval records. Candidate registry access, production deployment access and signing permissions should be separately scoped.

For multiple platform images, record the index and applicable child digests. Prove that the deployment platform's content is within the scanned and approved set.

## Required integration acceptance cases

| Case | Expected result |
| --- | --- |
| Complete valid evidence below thresholds | Approve exact digest |
| Required report absent or scanner failed | Block |
| Zero results but mandatory scope unassessed | Block |
| Evidence for another run, commit, digest or platform | Block |
| Advisory data exceeds chosen freshness budget | Block or require a separately authenticated, policy-permitted exception |
| Invalid/unexpected signer or wrong provenance subject | Block |
| Unapproved, expired or out-of-scope exception | Block |
| Valid exception for one finding, second unresolved blocker | Block |
| Candidate changes after approval | Invalidate the approval and reassess |
| Reports or approval records supplied by untrusted code | Reject as untrusted evidence |

These cases require your real CI and trust systems. Repository mock tests only verify the current wrappers' local behavior.
