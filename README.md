# SpinW Sphinx Docs

This repository builds a Sphinx documentation site for SpinW, pySpinW, and
SpinWcore, managed with `uv`.

## Specs

- Python 3.12, dependency management via `uv` (`uv sync`).
- Source directory: `docs/` · Entry page: `docs/index.rst` · Config file: `docs/conf.py`.
- Theme: `pydata_sphinx_theme==0.18.0`; Markdown authoring via `myst-parser>=4`.
- `pyspinw` is configured as an editable local dependency at `../pySpinW`
  (see `pyproject.toml`); the sibling checkout must exist and be importable
  for the API reference page to render.
- Extensions:
  - `sphinx.ext.autodoc` + `sphinx.ext.autosummary` + `sphinx.ext.napoleon` —
    generate the pySpinW API reference from docstrings.
  - `sphinx.ext.mathjax` — renders spin Hamiltonian equations.
  - `myst_parser` (with `dollarmath` and `deflist`) — lets Markdown sources use
    LaTeX-style math and definition lists alongside reST.

Build commands:

```bash
uv sync
uv run sphinx-build -M html docs docs/_build   # or `make html` from docs/
```

Serve the built site locally:

```bash
uv run python -m http.server --directory docs/_build/html 8000
```

Clean generated output: `make clean` (from inside `docs/`).

## Customization

- `pydata_sphinx_theme` options (`docs/conf.py`): light/dark logo swap,
  centered navbar with a theme switcher and GitHub icon link, persistent
  search, 3-level collapsible sidebar navigation, and no sidebar on the
  homepage.
- Custom CSS (`docs/_static/site.css`) styles homepage-specific elements on
  top of the theme defaults:
  - `project-cards` / `project-card` grid for the project tiles, with hover states
  - `project-logo` and `project-badges` layout inside each card
  - `partner-table` / `partner-logo` sizing for the partner logo grid
  - navbar spacing tweaks (`.bd-navbar-elements.navbar-nav`)
- Favicon: `docs/_static/favicon.png`.

## Key features

- **Homepage** with three project cards — SpinW (MATLAB), pySpinW (Python),
  and SpinWcore (C++) — each with live GitHub fork/star badges.
- **SpinW (MATLAB) docs** (`docs/spinw/`): installation, 31 tutorials, class
  and properties reference, and namespace references for `methods`, `files`,
  `plot`, `pref`, and `sym`.
- **pySpinW (Python) docs** (`docs/pyspinw/`): installation, an overview with
  the spin Hamiltonian rendered via MathJax, example scripts, and an
  autodoc-generated API reference (`docs/api/pySpinW.rst`).
- **Resources** (`docs/resources/`): FAQ, citation info (DOI plus a live
  citation-count badge), presentations, and contact details.
- **News** (`docs/news_posts/`): dated announcement and workshop posts.
