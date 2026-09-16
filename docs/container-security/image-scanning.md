# Image Scanning

Scan the exact image digest intended for release. Re-scan registry images periodically because new CVEs can be disclosed after build.

Record:

- image digest;
- scanner/database timestamp;
- finding list;
- gate decision;
- exception IDs.

<!-- course-explanation -->
## Working principle and implementation status

**LAYERS.** A container image packages application files, libraries and often operating-system packages.

**SCAN TARGET.** Inspect the release digest for the intended platform. Include base image and application package metadata.

**HARDENING.** Use minimal trusted bases, non-root execution, limited permissions and controlled updates.

An image is a packaged filesystem and configuration. A container is a running instance of an image. Removing a file in a later layer does not necessarily remove its content from earlier layers, so never bake credentials into builds. Vulnerability, secret and configuration checks are distinct capabilities. This repository's image wrapper explicitly scans vulnerabilities and requires a digest; it does not claim to scan every image secret or enforce runtime hardening. New base-image vulnerabilities require rebuilding from an updated base and then rescanning the newly produced digest.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-23), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
