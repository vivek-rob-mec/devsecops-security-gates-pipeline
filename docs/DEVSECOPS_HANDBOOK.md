# DevSecOps handbook

Full offline companion to the presentation. Source review: 2026-09-16.

## How to use this handbook

Read foundations first, then pipeline flow and detection. Intermediate readers can focus on intelligence and project practice. Professionals should inspect the release contract and evidence controls. Slide notes contain the same explanations. The separate implementation guides describe commands and current limits.

## Contents

- [01. DevSecOps, explained from first principles](#lesson-01)
- [02. Choose a path through the material](#lesson-02)
- [03. The problem: one change can carry many risks](#lesson-03)
- [04. The delivery vocabulary](#lesson-04)
- [05. The security vocabulary](#lesson-05)
- [06. A vulnerability ID is not a risk score](#lesson-06)
- [07. Prioritize with evidence and context](#lesson-07)
- [08. The complete flow in four phases](#lesson-08)
- [09. Phase 1: define what must be protected](#lesson-09)
- [10. Phase 2: verify the proposed change](#lesson-10)
- [11. Phase 3: identify and verify the artifact](#lesson-11)
- [12. Phase 4: test, release and observe](#lesson-12)
- [13. Five working principles behind the tools](#lesson-13)
- [14. Secret scanning: Gitleaks](#lesson-14)
- [15. SCA: identify, then match](#lesson-15)
- [16. Worked example: an affected version range](#lesson-16)
- [17. Trivy: source and image vulnerabilities](#lesson-17)
- [18. Dependency-Check, OSV and Grype](#lesson-18)
- [19. SAST: follow data through code](#lesson-19)
- [20. Semgrep: executable rules over code](#lesson-20)
- [21. CodeQL and SonarQube use different models](#lesson-21)
- [22. IaC scanning: compare desired state to policy](#lesson-22)
- [23. Containers: inspect what actually ships](#lesson-23)
- [24. SBOM: inventory for today and tomorrow](#lesson-24)
- [25. Signing and provenance establish origin](#lesson-25)
- [26. DAST: inspect the running application](#lesson-26)
- [27. ZAP: baseline is not a full active test](#lesson-27)
- [28. API security needs business-aware assertions](#lesson-28)
- [29. Admission control: prevent a bad deployment](#lesson-29)
- [30. Runtime detection: notice suspicious behavior](#lesson-30)
- [31. How a disclosure becomes a scanner finding](#lesson-31)
- [32. When Trivy updates its data](#lesson-32)
- [33. Refresh intervals across other tools](#lesson-33)
- [34. Freshness is an operational control](#lesson-34)
- [35. How to read a vulnerability report](#lesson-35)
- [36. False positives, false negatives and unknowns](#lesson-36)
- [37. Turn scanner output into an explicit gate](#lesson-37)
- [38. The release decision must fail closed](#lesson-38)
- [39. Exceptions need a lifecycle](#lesson-39)
- [40. What belongs in the release evidence package](#lesson-40)
- [41. What this repository actually provides](#lesson-41)
- [42. Local use: prerequisites and first checks](#lesson-42)
- [43. A stack changes inputs, not the control goals](#lesson-43)
- [44. CI templates need explicit setup](#lesson-44)
- [45. Corrections made during this review](#lesson-45)
- [46. Troubleshooting by symptom](#lesson-46)
- [47. After release: a new CVE changes the answer](#lesson-47)
- [48. Standards guide outcomes and assurance](#lesson-48)
- [49. Adopt in small, verifiable increments](#lesson-49)
- [50. Check your understanding](#lesson-50)
- [51. What a defensible release can explain](#lesson-51)
- [52. Sources and maintenance](#lesson-52)
- [53. Sources and maintenance](#lesson-53)
- [54. Sources and maintenance](#lesson-54)
- [55. Sources and maintenance](#lesson-55)
- [56. Sources and maintenance](#lesson-56)
- [57. Sources and maintenance](#lesson-57)

<a id="lesson-01"></a>

## 01. DevSecOps, explained from first principles

*START — Understand the flow. Understand the findings. Make a defensible release decision.*

**FOUNDATIONS.** What each stage does, why it exists, and the terms you need.

**DETECTION.** Inputs, working principles, comparison data, updates and blind spots.

**IMPLEMENTATION.** Repository commands, real gate behavior, evidence and release integration.

DevSecOps brings development, security and operations into one delivery process. This course uses a small online shop as a running example. The project is a reference architecture with scanner wrappers and integration templates; it is not a deployed application. Slides introduce the ideas, these notes explain them, and the handbook preserves the explanations for offline study. The existing filename is retained for compatibility; no universal industry standard mandates this exact pipeline.

**Key point:** Three learning paths, one consistent explanation.

<a id="lesson-02"></a>

## 02. Choose a path through the material

*START — Read the main course in sequence; return to technical sections when implementing.*

**BEGINNER.** Start with foundations and the four pipeline phases. Read every term and worked example.

**INTERMEDIATE.** Focus on detection, database freshness, command behavior and troubleshooting.

**PROFESSIONAL.** Review trust boundaries, evidence integrity, exceptions and the release contract.

A beginner should be able to explain why a dependency scan cannot detect every bug in application code. An intermediate engineer should be able to interpret a finding and fix its cause. A professional should be able to show that the reports describe the exact artifact being released and that missing evidence blocks promotion. Use the companion handbook for the full notes and the glossary for terms. Sources are linked for verification and future maintenance, not required to follow the course.

**Key point:** A scanner finding, a policy decision and a production release are different events.

<a id="lesson-03"></a>

## 03. The problem: one change can carry many risks

*01 FOUNDATIONS — Example: a developer changes checkout in an online shop.*

**SOURCE.** A token enters a file. A database query uses unsafe input. A new package brings old dependencies.

**DELIVERABLE.** The container includes an outdated system library. Its deployment requests excessive privilege.

**RUNNING SERVICE.** One customer can access another customer's order. A compromised process starts a shell.

Source is the code and configuration people edit. A deliverable, also called an artifact, is the package or container produced by the build. A running service includes that artifact plus environment, accounts, network access and data. These are different inspection targets. A secret scanner, dependency scanner, code analyzer, configuration checker and behavior test each answer a different question. Business authorization needs explicit tests that understand which customer owns which order.

**Key point:** Choose controls according to the risk and the object being inspected.

<a id="lesson-04"></a>

## 04. The delivery vocabulary

*01 FOUNDATIONS — Expand the terms before reading a pipeline diagram.*

**CI / CD.** Continuous Integration: merge and verify changes frequently. Continuous Delivery: keep releases ready for approval.

**PR / BUILD.** Pull Request: propose a reviewed change. Build: turn source and dependencies into a distributable artifact.

**STAGE / RELEASE.** Staging: a controlled test environment. Release: approve a specific artifact for use.

CD can also mean Continuous Deployment, where passing changes are automatically deployed. State which meaning your team uses. A runner or agent is the machine that executes pipeline jobs. A registry stores container images; an artifact repository can also store packages and other build products. A commit identifies a source snapshot. A digest is a cryptographic identifier of content. Staging should resemble production closely enough for meaningful testing, while using controlled test accounts and data.

**Key point:** This course uses CD to mean Continuous Delivery with an explicit release decision.

<a id="lesson-05"></a>

## 05. The security vocabulary

*01 FOUNDATIONS — Each acronym names a different activity.*

**SCA / SAST.** Software Composition Analysis: inspect dependencies. Static Application Security Testing: inspect code without running the app.

**IaC / DAST.** Infrastructure as Code: machine-readable infrastructure. Dynamic Application Security Testing: inspect a running service.

**SBOM / GATE.** Software Bill of Materials: component inventory. Security gate: a rule deciding whether work may continue.

Static means the application is not exercised as a running target. Dynamic means tests send requests to a running target and observe results. Composition means the third-party pieces the software contains. Infrastructure as Code can describe a virtual network, storage permissions, a container build or a Kubernetes workload. An SBOM records components; it does not by itself say that all components are safe. A gate can reject findings, incomplete scans or missing evidence. JSON is a structured data format; SARIF is Static Analysis Results Interchange Format.

**Key point:** Tool names are products; SCA, SAST and DAST are categories of work.

<a id="lesson-06"></a>

## 06. A vulnerability ID is not a risk score

*01 FOUNDATIONS — CVE, CWE and CVSS answer different questions.*

**CVE.** Common Vulnerabilities and Exposures: an identifier for a disclosed vulnerability. An advisory may also have a GHSA or OSV ID.

**CWE.** Common Weakness Enumeration: a class of mistake, such as improper input handling.

**CVSS.** Common Vulnerability Scoring System: a severity framework. Keep its version, score and vector together.

A CVE identifies a specific vulnerability; its year is part of the identifier and is not a guaranteed discovery date. A CWE describes a weakness category and can describe problems that have no CVE. CVSS describes technical severity, rather than the probability of an attack against your service. A vector records the metric choices behind a score. A scanner alert may identify a custom rule, a weakness or an advisory without any CVE. The informal abbreviation CV is ambiguous; use CVE for identifiers and CVSS for severity.

**Key point:** No CVE does not mean no security issue.

Sources: [CVE identifier lifecycle](https://www.cve.org/about/Process), [MITRE Common Weakness Enumeration](https://cwe.mitre.org/about/index.html), [FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document).

<a id="lesson-07"></a>

## 07. Prioritize with evidence and context

*01 FOUNDATIONS — Severity, exploitation and business impact are separate inputs.*

**CVSS.** How severe can exploitation be? Common bands: low 0.1–3.9, medium 4.0–6.9, high 7.0–8.9, critical 9.0–10.

**EPSS / KEV.** Exploit Prediction Scoring System estimates exploitation probability. Known Exploited Vulnerabilities records observed exploitation.

**YOUR SERVICE.** Is the component shipped, reachable and exposed? What data or operations can an attacker affect?

EPSS provides daily estimates for the probability of exploitation in the wild over the next 30 days. A percentile describes relative rank, not probability. CISA maintains KEV based on evidence of exploitation; absence from KEV is not proof of safety. Reachability asks whether execution can reach vulnerable functionality, subject to the analyzer's limits. Example policy: investigate a high-severity exposed component in KEV immediately; do not automatically dismiss another vulnerability because its EPSS is low. The repository wrappers implement severity thresholds, not automated EPSS, KEV or reachability enrichment.

**Key point:** A low prediction is not an exemption; a score needs application context.

Sources: [FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document), [FIRST Exploit Prediction Scoring System](https://www.first.org/epss/), [CISA official KEV data mirror](https://github.com/cisagov/kev-data).

<a id="lesson-08"></a>

## 08. The complete flow in four phases

*02 PIPELINE FLOW — Each phase produces evidence needed by the next.*

**1  PREPARE.** Requirements → threat model → reviewed source

**2  VERIFY.** Secrets + dependencies + code + configuration + tests

**3  PACKAGE.** Build → candidate registry → image scan + inventory + trust

**4  RELEASE.** Staging → behavior tests → gate → production → feedback

After checkout, independent scans can run in parallel. Language-specific analysis may need dependency resolution or a compilation step first. Build the release artifact once. Container signing commonly acts on an image already pushed to a restricted candidate registry, because its digest must be known and signatures are stored alongside it. Candidate publication is not production approval. Later promotion changes availability or deployment references while preserving the approved digest. Runtime findings and new advisories start a new remediation cycle.

**Key point:** The diagram expresses dependencies; it does not require every scan to run serially.

<a id="lesson-09"></a>

## 09. Phase 1: define what must be protected

*02 PIPELINE FLOW — Owner: product team with security and platform engineering.*

**INPUT.** Data, users, trust boundaries, critical business actions and architecture.

**WORK.** Write abuse cases. Define access rules, recovery needs and acceptance tests.

**OUTPUT / GATE.** Reviewed requirements, a threat model and named owners. Unresolved critical design risks need a decision.

A trust boundary is where data or control crosses between different levels of trust, such as a browser sending input to an application server. For the shop, an abuse case is customer A requesting customer B's order. Turn the threat into a requirement: every order lookup must authorize the authenticated customer against the order owner. Then write a test with two users. Threat modeling uses structured reasoning and architecture knowledge; it does not download a CVE database. See threat-model/template.md for a starting worksheet.

**Key point:** Requirements become tests; a vague security goal cannot be verified.

<a id="lesson-10"></a>

## 10. Phase 2: verify the proposed change

*02 PIPELINE FLOW — Owner: developers; security engineers maintain rules and triage support.*

**CHECKOUT.** Obtain the intended commit. Protect reviews, pipeline changes and runner credentials.

**ANALYZE.** Run secret, dependency, code and configuration checks. Run unit, integration and security tests.

**DECIDE.** Fail on configured violations or tool errors. Save reports and correct the change before retrying.

A lockfile records resolved dependency versions; a manifest may only express broad constraints. Resolve dependencies in an isolated runner because installation and build scripts can execute third-party code. A unit test checks a small behavior; integration tests check cooperating components. Neither guarantees security unless the intended security behavior is asserted. A merge gate belongs on a protected branch and must be required by the hosting platform. Merely adding a YAML file under pipelines/ does not activate a GitHub workflow.

**Key point:** A report file existing is not proof that the scanner completed or found nothing.

<a id="lesson-11"></a>

## 11. Phase 3: identify and verify the artifact

*02 PIPELINE FLOW — Owner: build and platform engineering.*

**BUILD ONCE.** Produce one candidate image from the reviewed source and controlled dependencies.

**INSPECT.** Scan the image by digest. Generate its component inventory. Record build provenance.

**ESTABLISH TRUST.** Sign the digest and relevant attestations. Store evidence in a restricted system.

An image tag such as latest is a changeable name. A reference containing @sha256: followed by 64 hexadecimal characters identifies specific content. Different builds of the same source may differ because dependencies, base images or timestamps changed. Provenance is a statement describing a build's inputs and builder. Signing provides an integrity and identity assertion; verifying the signature against an approved identity is a separate step. A signed artifact can still contain vulnerabilities. Multi-platform images require care: test and scan every deployable platform digest or define an explicit platform policy.

**Key point:** Source scans and image scans inspect different inputs; retain both sets of evidence.

<a id="lesson-12"></a>

## 12. Phase 4: test, release and observe

*02 PIPELINE FLOW — Owner: application team and release operations.*

**STAGING.** Deploy the candidate digest. Check health, authenticated behavior and API access rules.

**RELEASE GATE.** Verify identity, complete reports, thresholds, valid exceptions and approval.

**PRODUCTION.** Deploy the approved digest. Observe health and security; roll back or patch when needed.

Application Programming Interface, or API, means the structured interface used by another program or client. DAST and API tests should exercise the same candidate that will be released. If an artifact changes after scanning, repeat the affected checks. A production rollout can initially serve a small share of traffic, called a canary. Rollback restores an earlier approved version; database changes may require a separate recovery plan. New vulnerability information requires rescanning retained artifacts or SBOMs even when no source code changes.

**Key point:** A passing release gate is a time-bounded decision about one artifact.

<a id="lesson-13"></a>

## 13. Five working principles behind the tools

*03 DETECTION — Ask what is being compared before asking which database is used.*

**IDENTITY + ADVISORY.** SCA and image scanners identify packages and compare versions with affected ranges.

**STRUCTURE + RULE.** Secret, code and configuration tools match patterns, data flows or policy conditions.

**OBSERVATION + TRUST.** DAST inspects responses; runtime tools inspect events; signing tools verify cryptographic evidence.

Not every security product compares against the National Vulnerability Database, abbreviated NVD. A code rule may recognize unsafe SQL construction without knowing a CVE. An admission rule may reject privileged containers without any vulnerability feed. A signature verifier compares cryptographic evidence with a trust policy. The relevant freshness question may be the advisory snapshot, the rule revision, the analyzer version or the certificate trust root. Record the specific data source used by each control.

**Key point:** “Database” can mean advisories, a code model, an inventory or a rule bundle.

<a id="lesson-14"></a>

## 14. Secret scanning: Gitleaks

*03 DETECTION — Find credential-shaped material before it spreads.*

**INPUT / FINDINGS.** Files and Git history. Finds likely tokens, keys and other secrets with file and rule context.

**HOW IT WORKS.** Rules use patterns, keywords and optional entropy checks. Entropy measures apparent randomness.

**DATA / LIMITS.** Embedded and custom rules; no CVE feed. A pattern match does not establish that a credential is active.

Gitleaks combines configured detection rules with exclusions. Updating the executable refreshes embedded rules; a custom rules file changes through a reviewed configuration update. This project explicitly loads configs/gitleaks/.gitleaks.toml, extending the default rules. The wrapper checks the worktree and also reachable Git history when Git metadata exists. A downloaded ZIP contains no history. It redacts report secrets. A match requires investigation; any real exposed credential needs revocation or rotation, even if the code is deleted. Avoid broad allowlists that hide future exposures.

**Key point:** Rotate a real leaked credential; deleting the string does not invalidate it.

Sources: [Gitleaks detection and configuration](https://github.com/gitleaks/gitleaks).

<a id="lesson-15"></a>

## 15. SCA: identify, then match

*03 DETECTION — Software Composition Analysis starts with an accurate inventory.*

**IDENTIFY.** Read supported lockfiles, package metadata or binaries. Resolve name, ecosystem, version and origin.

**COMPARE.** Select the relevant advisory source. Evaluate affected version ranges using ecosystem-specific semantics.

**REPORT.** Return component, advisory ID, severity, installed version, fixed version and evidence path.

A direct dependency is one the application requests; a transitive dependency is requested by another dependency. Package names alone are insufficient because names can overlap between ecosystems. Package URL, written purl, is a standardized component coordinate; Common Platform Enumeration, or CPE, identifies product/platform attributes and is common in NVD applicability data. Missing metadata, unsupported formats, repackaged libraries and unresolved versions can prevent correct identification. SCA matches known advisory information; it does not prove that an arbitrary unknown package is trustworthy.

**Key point:** A missed component cannot receive a reliable vulnerability verdict.

<a id="lesson-16"></a>

## 16. Worked example: an affected version range

*03 DETECTION — Illustrative package and advisory; these are not real vulnerability records.*

**INVENTORY.** The lockfile resolves demo-parser 2.4.1. A transitive dependency brought it into the shop.

**ADVISORY.** The relevant ecosystem advisory says versions from 2.0.0 up to, but excluding, 2.4.3 are affected.

**DECISION.** 2.4.1 is inside the range. Upgrade resolution to a tested fixed release, rebuild and rescan.

Comparison is not a text search for the CVE string inside source files. It is an identity lookup followed by version-range evaluation. Lexical string comparison is wrong: a version containing 10 is not necessarily older than a version containing 9. Debian and RPM package revisions, epochs and distribution releases have their own ordering rules. A backport applies a security fix to an older maintained release without adopting the newest upstream version. Use the advisory for the actual package origin. A reported fixed version is a candidate remediation that still needs compatibility testing.

**Key point:** Name + ecosystem + version + origin determine which advisory applies.

<a id="lesson-17"></a>

## 17. Trivy: source and image vulnerabilities

*03 DETECTION — One product, several scanners; enable the intended scope explicitly.*

**INPUT.** Filesystem manifests or image package metadata. An image adds operating-system packages and packaged application libraries.

**COMPARISON DATA.** Trivy DB aggregates vendor and ecosystem advisories. OS-managed packages use the corresponding distribution source.

**OUTPUT / LIMIT.** Known vulnerable components. This project enables vulnerability scanning; licenses and image secrets need separate controls.

Trivy selects advisory sources according to package type and origin. Vendor advisories help account for distribution backports. The JSON report can identify the severity source, so two scanners can legitimately show different ratings. The source wrapper uses trivy fs; the image wrapper uses trivy image with an immutable reference. Config scanning is a separate operation. The current wrappers block HIGH and CRITICAL findings, including those without fixes. They do not calculate application reachability. The local Trivy configuration is now explicitly passed rather than merely stored in the repository.

**Key point:** Check which scanner ran and which packages it recognized.

Sources: [Trivy: vulnerability matching](https://trivy.dev/docs/latest/scanner/vulnerability/).

<a id="lesson-18"></a>

## 18. Dependency-Check, OSV and Grype

*03 DETECTION — Alternative matching systems share a goal but differ in identity and data.*

**DEPENDENCY-CHECK.** Analyzers collect package evidence, identify CPE candidates and consult NVD applicability data.

**OSV.** Open Source Vulnerabilities uses ecosystem-oriented records, package versions and affected ranges or commits.

**GRYPE.** Matches inventoried packages against its vulnerability database; can scan an image, filesystem or supported SBOM.

Dependency-Check is common in Java projects but has multiple analyzers. An ambiguous product name can produce an incorrect CPE candidate; inspect evidence and scope any suppression to the proven mismatch. OSV aligns vulnerability records to open-source ecosystems, and advisories can have aliases such as CVE or GHSA identifiers. Grype uses its own provider aggregation and matching behavior. These are alternatives or targeted secondary checks, not mandatory duplicates. The repository only directly wraps Trivy. A product being mentioned in a tool matrix does not mean that it is installed or integrated.

**Key point:** Compare evidence and coverage when tools disagree; do not just count alerts.

Sources: [Dependency-Check detection model](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/), [Open Source Vulnerabilities](https://osv.dev/), [Grype vulnerability scanning](https://github.com/anchore/grype).

<a id="lesson-19"></a>

## 19. SAST: follow data through code

*03 DETECTION — Static Application Security Testing looks for unsafe program behavior.*

**SOURCE.** Untrusted data enters through a request parameter, file, message or other boundary.

**FLOW.** Analysis follows values through assignments and calls. Models describe sanitizers and safe transformations.

**SINK.** A sensitive operation uses the value: a database query, command execution or rendered page.

A source is where untrusted input originates; a sink is where misuse can cause harm. Taint analysis tracks whether that input can reach the sink under the model used by the analyzer. An Abstract Syntax Tree, or AST, represents the structure of parsed code. Structural matching can recognize code patterns despite formatting changes. More advanced analysis may inspect control flow and relationships across functions or files. Framework support, reflection, generated code and missing build context can limit coverage. These techniques identify weakness patterns, not just known library CVEs.

**Key point:** Inspect the source-to-sink evidence before deciding whether the finding is real.

<a id="lesson-20"></a>

## 20. Semgrep: executable rules over code

*03 DETECTION — Rules define what the engine should recognize.*

**DETECTION.** Structural patterns and taint rules describe unsafe code. Analysis depth depends on engine, language and edition.

**DATA / UPDATES.** Local YAML rules or registry rulesets. Pin and review rules; upgrade the engine separately.

**PROJECT BEHAVIOR.** The local demonstration rule flags ignored pipeline failures. --error makes findings fail; --strict handles scan errors more strictly.

The project's Semgrep rule is deliberately small and is not a full application-security ruleset. It looks for shell failure suppression in scripts and pipeline templates. The wrapper now explicitly selects it, rather than fetching an automatically chosen ruleset. Set SEMGREP_CONFIG to an approved local rules directory when integrating an application. Community and commercial analysis capabilities differ; do not assume cross-file coverage from the product name alone. Semgrep scan ordinarily reports findings without necessarily returning a failing status unless error behavior is requested.

**Key point:** A successful process can contain findings unless failure behavior is configured.

Sources: [Semgrep rule and analysis concepts](https://semgrep.dev/docs/writing-rules/glossary), [Semgrep command and exit semantics](https://docs.semgrep.dev/cli-reference).

<a id="lesson-21"></a>

## 21. CodeQL and SonarQube use different models

*03 DETECTION — A database can represent your code rather than public vulnerabilities.*

**CODEQL.** Extracts a database representing source. Security queries analyze the code model and may return data-flow paths.

**SONARQUBE.** Analyzers apply language rules. Quality profiles choose active rules; quality gates evaluate configured metrics.

**INTEGRATION.** Match analyzer support to the language and build. Retrieve the final gate result; scanner upload success is insufficient.

CodeQL creates a database from the target code and runs query suites against it; this database is not an NVD copy. Query-pack and analyzer updates affect coverage. SonarQube receives analyzer results and applies server-side configuration; a security hotspot may need human review rather than representing a confirmed vulnerability. Plugin, server and edition capabilities matter. Both tools need a functioning analysis integration and an enforced result in CI. This repository has guidance and an example Sonar configuration, but no complete server or CodeQL setup.

**Key point:** Confirm analysis completion and the evaluated policy, not just report upload.

Sources: [CodeQL database and query model](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli), [SonarQube analysis overview](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview).

<a id="lesson-22"></a>

## 22. IaC scanning: compare desired state to policy

*03 DETECTION — Infrastructure as Code can create exposure before the application starts.*

**FINDS.** Examples include public storage, broad network access, privileged workloads and missing encryption settings.

**HOW.** Parse configuration and evaluate resource attributes or relationships against checks and organizational policy.

**DATA / LIMITS.** Rules and policy bundles, not primarily a CVE database. Templates may not equal deployed state.

Trivy config and Checkov inspect supported infrastructure formats. Checkov includes attribute and graph-based checks; graph analysis reasons about connected resources such as a service linked to a public network. A rule must consider explicit and inherited configuration, not just whether one string appears. Update the tool and policy bundles with review. Variables, dynamic templates and unmanaged changes can reduce accuracy, so inspect rendered manifests or plans when supported and audit the deployed environment separately. The current Trivy wrapper blocks HIGH and CRITICAL configuration findings.

**Key point:** Configuration scanning predicts risk in declared infrastructure; verify deployed reality too.

Sources: [Checkov configuration and graph checks](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html).

<a id="lesson-23"></a>

## 23. Containers: inspect what actually ships

*03 DETECTION — An application can be clean while its base image is vulnerable.*

**LAYERS.** A container image packages application files, libraries and often operating-system packages.

**SCAN TARGET.** Inspect the release digest for the intended platform. Include base image and application package metadata.

**HARDENING.** Use minimal trusted bases, non-root execution, limited permissions and controlled updates.

An image is a packaged filesystem and configuration. A container is a running instance of an image. Removing a file in a later layer does not necessarily remove its content from earlier layers, so never bake credentials into builds. Vulnerability, secret and configuration checks are distinct capabilities. This repository's image wrapper explicitly scans vulnerabilities and requires a digest; it does not claim to scan every image secret or enforce runtime hardening. New base-image vulnerabilities require rebuilding from an updated base and then rescanning the newly produced digest.

**Key point:** An image scan is not a runtime monitor or a complete hardening review.

<a id="lesson-24"></a>

## 24. SBOM: inventory for today and tomorrow

*03 DETECTION — Software Bill of Materials records component identity and relationships.*

**GENERATE.** Syft or Trivy examines the artifact and emits a structured inventory.

**EXCHANGE.** CycloneDX and SPDX are interoperable formats. SPDX expands to Software Package Data Exchange.

**USE.** Link the inventory to the artifact digest. Recheck it when new vulnerability information appears.

An SBOM is analogous to an ingredient list: it supports later questions about whether an affected component is present. It can contain names, versions, identifiers, relationships, hashes and licenses, depending on format and producer. Syft is an inventory generator, rather than a CVE matching engine. A generator does not need a vulnerability database to list packages. The quality of later vulnerability matching depends on inventory completeness. This project can generate CycloneDX JSON for a digest, but does not validate a full release evidence package or perform automatic inventory ingestion.

**Key point:** An inventory enables vulnerability analysis; it is not a clean bill of health.

Sources: [Syft software inventory](https://github.com/anchore/syft).

<a id="lesson-25"></a>

## 25. Signing and provenance establish origin

*03 DETECTION — Verify both cryptographic integrity and the expected identity.*

**DIGEST / SIGNATURE.** The digest identifies content. A signature binds a signing key or identity to that content.

**PROVENANCE.** An attestation describes the builder and inputs. Its trust depends on the builder and how evidence was produced.

**VERIFY.** Check the expected signer, identity issuer, artifact digest and required claims before deployment.

Cosign supports verification using public keys or certificate identity and issuer constraints. OpenID Connect, or OIDC, can provide a short-lived workload identity used in keyless signing flows. Fulcio and Rekor are Sigstore services involved in certificates and transparency evidence. A transparency log records evidence; it does not prove the software has no vulnerabilities. Never accept any valid signer when only one build workflow is trusted. The project signing wrapper signs an explicit digest but leaves key or workload-identity setup to the organization; production verification remains an integration requirement.

**Key point:** Signed does not mean safe; verified expected origin is one release condition.

Sources: [Cosign signature verification](https://docs.sigstore.dev/cosign/verifying/verify/), [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/).

<a id="lesson-26"></a>

## 26. DAST: inspect the running application

*03 DETECTION — Dynamic Application Security Testing observes requests and responses.*

**DISCOVER.** Find routes through crawling, recorded traffic or an API definition. Establish the intended authenticated session.

**EXERCISE.** Observe traffic or send targeted test inputs. Evaluate responses, behavior and rule-specific evidence.

**REPORT.** Record endpoint, parameter, evidence, rule, confidence and coverage. Reproduce important findings safely.

Crawling means visiting reachable links to discover pages. A traditional spider may miss JavaScript routes; browser-assisted discovery may improve coverage. Passive scanning observes messages without attack payloads. Active scanning sends test inputs and can change state or consume resources. The comparison knowledge is usually scanner rules and expected behavior, not just a downloaded list of CVEs. A running target can also be fingerprinted for known components, but that does not replace dependency analysis. Authentication and route coverage are essential to interpret a clean result.

**Key point:** A clean scan of a login page says little about the authenticated application.

<a id="lesson-27"></a>

## 27. ZAP: baseline is not a full active test

*03 DETECTION — ZAP rules arrive through the installed tool and add-ons.*

**BASELINE.** A short crawl followed by passive checks. Useful for headers and observable response issues.

**FULL SCAN.** Discovery plus active testing. Use controlled scope, test data, rate limits and an authorized environment.

**EXIT STATUS.** Packaged scans distinguish FAIL, WARN and execution errors. Choose an explicit handling policy for each.

The baseline script generally exits 0 on success, 1 for configured FAIL alerts, 2 for WARN alerts without FAILs, and 3 for other failure. The full-scan script adds active scanning. Do not silence these distinctions with shell failure suppression. Keep the ZAP image or version and add-on list with the report. Updating add-ons changes the installed rules; there is no universal ZAP CVE refresh interval. The current project DAST wrapper is an integration stub: it now exits with an error instead of pretending that a scan occurred.

**Key point:** State the scan mode, authenticated coverage and outcome in every DAST report.

Sources: [ZAP baseline scope and exit codes](https://www.zaproxy.org/docs/docker/baseline-scan/), [ZAP full scan](https://www.zaproxy.org/docs/docker/full-scan/), [ZAP add-ons and rules](https://www.zaproxy.org/docs/desktop/addons/).

<a id="lesson-28"></a>

## 28. API security needs business-aware assertions

*03 DETECTION — Example: order access must remain within a customer account.*

**TEST IDENTITY.** Create customer A, customer B and an administrative role using isolated test accounts.

**TEST OWNERSHIP.** Request A’s order as B. Expect access denial and no order data, including through alternate routes.

**TEST BOUNDARIES.** Check role changes, pagination, bulk endpoints, expired sessions and rate-sensitive operations.

Authentication answers who the requester is. Authorization answers whether that requester may perform this action on this object. Broken Object Level Authorization, or BOLA, and Insecure Direct Object Reference, or IDOR, describe related object-access failures. A generic scanner usually cannot infer the intended customer ownership model. API schema testing can find malformed input handling, while deliberate role and ownership tests establish business rules. Save expected and observed results, but redact tokens and customer information. Run these tests against the same candidate digest used for other staging checks.

**Key point:** Two authenticated users are often more useful than one anonymous scan.

<a id="lesson-29"></a>

## 29. Admission control: prevent a bad deployment

*03 DETECTION — Kubernetes admission evaluates requests before the cluster accepts them.*

**INPUT.** A workload manifest or deployment request, plus relevant policy and context.

**COMPARE.** Kyverno or Open Policy Agent rules test settings and, when configured, image trust requirements.

**MODE MATTERS.** Audit records violations. Enforce rejects violating requests. The project’s sample is Audit mode.

Kubernetes is a platform for running containerized workloads. A Pod groups containers scheduled together. Admission policy can require non-root execution, restrict registries or verify images. Open Policy Agent is commonly shortened to OPA; Gatekeeper integrates OPA policies with Kubernetes. Policy definitions and engine releases are the update sources, rather than a CVE feed. The sample require-non-root rule only illustrates ordinary-container checks and uses Audit. Extend and test it for inherited settings, init containers and ephemeral containers before enforcing a real cluster policy.

**Key point:** A policy file in the repository does nothing until it is installed and enforced.

Sources: [Kyverno admission validation](https://kyverno.io/docs/policy-types/cluster-policy/validate/).

<a id="lesson-30"></a>

## 30. Runtime detection: notice suspicious behavior

*03 DETECTION — Falco inspects events after software starts running.*

**OBSERVE.** System activity and supported event sources produce process, file and other runtime context.

**MATCH.** Rules compare event fields and conditions with behaviors worth investigating.

**RESPOND.** Route alerts to an owner. Investigate, contain when justified, preserve evidence and correct the cause.

Falco rules define event conditions and alert messages. Depending on deployment, a driver or plugin supplies the events. This is behavior detection, not an inventory-to-CVE comparison. Rules, exceptions and engine support need maintenance. Starting a shell inside an application container may be suspicious but can also be an authorized operational action, so context matters. SIEM means Security Information and Event Management, a system for collecting and correlating events. EDR means Endpoint Detection and Response. The repository documents these controls but does not install a runtime sensor or automate incident response.

**Key point:** Detection requires an operational response path; an unowned alert is incomplete.

Sources: [Falco runtime rules](https://falco.org/docs/concepts/rules/).

<a id="lesson-31"></a>

## 31. How a disclosure becomes a scanner finding

*04 INTELLIGENCE — There are several independent delays between discovery and detection.*

**DISCLOSE.** Researchers and vendors investigate. An advisory and identifier become public.

**ENRICH.** Maintainers and databases add package ranges, severity, references and applicability.

**DISTRIBUTE.** A scanner provider builds or exposes updated intelligence. Your runner refreshes its local data.

**MATCH.** The next scan inventories your artifact and evaluates it against that snapshot.

A CVE Numbering Authority, or CNA, assigns identifiers within its scope. NVD adds vulnerability information and applicability data, but enrichment can lag publication. Vendor and ecosystem advisories may have usable information earlier. No scanner can guarantee detection of every newly discovered issue immediately. A database is a snapshot rather than a live assertion about the whole world. Track source publication, provider build, local download and actual scan times separately. Corrected or rejected records also need to propagate.

**Key point:** Discovery time, public disclosure, database refresh and your next scan are different clocks.

Sources: [CVE identifier lifecycle](https://www.cve.org/about/Process), [NVD vulnerability enrichment](https://nvd.nist.gov/general/FAQ-Sections/CVE-FAQs).

<a id="lesson-32"></a>

## 32. When Trivy updates its data

*04 INTELLIGENCE — Verified upstream schedules; actual local freshness depends on metadata and execution.*

**VULNERABILITY DB.** Upstream publication is scheduled every 6 hours. Successful publication can be delayed by outages.

**JAVA INDEX.** A separate package-identification index has a daily publication schedule. It is not a second CVE feed.

**LOCAL RUNNER.** Refresh depends on cache metadata, execution and flags. Record UpdatedAt, NextUpdate and DownloadedAt where available.

The Trivy DB repository documents a six-hour build schedule and a default metadata update interval of 24 hours; these are not the same promise. Its workflow confirms the publication schedule. Inspect your actual metadata and tool version to establish local behavior. The Java database maps Java artifacts to package coordinates; vulnerability decisions still need vulnerability intelligence. A Java index may be used when package identity is not already available from metadata. Do not write “all Trivy databases update every six hours” in an operational policy.

**Key point:** Measure the database actually used, not just the provider’s nominal schedule.

Sources: [Trivy database build and metadata](https://github.com/aquasecurity/trivy-db), [Trivy database publication schedule](https://raw.githubusercontent.com/aquasecurity/trivy-db/main/.github/workflows/cron.yml), [Trivy Java index](https://github.com/aquasecurity/trivy-java-db), [Java index publication schedule](https://raw.githubusercontent.com/aquasecurity/trivy-java-db/main/.github/workflows/cron.yml).

<a id="lesson-33"></a>

## 33. Refresh intervals across other tools

*04 INTELLIGENCE — Some tools refresh data; others need a new rule pack or executable.*

**DEPENDENCY-CHECK.** The documented default NVD recheck interval is 4 hours. A scan or update job must actually run.

**RULE-BASED TOOLS.** Gitleaks, SAST, IaC and ZAP rules change through tool, policy or add-on updates. There is no common CVE refresh timer.

**PRIORITIZATION.** EPSS is refreshed daily. KEV grows as qualifying evidence is added. Poll and preserve the received snapshot.

Dependency-Check exposes nvdValidForHours and updateonly; noupdate disables its automatic update behavior. API credentials and rate limits affect refresh success. A scanner update and a database update are different operations: a current executable can use stale advisory data, while a fresh database cannot repair an unsupported package parser. Grype, OSV services and commercial platforms have their own provider and client refresh behavior. Verify the pinned release's documentation and observed timestamps rather than promising one universal interval.

**Key point:** Record both tool version and intelligence or rules revision.

Sources: [Dependency-Check update options](https://dependency-check.github.io/DependencyCheck/dependency-check-cli/arguments.html), [FIRST Exploit Prediction Scoring System](https://www.first.org/epss/), [CISA official KEV data mirror](https://github.com/cisagov/kev-data), [ZAP add-ons and rules](https://www.zaproxy.org/docs/desktop/addons/).

<a id="lesson-34"></a>

## 34. Freshness is an operational control

*04 INTELLIGENCE — Suggested operating policy, not a product default or universal requirement.*

**BEFORE A SCAN.** Check access to the approved source. Refresh as needed. Retain version, timestamps and update logs.

**ON AN OUTAGE.** Distinguish stale data from no findings. Block release when the accepted freshness budget is exceeded.

**AFTER RELEASE.** Schedule rescans of supported production artifacts. Trigger urgent checks after relevant new advisories.

Example organization policy: permit an advisory snapshot up to 24 hours old for ordinary builds, with a stricter emergency response when an exploited vulnerability is announced. That threshold is a local decision. Offline environments need an approved mirror, verified transferred data, recorded origin and an expiry rule. Trivy supports download-only and skip-update options; skipping updates requires a separate freshness control. Cache data to reduce network load, but do not treat a cache hit as a quality guarantee. This repository explains this control; it does not yet enforce database age automatically.

**Key point:** No update + no finding can still mean “insufficient evidence.”

Sources: [Trivy database refresh controls](https://trivy.dev/docs/latest/configuration/db/).

<a id="lesson-35"></a>

## 35. How to read a vulnerability report

*05 FINDINGS TO ACTION — Follow one result from package identity to remediation.*

**IDENTITY.** Target and digest; package name, ecosystem, installed version and evidence path.

**ADVISORY.** Identifier, affected range, severity source, fixed version and reference links.

**CONTEXT.** Tool and database versions, scan time, scope, suppressions and whether the package is shipped.

Start by confirming that the report belongs to the intended artifact and platform. Then verify package identification and advisory applicability. An empty fixed-version field usually means the source has not provided a fix; it does not mean safe. Multiple advisory aliases can describe the same vulnerability, so normalize aliases for counting without discarding separate affected components. Retain the raw report alongside normalized findings. The small reports/examples files in this repository are illustrative shapes, not complete vendor schemas or proof that a scan ran.

**Key point:** A useful finding explains what was matched, where, why and what to do next.

<a id="lesson-36"></a>

## 36. False positives, false negatives and unknowns

*05 FINDINGS TO ACTION — Accuracy includes knowing the limits of the inspection.*

**FALSE POSITIVE.** A reported issue does not apply: for example, incorrect package identity or a valid vendor backport.

**FALSE NEGATIVE.** A real issue is missed: for example, an unsupported file or missing authenticated route.

**UNKNOWN.** Evidence is incomplete: for example, a failed refresh, unresolved version or parser error.

Triage means investigating and assigning a finding. Validate identity, version, advisory source and execution context before suppressing it. A suppression should name the exact issue, reason, scope, owner and review date. Vulnerability Exploitability eXchange, or VEX, can carry statements about whether a product is affected, with justification; assess the producer and applicability before relying on it. Unknown status is not the same as pass. A useful review includes scan coverage and errors, rather than merely a zero count.

**Key point:** Reduce noise through evidence and scoped rules, not broad exclusions.

<a id="lesson-37"></a>

## 37. Turn scanner output into an explicit gate

*05 FINDINGS TO ACTION — This project uses a conservative, simple executable baseline.*

**SOURCE / IMAGE.** Trivy blocks HIGH and CRITICAL findings. Gitleaks blocks configured matches. Semgrep blocks local-rule findings.

**ERRORS.** Missing tools and failed scans stop their wrappers. Failure statuses propagate to the caller.

**RELEASE.** Unconfigured DAST and release verification stop with exit 2. They cannot establish production readiness.

The policy documents describe richer future decisions involving reachability, KEV, approvals and exceptions. Those decisions are not implemented by the scanner wrappers. The executable defaults intentionally differ: a suspected secret match blocks for review, and a high vulnerability can block even when no fix exists. A shell exit status is a process result; a release decision requires verified evidence from all mandatory controls. Store reports in an always-run artifact step while preserving the failed job status. Do not accept an old report simply because it remains in a working directory.

**Key point:** Document implemented behavior separately from the desired production architecture.

<a id="lesson-38"></a>

## 38. The release decision must fail closed

*05 FINDINGS TO ACTION — Missing, stale or mismatched evidence prevents approval.*

**BIND.** Match the commit, build run, platform and artifact digest across all required evidence.

**VERIFY.** Check required scan completion, coverage, freshness, signatures, provenance and trusted issuer identity.

**EVALUATE.** Apply versioned policy and validated exceptions. Save the reasons and the approved digest.

Fail closed means uncertainty prevents promotion until a required condition is resolved. Reports supplied by an untrusted pull request are not trustworthy just because they parse as JSON. Generate evidence in the trusted build context, protect its storage and verify its binding to the candidate artifact. Independently verify signature and provenance; never substitute a user-editable signature_verified: true field. A deploy job should depend on the gate result and receive the exact digest from that decision. See docs/implementation/release-contract.md for the acceptance checklist and integration boundary.

**Key point:** A gate that always prints success is a missing control.

<a id="lesson-39"></a>

## 39. Exceptions need a lifecycle

*05 FINDINGS TO ACTION — An exception is a documented risk decision with a limit.*

**REQUEST.** Identify finding, affected artifact or scope, reason, impact and proposed mitigation.

**APPROVE.** Assign an accountable approver, owner, expiry and remediation ticket. Protect approval records.

**REVALIDATE.** Check the scope and UTC expiry on each release. Reject expired or altered approvals.

UTC means Coordinated Universal Time, used to avoid ambiguous expiry checks across time zones. A compensating control reduces risk while the underlying issue is unresolved, such as disabling an affected feature. It must be evidenced, not assumed. An exception is different from a false-positive suppression: the former accepts a real risk, while the latter records that the reported condition does not apply. This project does not implement an exception parser or approval service. Do not bypass scanner errors by adding a blanket success override; integrate an authenticated decision system if exceptions are required.

**Key point:** An exception does not remove the finding or the obligation to remediate it.

<a id="lesson-40"></a>

## 40. What belongs in the release evidence package

*05 FINDINGS TO ACTION — Keep enough context to repeat and defend the decision.*

**SOURCE + TESTS.** Commit, reviewed change, runner/build identity, test results, scan scope and completion status.

**ARTIFACT + DATA.** Digest and platform, SBOM, reports, tool versions, rule revisions and advisory snapshot metadata.

**DECISION + DEPLOY.** Policy version, verified trust, approvals, exceptions, target environment and deployed digest.

Retain both machine-readable data and logs explaining execution. A JSON report may not contain every required version or database timestamp, so preserve supplementary metadata. Reports may contain code paths, URLs or credentials; restrict access and redact secrets. Retention should match organizational needs. Evidence should be tied to a specific run and protected from modification by untrusted contributors. Hashes detect changes only when the expected hash itself comes from a trusted source. An SBOM and its attestation should refer to the same artifact as the release decision.

**Key point:** Evidence is useful only when its origin, completeness and artifact binding can be trusted.

<a id="lesson-41"></a>

## 41. What this repository actually provides

*06 PROJECT PRACTICE — A teaching reference with runnable wrappers and incomplete deployment integrations.*

**AVAILABLE.** Source scanner wrappers, image and SBOM commands, signing entry point, policies and CI examples.

**DEMONSTRATION.** One Semgrep rule; an Audit-mode Kubernetes policy; illustrative reports and stack notes.

**INTEGRATION REQUIRED.** Tool provisioning, real application tests/build, DAST, trust verification, exceptions and deployment.

There is no application to build or deploy in this folder. The directories named examples contain stack guidance, not complete services. CI files under pipelines are templates and must be installed into the appropriate application repository. A standard hosted runner is not guaranteed to include Gitleaks, Trivy or Semgrep. Provision reviewed tool versions before executing the wrappers. DAST and release gate entry points now intentionally return failure until application-specific implementations exist. This makes the template's limits visible rather than producing a misleading green release.

**Key point:** Use the implementation guide to turn the reference into a tested application pipeline.

<a id="lesson-42"></a>

## 42. Local use: prerequisites and first checks

*06 PROJECT PRACTICE — Run Bash wrappers in Git Bash, Linux or a configured WSL environment.*

**PREPARE.** Install reviewed Git, Gitleaks, Trivy and Semgrep versions. Allow required advisory access.

**EXECUTE.** bash scripts/preflight.sh; bash scripts/secret-scan.sh; bash scripts/sca-scan.sh

**CONTINUE.** bash scripts/sast-scan.sh; bash scripts/iac-scan.sh; Inspect reports/generated/ and exit statuses.

WSL means Windows Subsystem for Linux. PowerShell does not interpret Bash syntax directly; launch the scripts with a compatible bash executable. Use the repository root as the working directory. Preflight now checks that source-scan tools exist and fails when they are missing. Trivy needs an initialized current database or access to download one. The source ZIP has no Git history, but the worktree secret scan still runs. To test image or SBOM commands, set IMAGE_REF to a real approved registry image pinned by digest. No scanner binaries are bundled with this project.

**Key point:** See docs/implementation/quickstart.md for commands, outputs and troubleshooting.

<a id="lesson-43"></a>

## 43. A stack changes inputs, not the control goals

*06 PROJECT PRACTICE — Use the same reasoning across application languages.*

**NODE / JAVA.** Node: resolved package lock and final image. Java: resolved Maven or Gradle graph, packaged archives and runtime image.

**PYTHON / .NET.** Python: pinned resolution plus built wheel/image. .NET: resolved NuGet dependencies and published application.

**GO.** Module resolution plus built binary metadata and image. Add language-aware vulnerability and code checks as needed.

The manifest tells a package manager what is requested; resolved dependencies tell you what the build selected. A final image can contain additional system components absent from application lockfiles. Native tooling can improve ecosystem context, but its version and advisory service must also be tracked. Test the actual supported input formats for the scanner release you choose. A dependency may be used only during development, still present in the build environment, or shipped in production: these have different exposure. Retain enough evidence to distinguish them.

**Key point:** Scan the resolved dependencies and the final deliverable; validate the supported formats.

<a id="lesson-44"></a>

## 44. CI templates need explicit setup

*06 PROJECT PRACTICE — Continuous Integration platforms differ in syntax and trust configuration.*

**RUNNER.** Provision reviewed tool versions. Isolate untrusted changes. Use least-privilege, short-lived credentials.

**JOBS.** Preserve scanner failures and always collect reports. Pass the artifact digest explicitly between jobs.

**PROMOTION.** Require checks and protected environments. Verify policy before production deployment.

Jenkins uses agents and pipeline stages; GitHub Actions uses workflows and jobs; GitLab CI uses jobs organized by stages; Azure DevOps uses pipelines, jobs and environments. The repository examples need a real tool-provisioning step or a reviewed runner image. Pin third-party actions to verified commit identifiers and container tools to digests, then maintain them through reviewed updates. Do not put privileged secrets on jobs that run untrusted pull-request code. A manual approval button does not replace artifact verification or completed security checks.

**Key point:** A copied YAML file is an integration starting point, not proof of enforcement.

<a id="lesson-45"></a>

## 45. Corrections made during this review

*06 PROJECT PRACTICE — Changes address misleading pass results and inconsistent scope.*

**SCAN WRAPPERS.** Explicit configuration, blocking exit behavior, worktree secret coverage and digest validation.

**PIPELINES.** Removed ignored scan failures. Fixed chained command failure handling. Added clearer prerequisite and evidence guidance.

**LEARNING MATERIAL.** Rebuilt flow, expanded terminology, explained comparison data and separated implementation from target design.

The old release placeholder returned success without evaluating anything, and DAST printed instructions without scanning. Both now fail explicitly. Trivy commands now pass the supplied configuration and request a non-zero status for blocking findings. Semgrep uses the reviewed local demonstration rule with explicit finding/error behavior. The image, SBOM and signing wrappers reject mutable image references. Jenkins and GitLab no longer mask scanner or SBOM failures. A dedicated validation report records what was actually checked and which external integrations remain untested.

**Key point:** See docs/PROJECT_REVIEW.md for the issue list, changes and remaining integration work.

<a id="lesson-46"></a>

## 46. Troubleshooting by symptom

*06 PROJECT PRACTICE — Resolve missing evidence before interpreting security results.*

**TOOL NOT FOUND.** Check PATH and runner provisioning. Preflight or the wrapper should fail instead of silently skipping.

**DB DOWNLOAD FAILS.** Check network, proxy, rate limits, credentials and supported cache format. Review the last successful update.

**ZERO FINDINGS.** Check recognized files, packages, rules, exclusions and authenticated routes before calling it clean.

PATH is the operating system's command search list. If commands work in one terminal but not CI, compare environments and executable versions. A database schema mismatch may require a compatible tool/cache refresh rather than bypassing updates. A source scan with no supported dependencies can produce no vulnerability findings even though nothing meaningful was assessed. For DAST, confirm login success and route coverage. For SAST, check supported language parsers, skipped files and configuration loading. Report status and useful error messages should be preserved during failure.

**Key point:** “The tool ran” and “the intended scope was assessed” are separate checks.

<a id="lesson-47"></a>

## 47. After release: a new CVE changes the answer

*07 OPERATIONS — The artifact is unchanged; the available knowledge has changed.*

**DETECT.** A new advisory or KEV entry arrives. Search inventories and rescan affected supported artifacts.

**RESPOND.** Confirm applicability and exposure. Assign an owner, fix or mitigate, and set a response deadline.

**RELEASE AGAIN.** Rebuild from controlled inputs, repeat the affected checks, deploy and verify the new digest.

Service Level Agreement, or SLA, often refers here to an internal remediation deadline rather than an external service contract. Define severity and exposure criteria and an escalation owner. Mean Time to Remediate, or MTTR, measures elapsed remediation time, but state when the clock starts and stops. A rescan alone does not patch production. The team must update dependencies or configuration, test the change and release a new artifact. Track supported versions and end-of-life components; unavailable maintenance changes the remediation options.

**Key point:** A security result expires as the artifact, environment or intelligence changes.

<a id="lesson-48"></a>

## 48. Standards guide outcomes and assurance

*07 OPERATIONS — This architecture is a reference; its exact sequence is not universally mandated.*

**NIST SSDF.** Secure Software Development Framework: organizational practices for preparing, protecting, producing and responding.

**OWASP.** Open Worldwide Application Security Project: application requirements, verification guidance and maturity resources.

**SLSA.** Supply-chain Levels for Software Artifacts: requirements and assurance concepts for source and build integrity.

NIST is the National Institute of Standards and Technology. This material references the named SSDF v1.1 publication rather than claiming it is always the latest revision. SLSA is often pronounced salsa. Implementing a signature alone does not establish a SLSA level; the applicable requirements and builder properties matter. OWASP ASVS means Application Security Verification Standard; SAMM means Software Assurance Maturity Model. CIS means Center for Internet Security, whose benchmarks provide configuration guidance. Mapping a control to a standard is not equivalent to certification or a compliance determination.

**Key point:** Use named versions and evidence-based mappings; avoid unsupported compliance claims.

Sources: [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final), [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/).

<a id="lesson-49"></a>

## 49. Adopt in small, verifiable increments

*07 OPERATIONS — Suggested engineering sequence; adapt it to application risk.*

**FOUNDATION.** Protect source, provision tools, run tests and enforce a small set of high-signal source checks.

**ARTIFACT TRUST.** Scan the deliverable, generate inventory, verify signing and preserve the same digest through staging.

**OPERATIONS.** Add authenticated behavior tests, trusted release evidence, admission controls and recurring response.

For each new control, first establish coverage and ownership, then test a passing case, a genuine violation and an operational failure. A control that works only on success is incomplete. Define an explicit observation period if tuning is necessary, and label results as advisory until enforcement is enabled. Measure scan coverage, freshness violations, bypasses, finding recurrence and remediation time alongside pipeline duration. Prioritize stable control ownership over accumulating products. The sample project is intentionally not an attempt to deploy every tool mentioned.

**Key point:** One reliable, owned control is more useful than several unverified report generators.

<a id="lesson-50"></a>

## 50. Check your understanding

*08 REVIEW — Try answering before opening the explanations in the notes.*

**QUESTION 1.** Why can a new CVE appear in an image that has not changed?

**QUESTION 2.** Why does a clean ZAP baseline not prove that customer authorization is correct?

**QUESTION 3.** Why must release verification reject a report about the wrong digest?

Answer 1: the advisory data changed, so a new scan can match an existing component to newly available vulnerability information. Answer 2: baseline scanning primarily crawls and passively inspects discovered responses; business authorization requires authenticated users, ownership expectations and deliberate assertions. Answer 3: the report describes different content and cannot establish the release candidate's assessment. Additional exercise: explain why a Gitleaks match is not proof that a token is active, why an SBOM is not a vulnerability report, and why signing still requires identity verification.

**Key point:** If you can explain the evidence behind a decision, you understand the pipeline.

<a id="lesson-51"></a>

## 51. What a defensible release can explain

*08 REVIEW — Five questions connect the entire course.*

**WHAT CHANGED?.** Identify reviewed source, dependencies and build inputs.

**WHAT WAS CHECKED?.** Show the scope, outcomes, tool/rule/data versions and remaining uncertainty.

**WHAT WAS RELEASED?.** Show the approved digest, trusted origin, policy decision and production deployment record.

The remaining two questions are who owns residual risk and what happens when new evidence appears. An effective DevSecOps system connects technical results with owners and operational response. No scanner guarantees that an application is free of vulnerabilities. The practical goal is to establish repeatable checks, make their limits visible, prevent unsupported promotion and respond quickly when knowledge changes. Read the handbook alongside the implementation quickstart and project review before adapting the pipeline.

**Key point:** Reviewed source → tested artifact → verified release → continuous response.

<a id="lesson-52"></a>

## 52. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** CVE identifier lifecycle; ; NVD vulnerability enrichment

**PRIMARY REFERENCES.** Trivy: vulnerability matching; ; Trivy database build and metadata

**PRIMARY REFERENCES.** Trivy database publication schedule; ; Trivy Java index

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [CVE identifier lifecycle](https://www.cve.org/about/Process), [NVD vulnerability enrichment](https://nvd.nist.gov/general/FAQ-Sections/CVE-FAQs), [Trivy: vulnerability matching](https://trivy.dev/docs/latest/scanner/vulnerability/), [Trivy database build and metadata](https://github.com/aquasecurity/trivy-db), [Trivy database publication schedule](https://raw.githubusercontent.com/aquasecurity/trivy-db/main/.github/workflows/cron.yml), [Trivy Java index](https://github.com/aquasecurity/trivy-java-db).

<a id="lesson-53"></a>

## 53. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** Java index publication schedule; ; Trivy database refresh controls

**PRIMARY REFERENCES.** Dependency-Check detection model; ; Dependency-Check update options

**PRIMARY REFERENCES.** Gitleaks detection and configuration; ; Semgrep rule and analysis concepts

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [Java index publication schedule](https://raw.githubusercontent.com/aquasecurity/trivy-java-db/main/.github/workflows/cron.yml), [Trivy database refresh controls](https://trivy.dev/docs/latest/configuration/db/), [Dependency-Check detection model](https://devguide.owasp.org/en/05-implementation/02-dependencies/01-dependency-check/), [Dependency-Check update options](https://dependency-check.github.io/DependencyCheck/dependency-check-cli/arguments.html), [Gitleaks detection and configuration](https://github.com/gitleaks/gitleaks), [Semgrep rule and analysis concepts](https://semgrep.dev/docs/writing-rules/glossary).

<a id="lesson-54"></a>

## 54. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** Semgrep command and exit semantics; ; CodeQL database and query model

**PRIMARY REFERENCES.** SonarQube analysis overview; ; Checkov configuration and graph checks

**PRIMARY REFERENCES.** ZAP baseline scope and exit codes; ; ZAP full scan

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [Semgrep command and exit semantics](https://docs.semgrep.dev/cli-reference), [CodeQL database and query model](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli), [SonarQube analysis overview](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview), [Checkov configuration and graph checks](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html), [ZAP baseline scope and exit codes](https://www.zaproxy.org/docs/docker/baseline-scan/), [ZAP full scan](https://www.zaproxy.org/docs/docker/full-scan/).

<a id="lesson-55"></a>

## 55. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** ZAP add-ons and rules; ; Syft software inventory

**PRIMARY REFERENCES.** Grype vulnerability scanning; ; Cosign signature verification

**PRIMARY REFERENCES.** Kyverno admission validation; ; Falco runtime rules

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [ZAP add-ons and rules](https://www.zaproxy.org/docs/desktop/addons/), [Syft software inventory](https://github.com/anchore/syft), [Grype vulnerability scanning](https://github.com/anchore/grype), [Cosign signature verification](https://docs.sigstore.dev/cosign/verifying/verify/), [Kyverno admission validation](https://kyverno.io/docs/policy-types/cluster-policy/validate/), [Falco runtime rules](https://falco.org/docs/concepts/rules/).

<a id="lesson-56"></a>

## 56. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** FIRST Exploit Prediction Scoring System; ; FIRST CVSS v4.0 specification

**PRIMARY REFERENCES.** CISA official KEV data mirror; ; MITRE Common Weakness Enumeration

**PRIMARY REFERENCES.** Open Source Vulnerabilities; ; NIST SP 800-218 SSDF v1.1

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [FIRST Exploit Prediction Scoring System](https://www.first.org/epss/), [FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document), [CISA official KEV data mirror](https://github.com/cisagov/kev-data), [MITRE Common Weakness Enumeration](https://cwe.mitre.org/about/index.html), [Open Source Vulnerabilities](https://osv.dev/), [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="lesson-57"></a>

## 57. Sources and maintenance

*09 SOURCES — Official documentation; full clickable links are in the slide notes and handbook.*

**PRIMARY REFERENCES.** SLSA v1.2 specification

These references support the tool-specific descriptions. Review behavior against your pinned versions when maintaining the project. Product behavior and publication schedules can change.

**Key point:** Source review date: 2026-09-16. Local configuration determines actual behavior.

Sources: [SLSA v1.2 specification](https://slsa.dev/spec/v1.2/).
