# DevSecOps Lifecycle

| Phase | Security objective | Evidence |
| --- | --- | --- |
| Plan | Define security requirements and abuse cases | Requirements, risk classification |
| Design | Identify threats and controls | Threat model, architecture review |
| Develop | Prevent common defects and secret leakage | Review records, pre-commit results |
| Verify | Detect code/dependency/configuration risk | SAST/SCA/IaC/test reports |
| Build | Secure the deliverable | Image scan, SBOM, digest |
| Release | Establish integrity and provenance | Signature, attestation, approvals |
| Stage | Test the running service | DAST/API results |
| Deploy | Enforce release policy | Admission/policy logs, deployment record |
| Operate | Detect and respond | Runtime alerts, SIEM/EDR events |
| Improve | Remove recurring root causes | Post-incident actions, updated standards |
