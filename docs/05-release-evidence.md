# Release Evidence Package

For a controlled production release, capture enough evidence to answer **what changed, what was tested, what artifact was approved, and who/what authorized deployment**.

Recommended evidence:

- commit SHA and pull request;
- branch/review status;
- SAST/SCA/secret/IaC results;
- test summary;
- artifact digest;
- container/image scan result;
- SBOM;
- signature/attestation/provenance;
- staging deployment identifier;
- DAST/API-security result;
- exceptions with owner and expiry;
- release approval/policy decision;
- production deployment record;
- rollback reference.

Evidence retention should follow the organization's audit and regulatory requirements.
