# CI/CD Pipeline Examples

These files are reference implementations. Adapt credentials, runner labels, build commands, deployment targets, scanner versions, and thresholds before use.

These templates do not provision scanner tools or an application. Read the [quickstart](../docs/implementation/quickstart.md) before running them. Required tools must be installed in the runner before scan steps. DAST and release-gate wrappers return exit 2 until the [application release contract](../docs/implementation/release-contract.md) is implemented. Explanatory build/test/deploy steps are not successful tests or real deployments.

Publish a container candidate to a restricted registry before registry-based scan/sign operations, then transfer its immutable digest and evidence between jobs. Candidate publication does not grant production approval. Preserve reports on failure without ignoring failed jobs. Do not expect job-local files or environment variables to automatically carry between jobs.

- `jenkins/Jenkinsfile` — full stage layout.
- `github-actions/devsecops.yml` — GitHub Actions pattern.
- `gitlab/.gitlab-ci.yml` — GitLab CI pattern.
- `azure-devops/azure-pipelines.yml` — Azure DevOps pattern.

Production recommendation: pin third-party actions/plugins/images to trusted immutable versions/digests wherever practical.
