# GitHub Actions

For production forks:

- use least-privilege `permissions`;
- protect deployment environments;
- require reviewers for production;
- prefer OIDC federation to long-lived cloud credentials;
- pin third-party actions to trusted commit SHAs;
- avoid making production secrets available to untrusted PRs/forks.
