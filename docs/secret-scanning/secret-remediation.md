# Secret Remediation

1. Treat a verified leaked secret as compromised.
2. Revoke/rotate it at the issuer.
3. Search logs, artifacts, forks, caches, and prior commits for exposure.
4. Replace it with secret-manager/CI-secret retrieval.
5. Remove the secret from the working tree.
6. Decide whether history rewriting is required.
7. Document impact and prevention action.
