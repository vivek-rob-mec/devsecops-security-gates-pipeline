# Container Security Policy

Production containers should:

- come from approved registries;
- use immutable digests for deployment;
- pass required vulnerability/misconfiguration gates;
- run as non-root unless an exception exists;
- avoid privileged mode and unnecessary capabilities;
- carry verifiable signature/provenance where enforced.
