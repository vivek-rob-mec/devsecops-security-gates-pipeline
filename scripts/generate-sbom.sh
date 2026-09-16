#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"

require_image_digest
if command -v syft >/dev/null 2>&1 && [[ -n "$IMAGE_REF" ]]; then
  syft "$IMAGE_REF" -o cyclonedx-json="$REPORT_DIR/sbom.cdx.json"
elif command -v trivy >/dev/null 2>&1 && [[ -n "$IMAGE_REF" ]]; then
  trivy image --format cyclonedx --output "$REPORT_DIR/sbom.cdx.json" "$IMAGE_REF"
else
  echo "Set IMAGE_REF and install syft or trivy to generate an SBOM." >&2
  exit 127
fi
