#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd cosign

require_image_digest

echo "Use an approved keyless/workload-identity or protected-key signing configuration."
cosign sign "$IMAGE_REF"
