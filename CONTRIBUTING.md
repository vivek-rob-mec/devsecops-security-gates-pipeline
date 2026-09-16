# Contributing

Contributions should improve defensive DevSecOps implementation guidance, examples, or documentation.

## Workflow

1. Create a branch.
2. Make a focused change.
3. Run repository validation/security checks.
4. Open a pull request.
5. Describe security impact and any new dependencies/actions/tools.
6. Obtain required review before merge.

## Pull-request expectations

- no secrets or private environment data;
- no unsanitized customer/company scan reports;
- examples must clearly separate illustrative policy from universal requirements;
- commands that perform active security testing must state that the target must be authorized;
- new GitHub Actions should be pinned to a trusted release or, preferably, immutable commit SHA in production forks;
- new dependencies should have a clear reason.
