# Introduction

DevSecOps integrates security practices into the same engineering system used to design, build, test, release, deploy, and operate software. The goal is not to add one final security scan; it is to create continuous, risk-based feedback and enforceable release decisions throughout the SDLC.

## Core principles

1. **Security begins before code** — define security requirements and threat-model important changes.
2. **Automate repeatable checks** — secrets, dependencies, source code, IaC, images, SBOM, and deployment policy.
3. **Test the built/running system** — source scanning alone cannot validate runtime configuration or application behavior.
4. **Use risk-based gates** — distinguish findings from release decisions.
5. **Preserve artifact identity** — build once and promote the same signed artifact/digest.
6. **Make exceptions explicit** — documented owner, justification, compensating control, approval, and expiry.
7. **Monitor production** — secure development does not remove runtime risk.
8. **Feed incidents and findings back into engineering** — prevention improves when root causes are addressed.
