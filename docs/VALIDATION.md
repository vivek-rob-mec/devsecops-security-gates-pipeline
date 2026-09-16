# Validation of the revision

Validation performed locally on Windows with Python 3.14 and Git Bash. No real security scanner, signing operation, remote CI job, active DAST target or production deployment was executed.

## Checks performed

| Check | Result and interpretation |
| --- | --- |
| Offline wrapper regression suite | 12 test methods passed, including multiple finding/error/reference subcases. Controlled fake tools verify wrapper arguments and exit-status propagation. |
| Markdown formatting | markdownlint-cli2 0.23.2 checked 126 files; 278 spacing/table-style issues were fixed across 54 files; final result: zero issues. |
| Script syntax | Bash syntax parsed for the project's shell wrappers. |
| Structured configuration | JSON/SARIF, TOML, XML and available YAML files parsed successfully. This checks syntax, not each vendor's full configuration schema. |
| Documentation navigation | Local Markdown file links checked. Remote-source availability and Markdown fragment links are not continuously tested by this validator. |
| PowerPoint package | ZIP integrity and all XML/relationship files parsed. |
| Presentation layout | 57 slides and 690 text boxes passed shared-builder bounds checks; overflow/out-of-slide positions are rejected. |
| Visual inspection | Contact-sheet preview and representative full-size PDF-layout slides inspected. |
| Original preservation | Original source deck retained; previous expanded deck copied to a separately named backup before replacement. |

## Reproduce

```powershell
python -m unittest discover -s tests -v
python scripts/validate_repository.py
python presentation/build_presentation.py
python scripts/update_manifest.py
```

The presentation builder needs `presentation/requirements.txt`. YAML syntax checking requires PyYAML; the validator explicitly reports if YAML or Bash checks are skipped. The wrapper tests require Bash and report a skip if unavailable. The tests are separate from live scanner acceptance testing.

Markdown formatting was checked with `npx.cmd --offline markdownlint-cli2 '**/*.md' '#.tools/**' '#presentation/preview/**'` after installing the linter; use `npx` on Linux/macOS. The manifest checker validates the current distributable file hashes and sizes; after reviewed changes, use `--write` to refresh it.

## Presentation verification limits

The PDF and previews use the same text, font measurements and geometry as the PPTX builder. They are **not Microsoft PowerPoint renders**. Native PowerPoint and LibreOffice were unavailable here. Font substitution and application-specific typography can change rendering elsewhere; the editable deck specifies Arial, while the PDF embeds the corresponding font data. All deep explanations are in speaker notes and the offline handbook.

## Production verification still required

- Install reviewed scanner versions and test that real vulnerable and clean fixtures yield the intended results.
- Confirm supported file formats, package discovery, analyzer coverage and rule severity mappings.
- Exercise stale database, failed refresh, incomplete reports and wrong artifact identities.
- Configure and test authenticated DAST/API coverage on an authorized staging deployment.
- Verify signing identity, provenance and the exact artifact promoted between jobs/environments.
- Implement and test protected approval/exception processing and deployment enforcement.

These are application integration requirements, not claims made by the local checks. The [project review](PROJECT_REVIEW.md) records their current status.
