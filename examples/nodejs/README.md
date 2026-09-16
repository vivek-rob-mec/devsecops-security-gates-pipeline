# Node.js / TypeScript Example

Suggested sequence:
`npm ci → secret scan → npm/ecosystem audit + Trivy SCA → Semgrep/SonarQube → Jest/Vitest → build → image scan → SBOM → sign → staging → ZAP/API tests → production`.

Prefer deterministic lockfiles and do not use `npm install` in CI when `npm ci` is appropriate.
