# Introduction to Real World Data Science

Jupyter Book source and previously published HTML for the Data Science Society at Berkeley DeCal. The original book credits remain in `chapters/intro.md` and `LICENSE.md`.

## Fall 2026 readings

The eight course notebooks from the adjacent `updatedtextbook` repository are in [chapters/fa26](chapters/fa26/index.md). The supplemental Week 2 study-space example and its CSV are in [chapters/03/2](chapters/03/2/pandas-cleaning-eda.ipynb).

## Build and preview locally

Use Python 3.11 in a virtual environment:

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build_book.py
python -m http.server 8765 --bind 127.0.0.1 --directory _build/html
```

Open `http://127.0.0.1:8765/chapters/fa26/index.html`.
After editing content, rerun `python scripts/build_book.py` and refresh the page.

Keep the original Jupyter Book styling. The pinned Sphinx Book Theme 1.0.1 and PyData theme 0.13.3 CSS match the repository's published theme files byte for byte. No custom CSS or theme extension is needed. Jupyter Book 0.15.1 builds with that theme generation. The upstream Data 8 repository has since migrated to Jupyter Book 2; merging upstream would be a separate migration, not a content-only update.

Use the build script rather than building directly at the repository root. This repository contains both source content and old published HTML/assets; Jupyter Book otherwise mistakes the old `_static` files for custom styles and mixes them with its theme. The script stages only sources in a temporary directory and writes the preview to `_build/html`, leaving published files untouched. If switching from a different toolchain, move the old `_build` directory aside first and clear the browser's cached site assets.

Notebook execution remains disabled during builds: execute changed notebooks and save their outputs before building. Their CSV files must remain alongside them.

The existing book produces warnings about older chapters absent from the table of contents and some old heading levels. These chapters are retained. Check that no new warning refers to the page you edited, that its local links resolve, and that its displayed numerical results match execution.

## Publishing after review

**Ask for confirmation before pushing.** There are two repositories involved: `dssdecal/textbook` for the reading and `dssdecal/fa26` for the schedule link.

This checkout contains previously generated HTML at the repository root and no build workflow. Editing notebook sources alone does not update those HTML pages. Before publishing, verify the repository's GitHub Pages configuration, then either prepare an overlay of `_build/html/` into the existing published tree or configure an approved build-and-deploy workflow. Preserve old published pages and assets; do not delete chapters or replace the repository with build output.

Publish and verify the Fall 2026 chapter pages under `https://dssdecal.org/textbook/chapters/fa26/` before switching the course schedule links in `dssdecal/fa26`. The supplemental Week 2 example has its own URL:

`https://dssdecal.org/textbook/chapters/03/2/pandas-cleaning-eda.html`

The preview is local only. No deployment settings, branches, or remote content have been changed for this draft.
