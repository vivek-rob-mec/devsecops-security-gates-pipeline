#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"

cat >&2 <<'EOF'
RELEASE BLOCKED: application-specific release verification is not configured.
The scanner wrappers enforce their own thresholds, but this repository cannot
verify your build, tests, authenticated DAST coverage, artifact signature,
provenance, deployment identity or approved exceptions.
Implement those checks using docs/implementation/release-contract.md.
Do not replace this error with a successful echo or suppress its exit status.
EOF
exit 2
