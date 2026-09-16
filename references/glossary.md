# Glossary

Read the [offline handbook](../docs/DEVSECOPS_HANDBOOK.md) for examples and the [detection matrix](../docs/DETECTION_AND_DATA.md) for tool-specific data sources. Product names such as Trivy, Gitleaks, Syft, Grype and Falco do not need invented acronym expansions.

- **SAST** — Static Application Security Testing.
- **SCA** — Software Composition Analysis.
- **DAST** — Dynamic Application Security Testing.
- **IaC** — Infrastructure as Code.
- **SBOM** — Software Bill of Materials.
- **SARIF** — Static Analysis Results Interchange Format.
- **CVE** — Common Vulnerabilities and Exposures identifier.
- **CVSS** — Common Vulnerability Scoring System.
- **Provenance** — verifiable information describing how an artifact was produced.
- **Artifact digest** — cryptographic content identifier such as SHA-256.
- **Security gate** — policy decision that determines whether a pipeline stage may continue.
- **Exception** — approved, bounded, time-limited deviation from a security policy.

## Delivery and infrastructure

| Term | Meaning and practical use |
| --- | --- |
| DevSecOps | Development, Security and Operations working within one delivery process |
| SDLC | Software Development Life Cycle: planning through operation and retirement |
| CI | Continuous Integration: frequently combine and verify changes |
| CD | Continuous Delivery (release-ready with approval) or Continuous Deployment (automatic deployment); specify which |
| PR / MR | Pull Request / Merge Request: a proposed reviewed source change |
| Runner / agent | Machine executing pipeline jobs; its isolation and permissions affect trust |
| Artifact | Build output, such as a package or container image |
| Registry | Store for images/packages; candidate storage does not equal production approval |
| SHA-256 | Secure Hash Algorithm with a 256-bit result, commonly used for content digests |
| Tag | Changeable label; retain the immutable content identity it resolves to |
| Image / container | Packaged filesystem and configuration / running instance of that image |
| Manifest / lockfile | Requested dependencies or configuration / exact recorded dependency resolution |
| Direct / transitive dependency | Package requested by the application / by another dependency |
| OS | Operating System, such as a Linux distribution in a base image |
| OCI | Open Container Initiative: container formats and distribution conventions |
| Kubernetes / K8s | Platform for orchestrating container workloads |
| Pod | Kubernetes unit grouping containers; target of the sample Kyverno policy |
| OPA | Open Policy Agent: policy evaluation engine used with Gatekeeper |
| Audit / Enforce | Record policy violations / reject violating requests |
| Canary / rollback | Limited initial release exposure / restoration of an earlier approved version |
| WSL | Windows Subsystem for Linux: one way to run Linux tools on Windows |
| PATH | Operating-system search path for executable commands |

## Vulnerability intelligence and detection

| Term | Meaning and practical use |
| --- | --- |
| CNA | CVE Numbering Authority: assigns identifiers within its scope |
| CWE | Common Weakness Enumeration: categories of software/hardware weakness |
| NVD | National Vulnerability Database: NIST vulnerability enrichment and applicability data |
| CPE | Common Platform Enumeration: product/platform identification used in applicability matching |
| purl | Package URL: structured package coordinate including ecosystem, name and version |
| OSV | Open Source Vulnerabilities: ecosystem-oriented advisory records and services |
| GHSA | GitHub Security Advisory identifier prefix; may alias a CVE |
| CISA | Cybersecurity and Infrastructure Security Agency; maintains KEV |
| KEV | Known Exploited Vulnerabilities: catalog based on evidence of exploitation |
| FIRST | Forum of Incident Response and Security Teams; maintains CVSS/EPSS resources |
| EPSS | Exploit Prediction Scoring System: probability of exploitation in the next 30 days; percentile is a different measure |
| VEX | Vulnerability Exploitability eXchange: structured applicability statements with justification |
| AST | Abstract Syntax Tree: parsed structural representation of source code |
| Taint analysis | Follow untrusted data toward a sensitive operation under an analyzer's models |
| Source / sink | Origin of input / sensitive operation that uses it |
| Sanitizer | Transformation modeled as making input safe for a particular context |
| Regex / entropy | Regular-expression text pattern / measure of apparent randomness used by some secret rules |
| Backport | Apply a fix to an older maintained release without adopting the newest upstream version |
| False positive / false negative | Reported issue does not apply / actual issue was missed |
| Unknown | Insufficient evidence; distinct from a passing result |
| ZAP | Zed Attack Proxy: web/API dynamic testing tool |
| Crawl / spider | Discover reachable pages and routes |
| Passive / active scan | Observe traffic without attack payloads / send targeted test inputs |
| Reachability | Whether execution can reach affected functionality; conclusions depend on the analysis model |

## Application security and reports

| Term | Meaning and practical use |
| --- | --- |
| API | Application Programming Interface: structured interface used by a client/program |
| Authentication / authorization | Establish identity / decide which action on which object is permitted |
| HTTP / HTTPS | Hypertext Transfer Protocol / HTTP over a secure transport |
| TLS | Transport Layer Security: protects transport and authenticates peers under its trust model |
| SQL | Structured Query Language; unsafe query construction can cause injection |
| XSS | Cross-Site Scripting: untrusted content executes in a browser context |
| CSRF | Cross-Site Request Forgery: unwanted action using a browser's authenticated context |
| CORS | Cross-Origin Resource Sharing: browser rules for cross-origin access |
| BOLA / IDOR | Broken Object Level Authorization / Insecure Direct Object Reference: related object-access failures |
| JSON | JavaScript Object Notation: structured report format |
| YAML | YAML Ain't Markup Language: configuration format used by pipelines and rules |
| TOML | Tom's Obvious Minimal Language: configuration format used by Gitleaks |
| XML | Extensible Markup Language: used in document formats and some suppression files |
| CLI | Command-Line Interface: how wrappers invoke tools |
| Exit status | Process completion code; interpret using the tool's documented meanings |
| SPDX | Software Package Data Exchange: standard for exchanging software information |
| CycloneDX | A bill-of-materials standard; inventory format used by this project |

## Trust, governance and operations

| Term | Meaning and practical use |
| --- | --- |
| OIDC | OpenID Connect: short-lived workload identity in supported CI/signing configurations |
| KMS / HSM | Key Management Service / Hardware Security Module: protected key management |
| Signature | Cryptographic assertion over content; verify expected signer and subject |
| Attestation | A statement about a subject, often signed; validate both signature and claims |
| Fulcio / Rekor | Sigstore certificate / transparency services for applicable signing flows |
| Fail closed | Stop progression when a mandatory condition cannot be established |
| Compensating control | Additional measure reducing accepted residual risk; requires evidence |
| SIEM | Security Information and Event Management: event collection and correlation |
| EDR | Endpoint Detection and Response: endpoint monitoring and response |
| RBAC / SSO | Role-Based Access Control / Single Sign-On |
| SLA | Service Level Agreement; here often an internal remediation deadline |
| MTTR | Mean Time to Remediate in this context; define start and end events |
| UTC | Coordinated Universal Time: consistent evidence and exception timestamps |
| NIST | National Institute of Standards and Technology |
| SSDF | Secure Software Development Framework: NIST secure development practices |
| OWASP | Open Worldwide Application Security Project |
| ASVS / SAMM | Application Security Verification Standard / Software Assurance Maturity Model |
| SLSA | Supply-chain Levels for Software Artifacts: supply-chain assurance requirements |
| CIS | Center for Internet Security: configuration benchmark guidance |

Vulnerability definitions are supported by [CVE](https://www.cve.org/about/Process), [NVD](https://nvd.nist.gov/general/FAQ-Sections/CVE-FAQs), [CWE](https://cwe.mitre.org/about/index.html) and [FIRST CVSS](https://www.first.org/cvss/v4.0/specification-document).
