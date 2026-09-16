# Semgrep

Example:

```bash
semgrep scan --config auto --sarif --output reports/generated/semgrep.sarif .
```

For production pipelines, use reviewed rule packs, baseline/tuning, path exclusions, and rule ownership. Do not automatically suppress noisy rules without documenting why.

<!-- course-explanation -->
## Working principle and implementation status

**DETECTION.** Structural patterns and taint rules describe unsafe code. Analysis depth depends on engine, language and edition.

**DATA / UPDATES.** Local YAML rules or registry rulesets. Pin and review rules; upgrade the engine separately.

**PROJECT BEHAVIOR.** The local demonstration rule flags ignored pipeline failures. --error makes findings fail; --strict handles scan errors more strictly.

The project's Semgrep rule is deliberately small and is not a full application-security ruleset. It looks for shell failure suppression in scripts and pipeline templates. The wrapper now explicitly selects it, rather than fetching an automatically chosen ruleset. Set SEMGREP_CONFIG to an approved local rules directory when integrating an application. Community and commercial analysis capabilities differ; do not assume cross-file coverage from the product name alone. Semgrep scan ordinarily reports findings without necessarily returning a failing status unless error behavior is requested.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-20), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
