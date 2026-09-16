# Cosign / Sigstore

Cosign can sign and verify container images and attestations. Prefer keyless/workload-identity workflows where they fit your trust model; otherwise protect signing keys in a managed KMS/HSM or equivalent secure system.

<!-- course-explanation -->
## Working principle and implementation status

**DIGEST / SIGNATURE.** The digest identifies content. A signature binds a signing key or identity to that content.

**PROVENANCE.** An attestation describes the builder and inputs. Its trust depends on the builder and how evidence was produced.

**VERIFY.** Check the expected signer, identity issuer, artifact digest and required claims before deployment.

Cosign supports verification using public keys or certificate identity and issuer constraints. OpenID Connect, or OIDC, can provide a short-lived workload identity used in keyless signing flows. Fulcio and Rekor are Sigstore services involved in certificates and transparency evidence. A transparency log records evidence; it does not prove the software has no vulnerabilities. Never accept any valid signer when only one build workflow is trusted. The project signing wrapper signs an explicit digest but leaves key or workload-identity setup to the organization; production verification remains an integration requirement.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-25), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
