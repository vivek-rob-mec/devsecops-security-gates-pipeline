#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd trivy

trivy config \
  --config "$ROOT_DIR/configs/trivy/trivy.yaml" \
  --exit-code 1 \
  --format json \
  --output "$REPORT_DIR/trivy-config.json" \
  "$ROOT_DIR"
