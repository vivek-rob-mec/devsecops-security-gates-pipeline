# Security Tool Matrix

| Control | Common open-source / built-in choices | Enterprise/commercial examples | Where it usually runs |
| --- | --- | --- | --- |
| Secret scanning | Gitleaks, TruffleHog | GitHub Secret Scanning, GitLab Secret Detection | Pre-commit / PR / CI / server-side |
| SCA | Trivy, OWASP Dependency-Check, osv-scanner | Snyk, Mend, Black Duck | PR / CI / scheduled |
| SAST | Semgrep Community, CodeQL (eligible use), SonarQube Community | Checkmarx, Fortify, Veracode, Semgrep AppSec | PR / CI |
| IaC | Trivy, Checkov | Wiz, Prisma Cloud, Snyk IaC | PR / CI |
| Container image | Trivy, Grype | Registry/cloud-native scanners, Prisma/Wiz | Build / registry / scheduled |
| SBOM | Syft, Trivy, CycloneDX tools | Platform-native inventory products | Build / release |
| DAST | OWASP ZAP | Burp Suite Enterprise, Invicti | Staging |
| Signing | Cosign/Sigstore, Notation | KMS/HSM-backed enterprise signing | Release |
| K8s policy | Kyverno, OPA Gatekeeper | Platform policy products | Admission / deploy |
| Runtime | Falco, Tetragon | EDR/CNAPP/runtime platforms | Production |

Tool popularity changes. Choose based on language coverage, deployment model, signal quality, support, policy/reporting needs, integration cost, and organizational constraints—not logos alone.
