# Pull-Request Security

PR automation should give developers fast feedback. Run high-signal controls first and avoid leaking secrets into logs.

Suggested PR checks:

- secret scan;
- SCA;
- SAST;
- IaC/config scan;
- unit/integration tests;
- policy checks for changed high-risk files.

Keep production deployment credentials unavailable to untrusted fork/PR jobs.
