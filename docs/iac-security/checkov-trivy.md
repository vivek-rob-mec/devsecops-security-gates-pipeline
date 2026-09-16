# Checkov and Trivy Misconfiguration Scanning

Both can cover IaC/configuration use cases. Standardize one primary policy set to avoid duplicated noisy findings, and use a second tool where it provides materially different coverage.

<!-- course-explanation -->
## Working principle and implementation status

**FINDS.** Examples include public storage, broad network access, privileged workloads and missing encryption settings.

**HOW.** Parse configuration and evaluate resource attributes or relationships against checks and organizational policy.

**DATA / LIMITS.** Rules and policy bundles, not primarily a CVE database. Templates may not equal deployed state.

Trivy config and Checkov inspect supported infrastructure formats. Checkov includes attribute and graph-based checks; graph analysis reasons about connected resources such as a service linked to a public network. A rule must consider explicit and inherited configuration, not just whether one string appears. Update the tool and policy bundles with review. Variables, dynamic templates and unmanaged changes can reduce accuracy, so inspect rendered manifests or plans when supported and audit the deployed environment separately. The current Trivy wrapper blocks HIGH and CRITICAL configuration findings.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-22), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
