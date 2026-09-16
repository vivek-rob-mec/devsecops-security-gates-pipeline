# OWASP Dependency-Check

OWASP Dependency-Check is especially common in Java-centric environments and correlates identified dependencies with vulnerability data. Keep its vulnerability database/cache updated and review suppression rules because overly broad suppression can hide genuine risk.

<!-- course-explanation -->
## Working principle and implementation status

**DEPENDENCY-CHECK.** Analyzers collect package evidence, identify CPE candidates and consult NVD applicability data.

**OSV.** Open Source Vulnerabilities uses ecosystem-oriented records, package versions and affected ranges or commits.

**GRYPE.** Matches inventoried packages against its vulnerability database; can scan an image, filesystem or supported SBOM.

Dependency-Check is common in Java projects but has multiple analyzers. An ambiguous product name can produce an incorrect CPE candidate; inspect evidence and scope any suppression to the proven mismatch. OSV aligns vulnerability records to open-source ecosystems, and advisories can have aliases such as CVE or GHSA identifiers. Grype uses its own provider aggregation and matching behavior. These are alternatives or targeted secondary checks, not mandatory duplicates. The repository only directly wraps Trivy. A product being mentioned in a tool matrix does not mean that it is installed or integrated.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-18), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
