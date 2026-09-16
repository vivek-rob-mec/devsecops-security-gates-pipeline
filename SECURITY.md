# Security Policy

## Reporting a vulnerability

Do **not** publish exploitable vulnerabilities, real credentials, tokens, private keys, or sensitive scan results in a public issue.

For a real repository, enable **GitHub Private Vulnerability Reporting** and use it for security reports. Include:

- affected component/file/version;
- security impact;
- reproduction steps that are safe and minimal;
- proof/evidence without exposing third-party secrets;
- recommended remediation, if known.

## Supported content

This reference repository contains example policies, scanner configuration, and CI/CD templates. It does not contain a production service. Security issues can still include unsafe scripts, malicious configuration, accidental credentials, dependency risk, or misleading security guidance.

## Secret handling

Never commit real values for:

- cloud access keys;
- GitHub/GitLab tokens;
- registry passwords;
- database passwords;
- signing private keys;
- SSH private keys;
- API tokens;
- production `.env` files.

Use a secret manager or CI secret store and prefer short-lived identity federation where possible.
