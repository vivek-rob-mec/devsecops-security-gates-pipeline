#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd semgrep

semgrep scan \
  --config "${SEMGREP_CONFIG:-$ROOT_DIR/configs/semgrep/semgrep.yml}" \
  --error --strict --metrics off \
  --exclude .tools --exclude reports/generated \
  --sarif \
  --output "$REPORT_DIR/semgrep.sarif" \
  "$ROOT_DIR"
