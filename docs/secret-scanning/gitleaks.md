# Gitleaks

Example local scan:

```bash
gitleaks detect --source . --redact --report-format sarif --report-path reports/generated/gitleaks.sarif
```

For CI, use a reviewed configuration and decide whether you are scanning the worktree, commit range, or repository history. Always redact secrets in console/report output.

<!-- course-explanation -->
## Working principle and implementation status

**INPUT / FINDINGS.** Files and Git history. Finds likely tokens, keys and other secrets with file and rule context.

**HOW IT WORKS.** Rules use patterns, keywords and optional entropy checks. Entropy measures apparent randomness.

**DATA / LIMITS.** Embedded and custom rules; no CVE feed. A pattern match does not establish that a credential is active.

Gitleaks combines configured detection rules with exclusions. Updating the executable refreshes embedded rules; a custom rules file changes through a reviewed configuration update. This project explicitly loads configs/gitleaks/.gitleaks.toml, extending the default rules. The wrapper checks the worktree and also reachable Git history when Git metadata exists. A downloaded ZIP contains no history. It redacts report secrets. A match requires investigation; any real exposed credential needs revocation or rotation, even if the code is deleted. Avoid broad allowlists that hide future exposures.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-14), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
