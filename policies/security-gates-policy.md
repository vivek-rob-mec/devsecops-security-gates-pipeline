# Security Gates Policy — Reference Template

> Example policy only. Tune for your organization.

## Current executable baseline

The richer policy below is target guidance. The current wrappers block Trivy HIGH/CRITICAL results (including unfixed issues), configured Gitleaks matches (not verified credential activity), and findings from the explicitly selected Semgrep ruleset. They do not automatically enrich KEV/EPSS, prove reachability, validate exceptions or verify a production release. DAST and release integration stubs return exit 2 until implemented. See the [quickstart](../docs/implementation/quickstart.md) and [release contract](../docs/implementation/release-contract.md).

## Gate 1 — Secret scanning

- Verified active secret: **BLOCK**.
- Suspected false positive: review before suppression.
- Any exposed real secret: rotate/revoke even if removed from code.

## Gate 2 — SCA / vulnerability

Suggested production policy logic:

- known-exploited or highly exploitable critical/high risk affecting the deployed path: **BLOCK** unless approved exception;
- fixable critical risk in release artifact: **BLOCK** by default;
- lower risk: track according to remediation SLA;
- new findings should receive stricter treatment than accepted legacy baseline.

## Gate 3 — SAST

- high-confidence critical vulnerabilities introduced by the change: **BLOCK**;
- repeated false positives require rule tuning, not indefinite manual dismissal.

## Gate 4 — IaC / container

- privileged/root/public-exposure policies defined by platform security: **BLOCK** where prohibited;
- release image must be scanned by digest.

## Gate 5 — Supply chain

- release artifact must have expected digest;
- SBOM required for production release where policy requires it;
- signature/provenance must verify when enforcement is enabled.

## Gate 6 — DAST / API

- reproducible critical/high-impact vulnerabilities in staging: **BLOCK** unless approved exception;
- active scan must target an authorized environment.

## Gate 7 — Release

Release only if all required checks are successful or every bypass has a valid, approved, unexpired exception.
