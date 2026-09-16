# Python Example

Suggested sequence:
`locked dependency install → pip-audit/Trivy → Semgrep/Bandit/SonarQube → pytest → package/image → image scan → SBOM → sign → staging → DAST`.

Use isolated virtual environments and lock/constraints appropriate to the chosen packaging tool.
