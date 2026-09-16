#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"

: "${DAST_TARGET_URL:?Set DAST_TARGET_URL to an EXPLICITLY AUTHORIZED staging/test target}"

cat <<EOF
DAST target: $DAST_TARGET_URL
This wrapper intentionally does not auto-launch an active scanner.
Integrate your approved OWASP ZAP deployment here after defining authentication,
rate limits, exclusions, test data, and authorization.
EOF
echo "DAST NOT RUN: configure and validate the scanner integration before this gate can pass." >&2
exit 2
