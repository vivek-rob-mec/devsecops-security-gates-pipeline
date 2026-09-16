# Run and understand the project

## 1. Start with the right expectation

This is a reference project, not an application or a ready-to-deploy production pipeline. Source-scan wrappers execute tools you install. DAST and release verification are deliberately incomplete and return exit status 2. That is expected until you implement the application-specific contracts.

Read the [handbook](../DEVSECOPS_HANDBOOK.md) for the flow and working principles, and the [project review](../PROJECT_REVIEW.md) for implemented changes and remaining work.

## 2. Choose a shell and install tools

The wrappers require Bash. On Windows, use Git Bash or a configured Windows Subsystem for Linux (WSL) distribution. Do not paste Bash environment-variable syntax directly into PowerShell. Use Linux runners for application CI unless you have validated another environment.

Install reviewed releases from the official projects:

| Tool | Purpose | Installation and verification |
| --- | --- | --- |
| Git | Source history | Install Git; check `git --version` |
| Gitleaks | Secret patterns | [Official releases and install guidance](https://github.com/gitleaks/gitleaks); check `gitleaks version`; the wrapper uses `dir` and `git` subcommands |
| Trivy | Dependencies, images and configuration | [Official installation](https://trivy.dev/docs/latest/getting-started/installation/); check `trivy --version` |
| Semgrep | Code/rule analysis | [Official CLI documentation](https://docs.semgrep.dev/cli-reference); check `semgrep --version` |
| Syft, optional | Inventory generation | [Official project](https://github.com/anchore/syft); check `syft version`; Trivy is the inventory fallback |
| Cosign, optional | Artifact signing | [Official project](https://github.com/sigstore/cosign); check `cosign version`; configure trusted keys or workload identity separately |

Pin reviewed versions and verify downloaded signatures/checksums using the publisher's instructions. Maintain the versions through reviewed updates. No scanner binaries, application package installations or security platform accounts are bundled here. The presentation dependencies are unrelated to the security scanners.

Network access is generally needed for initial vulnerability data, registry images and any remotely selected rules. Configure a proxy or approved mirror where required; do not conceal update errors. A ZIP download contains no Git history. This is supported for worktree scanning, but historical coverage requires a full clone.

## 3. Run source checks

From the project root in Bash:

```bash
bash scripts/preflight.sh
bash scripts/secret-scan.sh
bash scripts/sca-scan.sh
bash scripts/sast-scan.sh
bash scripts/iac-scan.sh
```

Run commands individually while learning, or use `make security` after provisioning tools and Make. In a shell script, enable `set -euo pipefail` or explicitly chain required operations with `&&`; interactive shells do not automatically stop after every non-zero command.

From PowerShell with Git Bash installed at its standard location:

```powershell
& 'C:/Program Files/Git/bin/bash.exe' scripts/preflight.sh
$LASTEXITCODE
```

After reviewing prerequisites, invoke each desired wrapper the same way. `$LASTEXITCODE` is the status of the last native command. Zero means the wrapper's configured checks passed; non-zero means a finding or an execution/configuration failure. Inspect the output to distinguish them.

| Wrapper | Actual scope | Report | Implemented blocking behavior |
| --- | --- | --- | --- |
| `secret-scan.sh` | Worktree, then reachable Git history when available | `gitleaks.sarif`, optionally `gitleaks-history.sarif` | Configured secret matches or errors block; a match is not verified token activity |
| `sca-scan.sh` | Supported dependency inputs under repository root | `trivy-fs.json` | HIGH/CRITICAL vulnerabilities block, including unfixed ones |
| `sast-scan.sh` | Approved local Semgrep config | `semgrep.sarif` | All findings from that ruleset block; strict error handling requested |
| `iac-scan.sh` | Supported configuration under root | `trivy-config.json` | HIGH/CRITICAL misconfigurations block |
| `image-scan.sh` | Explicit image digest | `trivy-image.json` | HIGH/CRITICAL vulnerabilities block |
| `generate-sbom.sh` | Explicit image digest | `sbom.cdx.json` | Missing tools/input or generator errors block |
| `sign-artifact.sh` | Explicit image digest | Provider-dependent signing output | Signing failure blocks; verification is not performed here |
| `dast-scan.sh` | Integration stub | None | Always fails until implemented |
| `security-gate.sh` | Integration stub | None | Always fails until implemented |

Reports default to `reports/generated/`. `REPORT_DIR` can override the location; a relative value is resolved from the repository root. Use a fresh run-specific report directory in CI. Preserve the process status and upload available reports even on failure; never interpret an old report as a new scan.

The local Semgrep ruleset only demonstrates detection of ignored pipeline failures. It is **not broad SAST coverage**. Supply an approved application ruleset, for example:

```bash
SEMGREP_CONFIG=/path/to/reviewed/rules bash scripts/sast-scan.sh
```

Rules, tool versions and scan scope all need review. Excluding generated reports and local presentation libraries prevents irrelevant noise, but every exclusion is part of the coverage boundary.

## 4. Image, SBOM and signing commands

Replace the descriptive placeholder below with a real immutable digest before running. These commands are not a request to scan an arbitrary public target.

```bash
export IMAGE_REF='registry.example/team/shop@sha256:<64-lowercase-hex-characters>'
bash scripts/image-scan.sh
bash scripts/generate-sbom.sh
```

The wrapper rejects the placeholder and mutable tags such as `latest`. Push the built candidate to an access-controlled registry, resolve its digest and pass that actual reference. For a multi-platform image, define which platform digests are approved and scan them accordingly.

After your key or workload identity has been configured:

```bash
bash scripts/sign-artifact.sh
```

Signing can write signature material to a remote registry or transparency service. Its output does not by itself authorize deployment. Add verification of the expected key or identity/issuer and provenance claims to the [release contract](release-contract.md).

## 5. Understand database freshness

The [detection and update matrix](../DETECTION_AND_DATA.md) distinguishes data publication, local refresh and your scan schedule. For Trivy, the following initializes or refreshes the cached vulnerability database as the tool determines necessary:

```bash
trivy image --download-db-only
trivy --version
```

If the scan requires the Java identification index, initialize it with `trivy image --download-java-db-only`. Preserve the metadata in the configured cache and the scan logs. Download time alone does not establish the age of the source data. The repository wrappers do not yet enforce a database-age budget. That is a separate production integration requirement.

## 6. Integrate one CI platform

1. Pick one template under `pipelines/` and read its README.
2. Provision reviewed tools before the first scan; hosted runners do not guarantee these binaries.
3. Install the template in the platform's active location and require the resulting checks on the protected branch.
4. Add real application tests and build commands. Replace explanatory `echo` steps.
5. Transfer the candidate digest and evidence between jobs; job workspaces are not automatically shared.
6. Add authenticated staging tests, trust verification and the release contract.
7. Validate a passing build, a genuine finding, a tool failure and missing/stale/wrong-digest evidence.

These templates do not provision an application, registry, signing identity, cluster or scanner service.

## 7. Validate repository changes locally

The standard-library checks below do not install or execute real security scanners:

```powershell
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

The wrapper tests substitute controlled fake commands to verify argument selection and failure propagation. They are not live scanner acceptance tests. Use a real application and reviewed scanner versions to validate detection before deployment.

## Troubleshooting

| Symptom | Interpretation | Next step |
| --- | --- | --- |
| Exit 127 | Required command unavailable | Compare PATH and installed tools with the runner setup |
| Trivy update error | Required data could not be refreshed/loaded | Inspect connectivity, throttling, credentials and cache compatibility |
| No findings in this repository | There may be no supported application dependency inputs | Check package discovery and scan summary; test on the real application |
| Semgrep only checks failure suppression | You are using the intentionally small demonstration ruleset | Integrate reviewed language/security rules |
| DAST exits 2 | Scanner integration is absent | Configure target scope, login, rate limits, mode, reports and failure behavior |
| Release gate exits 2 | Release contract is absent | Integrate verified evidence rather than bypassing the error |
| Signing fails | Identity, registry access or signing configuration is unavailable | Correct the intended trust setup; never treat an unsigned result as signed |
