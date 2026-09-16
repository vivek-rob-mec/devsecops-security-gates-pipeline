# Project review and implementation status

Reviewed 2026-09-16. The provided folder is a downloaded project without `.git` metadata, so this review does not include commit history. The source presentation and original 40-slide expanded presentation are preserved under `presentation/source-original/`.

## Findings and corrections

| Finding | Impact | Correction |
| --- | --- | --- |
| Dense presentation; acronyms and mechanisms underexplained | Readers could recognize tool names without understanding what evidence they provide | Rebuilt course with staged flow, working principles, examples, notes, glossary and offline handbook |
| Markdown spacing and table formatting inconsistent | Documentation lint failed and rendering was inconsistent | Applied 278 formatter fixes across 54 files; final lint is clean |
| Release gate printed a placeholder and returned success | Incomplete release verification appeared to pass | Gate now stops with exit 2 and points to the application release contract |
| DAST printed instructions and returned success | A pipeline could imply that dynamic testing occurred | Stub now stops with exit 2 until integrated |
| Trivy wrappers did not request failure on findings or load stored config | Reports could contain vulnerabilities without blocking CI | Explicit config and `--exit-code 1`; HIGH/CRITICAL baseline retained |
| Semgrep fetched auto rules without enforcing finding failure | Scope was mutable and findings could pass | Explicit local/configurable rules with `--error`, `--strict`, disabled metrics and clear limited-scope documentation |
| Secret wrapper relied on repository history command and implicit config | ZIP worktrees and stored config could be mishandled | Worktree scan plus reachable-history scan when available; explicit config and redacted reports |
| Image/SBOM/signing accepted mutable references | Scan and signing targets could differ from released content | Validate an explicit SHA-256 image digest before execution |
| Jenkins/GitLab suppressed scanner/SBOM failures | Required failures were ignored | Removed suppression; Java/Node chaining now preserves failures |
| Preflight checked little beyond version display | Missing scanner prerequisites were discovered late | Check required source-scanner commands and report setup guidance |
| Generated evidence not preserved consistently | Failure investigation could lose scanner reports | Added report retention to full GitHub template, GitLab defaults and active Trivy workflow |
| Active Trivy action used mutable `master` | Unreviewed upstream changes could alter CI execution | Pinned the verified v0.35.0 release commit |
| Source/build/sign/publish order was ambiguous for registry signing | Users could try to sign a not-yet-published container reference | Canonical flow explains restricted candidate publication before digest-based scan/sign and later approved promotion |

The Trivy action pin was resolved from the [official release](https://github.com/aquasecurity/trivy-action/releases/tag/v0.35.0) and [full commit](https://github.com/aquasecurity/trivy-action/commit/57a97c7e7821a5776cebc9bb87c984fa69cba8f1). This is not a blanket audit of its transitive dependencies or every action in the project. Continue reviewing nested actions, tool downloads and version updates.

## Important implementation boundaries

- The folder has no application, production target, configured scanner service or deployment credentials.
- `pipelines/` contains integration templates. Hosted CI runners are not guaranteed to have the required scanners; tool provisioning must be added.
- Existing explanatory build/test/deploy steps are not real implementations. DAST and release entry points fail explicitly until configured.
- The local Semgrep rule only demonstrates ignored-failure detection; it is not a comprehensive SAST ruleset.
- The image wrapper scans vulnerabilities; additional image secret/license controls require deliberate integration.
- Kyverno's sample uses Audit mode and only illustrates ordinary-container non-root checking. It is neither deployed nor a complete hardening policy.
- KEV, EPSS, reachability, automatic database-age checks, exception approvals and cryptographic release verification are described but not automated here.
- Example report files are illustrative shapes, not vendor-schema conformance fixtures or actual scan evidence.
- Some other CI actions remain version-tag references. Resolve/review full commits and transitive dependencies before production adoption.
- Policies are reference organizational choices. The current wrappers implement a simpler blocking baseline; see the policy's implementation-status section.

## Validation

See [VALIDATION.md](VALIDATION.md) for actual checks and limitations. In particular, offline fake-tool tests demonstrate wrapper behavior, not the detection quality of real scanner releases. No active scan, signing operation, remote pipeline run or deployment was executed during this review.

## Next integration steps

1. Follow [quickstart](implementation/quickstart.md) to provision reviewed tools and verify their scopes.
2. Use a real application to validate source, package, image and test coverage.
3. Implement authenticated staging testing and the [release contract](implementation/release-contract.md).
4. Test missing, stale, malformed, untrusted and wrong-digest evidence before enabling production promotion.
