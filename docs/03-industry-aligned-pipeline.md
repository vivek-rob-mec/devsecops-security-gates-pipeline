# Industry-Aligned DevSecOps Pipeline

This repository uses a 20-step reference flow. It is intentionally vendor-neutral and should be tailored.

1. Plan and security requirements
2. Threat modeling
3. Develop
4. Pull request / source controls
5. Secret scanning
6. SCA
7. SAST
8. IaC/configuration scanning
9. Unit/integration/security tests
10. Build once and publish to a restricted candidate registry when using registry-based signing
11. Artifact/container scanning by immutable digest
12. Generate SBOM
13. Sign and create provenance
14. Retain candidate artifact and trust evidence; candidate publication is not production approval
15. Deploy to staging
16. DAST and API security testing
17. Evaluate release policy
18. Deploy the same approved artifact to production
19. Runtime monitoring and detection
20. Feedback/remediation

## Fast-fail ordering

Cheap, high-confidence checks should usually execute early. A practical order is:

`checkout → secret scan → lint/IaC → dependency resolution/SCA → SAST → tests → build/candidate publication → image scan by digest → SBOM/sign → staging → DAST → release gate → production`

Parallelize independent scans after checkout to reduce lead time.

## Why the order matters

Code/configuration checks inspect source; image checks inspect the delivered content; DAST inspects the running candidate. Container signing commonly uses an image already stored in a restricted registry so its digest is known and signatures can be associated with it. Candidate storage does not authorize production use. Promote the approved digest, and never rebuild after approval. Some language analyzers need dependency resolution or compilation before analysis.

For the plain-language phase explanations and evidence flow, read [handbook lessons 8–12](DEVSECOPS_HANDBOOK.md#lesson-08). For actual script coverage and application integration requirements, use the [quickstart](implementation/quickstart.md).
