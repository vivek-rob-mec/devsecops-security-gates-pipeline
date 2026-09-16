# Trivy for SCA

Examples:

```bash
trivy fs --scanners vuln,misconfig --severity HIGH,CRITICAL .
trivy image --severity HIGH,CRITICAL your-image@sha256:<digest>
```

For a mature gate, add policy around fixed/unfixed vulnerabilities, exploitability/reachability, baseline findings, and exceptions instead of relying only on raw severity.

<!-- course-explanation -->
## Working principle and implementation status

**INPUT.** Filesystem manifests or image package metadata. An image adds operating-system packages and packaged application libraries.

**COMPARISON DATA.** Trivy DB aggregates vendor and ecosystem advisories. OS-managed packages use the corresponding distribution source.

**OUTPUT / LIMIT.** Known vulnerable components. This project enables vulnerability scanning; licenses and image secrets need separate controls.

Trivy selects advisory sources according to package type and origin. Vendor advisories help account for distribution backports. The JSON report can identify the severity source, so two scanners can legitimately show different ratings. The source wrapper uses trivy fs; the image wrapper uses trivy image with an immutable reference. Config scanning is a separate operation. The current wrappers block HIGH and CRITICAL findings, including those without fixes. They do not calculate application reachability. The local Trivy configuration is now explicitly passed rather than merely stored in the repository.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-17), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
