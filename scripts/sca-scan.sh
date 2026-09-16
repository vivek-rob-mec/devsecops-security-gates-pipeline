#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd trivy

trivy fs \
  --config "$ROOT_DIR/configs/trivy/trivy.yaml" \
  --exit-code 1 \
  --scanners vuln \
  --format json \
  --output "$REPORT_DIR/trivy-fs.json" \
  "$ROOT_DIR"

# HIGH/CRITICAL findings block, including findings with no available fix.
