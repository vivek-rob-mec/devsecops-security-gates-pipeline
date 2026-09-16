#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Repository: $ROOT_DIR"
echo "Git: $(git --version 2>/dev/null || echo not-installed)"
echo "Shell: ${BASH_VERSION:-unknown}"
missing=0
for tool in git gitleaks trivy semgrep; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "MISSING: $tool (see docs/implementation/quickstart.md)" >&2
    missing=1
  fi
done
if [[ "$missing" == 1 ]]; then exit 127; fi
echo "Required source-scan tools found. Image, signing and DAST tools need separate setup."
