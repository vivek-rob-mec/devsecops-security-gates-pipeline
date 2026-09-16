#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
REPORT_DIR="${REPORT_DIR:-$ROOT_DIR/reports/generated}"
cd "$ROOT_DIR"
mkdir -p "$REPORT_DIR"

require_image_digest() {
  if [[ ! "${IMAGE_REF:-}" =~ ^[^[:space:]@]+@sha256:[a-f0-9]{64}$ ]]; then
    echo "ERROR: IMAGE_REF must be a registry image pinned as repository@sha256:<64 lowercase hex characters>." >&2
    exit 2
  fi
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "ERROR: required command '$1' was not found." >&2
    exit 127
  fi
}
