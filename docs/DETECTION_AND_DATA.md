# Detection methods, comparison data and updates

Source review: **2026-09-16**. These are product mechanisms and documented schedules, not guarantees that your runner has fresh data. See the [handbook](DEVSECOPS_HANDBOOK.md) for worked examples and expanded terms.

## Comparison matrix

| Tool/control | What it finds | Working principle and knowledge source | Update model |
| --- | --- | --- | --- |
| Gitleaks | Likely secrets in files/history | Patterns, keywords, optional entropy; embedded/custom rules | Executable and rule changes; no CVE feed |
| Trivy vulnerability scanner | Known vulnerable packages | Identify packages; compare ecosystem/vendor versions with advisory applicability in aggregated Trivy DB | Provider scheduled every 6 hours; local refresh follows metadata, configuration and execution |
| Trivy Java DB | Java package identity | Separate index mapping artifact evidence to package coordinates | Daily provider build; not a second CVE database |
| Dependency-Check | Known vulnerable dependencies | Artifact evidence, candidate CPE identity, NVD applicability and other supported analyzers | Default NVD recheck interval 4 hours when update/scan runs |
| OSV | Known affected open-source packages | Ecosystem coordinates, affected versions/ranges/commits and aliases | Provider/importer and client dependent; no universal ingestion guarantee |
| Grype | Vulnerabilities in inventoried packages | Package matchers and Grype vulnerability database | Check database status and the pinned client's update settings |
| Semgrep | Configured insecure patterns/flows | Structured rules and supported taint analysis | Review local/registry rules and engine separately |
| CodeQL | Query-defined code weaknesses | Queries over an extracted code database | Re-extract changed code; maintain analyzer and query packs |
| SonarQube | Rule findings and failed quality conditions | Language analyzers, quality profiles and server quality gates | Analyzer/server/profile changes; wait for final gate evaluation |
| Trivy config / Checkov | Infrastructure policy violations | Structured attributes and supported graph relationships versus policy | Tool and policy bundle updates; not a shared CVE timer |
| Syft / SBOM generator | Component inventory | Catalog recognized package metadata | Recreate per artifact; maintain generator coverage |
| ZAP baseline | Issues visible in discovered traffic | Crawl and passive response rules | Installed tool/image and add-on updates |
| ZAP full scan | Rule-specific running-app issues | Discovery and active/passive tests | Installed tool/image and add-on updates |
| API access tests | Broken role/ownership behavior | Assert business requirements with known users and objects | Update with routes, roles and requirements |
| Cosign | Invalid/unexpected artifact trust | Cryptography, expected keys/identity/issuer and signed subject | Maintain trust roots, identities and policies; no CVE lookup |
| Kyverno / OPA Gatekeeper | Disallowed deployment requests | Evaluate organization policy against manifests/context | Review policy and engine changes |
| Falco | Suspicious runtime behavior | Event fields and conditions versus runtime rules | Rule, engine, driver and plugin updates |

Primary sources: [Gitleaks](https://github.com/gitleaks/gitleaks), [Trivy](https://trivy.dev/docs/latest/scanner/vulnerability/), [Dependency-Check](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/), [OSV](https://osv.dev/), [Grype](https://github.com/anchore/grype), [Semgrep](https://semgrep.dev/docs/writing-rules/glossary), [CodeQL](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli), [SonarQube](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview), [Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html), [Syft](https://github.com/anchore/syft), [ZAP](https://www.zaproxy.org/docs/desktop/addons/), [Cosign](https://docs.sigstore.dev/cosign/verifying/verify/), [Kyverno](https://kyverno.io/docs/policy-types/cluster-policy/validate/), [Falco](https://falco.org/docs/concepts/rules/).

## The four independent clocks

1. **Disclosure/enrichment:** vendors, maintainers or vulnerability programs publish and enrich information. These events need not happen together.
2. **Provider publication:** a scanner provider ingests sources and produces a consumable snapshot.
3. **Local refresh:** your client retrieves it, subject to cache policy, execution, credentials, mirrors and connectivity.
4. **Assessment:** your artifact is actually scanned with that snapshot and the relevant rules/tool version.

End-to-end detection delay includes all four stages. A six-hour provider schedule is not a six-hour detection guarantee. Corrected and rejected advisory records also need to propagate. [CVE process](https://www.cve.org/about/Process) and [NVD enrichment](https://nvd.nist.gov/general/FAQ-Sections/CVE-FAQs) explain their different roles.

## Verified timing and caveats

| Source | Documented behavior | What to inspect locally |
| --- | --- | --- |
| Trivy vulnerability DB | [Build workflow](https://raw.githubusercontent.com/aquasecurity/trivy-db/main/.github/workflows/cron.yml): every 6 hours. [Repository documentation](https://github.com/aquasecurity/trivy-db): default metadata interval 24 hours. | Actual `UpdatedAt`, `NextUpdate`, `DownloadedAt`, schema, tool version and refresh logs. Publication and local eligibility differ. |
| Trivy Java index | [Workflow](https://raw.githubusercontent.com/aquasecurity/trivy-java-db/main/.github/workflows/cron.yml): daily at 00:00 UTC. | Its identification data can have a different age from the vulnerability DB. |
| Dependency-Check | [CLI](https://dependency-check.github.io/DependencyCheck/dependency-check-cli/arguments.html): `--nvdValidForHours` defaults to 4; `--updateonly` refreshes without scanning. | Successful execution, cache age, API limits and any `--noupdate` setting. |
| EPSS | [FIRST](https://www.first.org/epss/): daily probabilities for exploitation in the next 30 days. | Score date; probability is different from percentile. |
| KEV | [CISA official mirror](https://github.com/cisagov/kev-data): maintained catalog of known exploitation. | Retrieved catalog/version and changes; absence is not proof of safety. |

Schedules can change. Match documentation to your pinned release and verify observed metadata. Rules-based tools and commercial platforms do not share a common refresh interval; verify the actual product's update mechanism.

## Matching example and disagreements

Illustration: `demo-parser` version `2.4.1` matches the correct ecosystem advisory range `>=2.0.0, <2.4.3`. This is a candidate vulnerability, not proof that the affected function is reachable in your application. Compare versions using ecosystem semantics, not lexical string ordering.

Origin and distribution revision matter. A vendor backport can fix an older release without adopting the newest upstream version. A wrong CPE, missing metadata, a different advisory snapshot, a different platform or a different exclusion can produce different results. Inspect that evidence before choosing which scanner to trust.

## Operational policy to implement

- Assign an owner and maximum age to each required intelligence/rule source.
- Record actual tool version, rule revision, source timestamps and refresh success per run.
- Use reviewed mirrors/caches and monitor their failures.
- Block or escalate releases with stale or missing data under an explicit policy.
- Rescan supported production artifacts or inventories on a schedule and after relevant advisories.
- Test unavailable-provider and stale-cache cases before relying on a gate.

Known-advisory matching cannot detect every undisclosed issue. Secret patterns do not prove validity; DAST only covers exercised behavior; an SBOM is inventory; a signature is a trust assertion. Automatic age enforcement, KEV/EPSS enrichment and exception verification remain application integration work in this repository. See the [release contract](implementation/release-contract.md).
