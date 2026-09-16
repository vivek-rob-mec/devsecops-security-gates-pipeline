#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib/common.sh"
require_cmd gitleaks

gitleaks dir "$ROOT_DIR" \
  --config "$ROOT_DIR/configs/gitleaks/.gitleaks.toml" \
  --redact \
  --report-format sarif \
  --report-path "$REPORT_DIR/gitleaks.sarif"

# The worktree scan also works in downloaded ZIPs. Scan history when available.
if git -C "$ROOT_DIR" rev-parse --git-dir >/dev/null 2>&1; then
  gitleaks git "$ROOT_DIR" --log-opts="--all" \
    --config "$ROOT_DIR/configs/gitleaks/.gitleaks.toml" --redact \
    --report-format sarif --report-path "$REPORT_DIR/gitleaks-history.sarif"
fi
