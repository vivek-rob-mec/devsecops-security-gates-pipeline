# OWASP ZAP

Typical progression:

1. Passive/baseline scan for low-risk adoption.
2. Spider/crawl authenticated and public routes.
3. Active scan in controlled staging.
4. API scan using OpenAPI/GraphQL definitions where supported.
5. Gate on reviewed/high-confidence policy findings.

Do not point active scanners at production by default.

<!-- course-explanation -->
## Working principle and implementation status

**BASELINE.** A short crawl followed by passive checks. Useful for headers and observable response issues.

**FULL SCAN.** Discovery plus active testing. Use controlled scope, test data, rate limits and an authorized environment.

**EXIT STATUS.** Packaged scans distinguish FAIL, WARN and execution errors. Choose an explicit handling policy for each.

The baseline script generally exits 0 on success, 1 for configured FAIL alerts, 2 for WARN alerts without FAILs, and 3 for other failure. The full-scan script adds active scanning. Do not silence these distinctions with shell failure suppression. Keep the ZAP image or version and add-on list with the report. Updating add-ons changes the installed rules; there is no universal ZAP CVE refresh interval. The current project DAST wrapper is an integration stub: it now exits with an error instead of pretending that a scan occurred.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-27), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
