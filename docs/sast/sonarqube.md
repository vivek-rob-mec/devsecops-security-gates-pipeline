# SonarQube

SonarQube can combine static-analysis findings with maintainability and quality metrics. Treat the **Quality Gate** as policy and tune it for new code so legacy technical debt does not make adoption impossible.

Never store a Sonar token in `sonar-project.properties`; inject it through the CI secret mechanism.

<!-- course-explanation -->
## Working principle and implementation status

**CODEQL.** Extracts a database representing source. Security queries analyze the code model and may return data-flow paths.

**SONARQUBE.** Analyzers apply language rules. Quality profiles choose active rules; quality gates evaluate configured metrics.

**INTEGRATION.** Match analyzer support to the language and build. Retrieve the final gate result; scanner upload success is insufficient.

CodeQL creates a database from the target code and runs query suites against it; this database is not an NVD copy. Query-pack and analyzer updates affect coverage. SonarQube receives analyzer results and applies server-side configuration; a security hotspot may need human review rather than representing a confirmed vulnerability. Plugin, server and edition capabilities matter. Both tools need a functioning analysis integration and an enforced result in CI. This repository has guidance and an example Sonar configuration, but no complete server or CodeQL setup.

Read the [complete lesson and primary sources](../DEVSECOPS_HANDBOOK.md#lesson-21), [data/update matrix](../DETECTION_AND_DATA.md) and [implementation quickstart](../implementation/quickstart.md).
<!-- /course-explanation -->
