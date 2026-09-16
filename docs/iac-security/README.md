# Infrastructure-as-Code Security

IaC scanning evaluates Terraform, Kubernetes manifests, Dockerfiles, Helm, CloudFormation, and other configuration before deployment.

Common issues:

- public network exposure;
- over-privileged IAM/RBAC;
- encryption disabled;
- insecure container settings;
- missing logging;
- permissive security groups;
- mutable/unpinned images;
- unsafe Kubernetes privileges.
