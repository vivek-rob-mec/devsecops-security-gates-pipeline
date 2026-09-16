# Java / Spring Example

Suggested sequence:
`Maven/Gradle dependency resolution → OWASP Dependency-Check/Trivy → SonarQube/Semgrep/CodeQL → JUnit → package JAR → image scan → SBOM → sign → staging → DAST`.

Keep vulnerability databases and Maven/Gradle plugin versions managed centrally.
