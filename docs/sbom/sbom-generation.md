# SBOM Generation

Example with Syft:

```bash
syft your-image@sha256:<digest> -o cyclonedx-json=reports/generated/sbom.cdx.json
```

Example with Trivy:

```bash
trivy image --format cyclonedx --output reports/generated/sbom.cdx.json your-image@sha256:<digest>
```

<!-- course-explanation -->
## Working principle and implementation status

**GENERATE.** Syft or Trivy examines the artifact and emits a structured inventory.

**EXCHANGE.** CycloneDX and SPDX are interoperable formats. SPDX expands to Software Package Data Exchange.

**USE.** Link the inventory to the artifact digest. Recheck it when new vulnerability information appears.

An SBOM is analogous to an ingredient list: it supports later questions about whether an affected component is present. It can contain names, versions, identifiers, relationships, hashes and licenses, depending on format and producer. Syft is an inventory generator, rather than a CVE matching engine. A generator does not need a vulnerability database to list packages. The quality of later vulnerability matching depends on inventory completeness. This project can generate CycloneDX JSON for a digest, but does not validate a full release evidence package or perform automatic inventory ingestion.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-24), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
