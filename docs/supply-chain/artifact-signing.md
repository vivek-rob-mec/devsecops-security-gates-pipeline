# Artifact Signing

Recommended flow:

`source → protected CI build → artifact digest → vulnerability scan → SBOM → signature/attestation → registry → verification → deploy`

Sign the immutable digest, not only a mutable tag or filename.
