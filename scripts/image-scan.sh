#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd trivy

require_image_digest
trivy image --config "$ROOT_DIR/configs/trivy/trivy.yaml" --scanners vuln \
  --exit-code 1 --format json --output "$REPORT_DIR/trivy-image.json" "$IMAGE_REF"
