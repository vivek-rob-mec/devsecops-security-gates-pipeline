SHELL := /bin/bash

.PHONY: help validate secret-scan sca sast iac security

help:
	@echo "Targets: validate secret-scan sca sast iac security"

validate:
	@bash scripts/preflight.sh

secret-scan:
	@bash scripts/secret-scan.sh

sca:
	@bash scripts/sca-scan.sh

sast:
	@bash scripts/sast-scan.sh

iac:
	@bash scripts/iac-scan.sh

security: secret-scan sca sast iac
