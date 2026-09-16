# Language / Stack Tool Matrix

| Stack | SAST examples | SCA / package audit | Tests | Build/package |
| --- | --- | --- | --- | --- |
| JavaScript / TypeScript | Semgrep, SonarQube, CodeQL | Trivy, npm/pnpm/yarn audit, osv-scanner | Jest, Vitest | npm/pnpm/yarn |
| Java / Kotlin | SonarQube, Semgrep, CodeQL | OWASP Dependency-Check, Trivy, Maven/Gradle ecosystem tools | JUnit | Maven/Gradle |
| Python | Semgrep, Bandit, SonarQube | pip-audit, Trivy, osv-scanner | pytest | pip/Poetry/uv |
| .NET / C# | SonarQube, CodeQL, Roslyn analyzers | NuGet audit/ecosystem tools, Trivy | xUnit/NUnit/MSTest | dotnet |
| Go | gosec, Semgrep, CodeQL | govulncheck, Trivy | go test | go build |
| PHP | Semgrep, SonarQube | Composer audit, Trivy | PHPUnit | Composer |

A mature pipeline generally combines language-aware checks with artifact/image/configuration controls.
