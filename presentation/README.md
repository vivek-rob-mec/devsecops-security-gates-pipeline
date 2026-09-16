# Presentation and offline course

- [DevSecOps_Industry_Standard_Pipeline.pptx](DevSecOps_Industry_Standard_Pipeline.pptx) — rebuilt editable course, with detailed speaker notes.
- [DevSecOps_Industry_Standard_Pipeline.pdf](DevSecOps_Industry_Standard_Pipeline.pdf) — matching slide layout for convenient reading.
- [Offline handbook](../docs/DEVSECOPS_HANDBOOK.md) — slide content, full explanations and source links.
- [Browser-readable handbook](../docs/DEVSECOPS_HANDBOOK.html) — the same course as a standalone offline web page.
- [Slide index](slide-index.md) — numbered learning sequence.
- `source-original/DevSecOps_Industry_Standard_Pipeline.before-revision.pptx` — backup of the previous expanded deck.
- `source-original/SCA_SAST_DAST.pptx` — original source deck retained for traceability.

When changing the presentation, keep the Markdown documentation authoritative for implementation details because it is easier to review, diff, and maintain in Git.

## Structure

Foundations → four-phase flow → detection principles → advisory data and updates → findings and gates → project implementation → operation and review. Beginners can follow the sequence; intermediate and professional readers can use the implementation sections and full notes.

The slides use consistent typography, explicit line breaks, editable text/shapes, concise visible explanations, and deeper speaker notes. The original filename is retained, but the content correctly describes a reference architecture rather than a universally mandated industry standard.

## Rebuild

Requires Python 3.11 or later and the packages in `requirements.txt`. From the repository root:

```powershell
python -m pip install --target .tools/python -r presentation/requirements.txt
python presentation/build_presentation.py
python scripts/update_learning_links.py
```

Edit `course_content.py` for lesson content and sources; edit `build_presentation.py` for layout. Rebuilding updates the PPTX, PDF, handbook and index. The first rebuild preserves the previous expanded deck if its backup is absent. The builder measures every text box and fails on overflow. It writes a contact sheet and layout report under ignored `presentation/preview/`.

After reviewing regenerated deliverables, refresh the distribution inventory with `python scripts/update_manifest.py --write`. Running the command without `--write` checks existing hashes. Local tools, temporary reports and previews are excluded.

The PDF is generated from the shared layout model, not by Microsoft PowerPoint. Its fonts are embedded; the editable PPTX specifies Arial (or DejaVu Sans on supported Linux builds) without embedding fonts. Native PowerPoint rendering was unavailable in this environment, so font substitution may affect appearance on another machine. Full notes are in the handbook; the slide PDF does not include notes pages.
