# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pySpinW"
copyright = "2026, pySpinW Devs"
author = "pySpinW Devs"
release = "0.0.01"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
]

myst_enable_extensions = [
    "dollarmath",
    "deflist",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "default_mode": "light",
    "logo": {
        "image_light": "_static/img/spinw3_header.png",
        "image_dark": "_static/img/spinw3_header_dark.png",
        "alt_text": "SpinW documentation",
    },
    "navbar_align": "content",
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/SpinW",
            "icon": "fa-brands fa-github",
        },
    ],
    "navigation_depth": 3,
    "show_nav_level": 1,
    "collapse_navigation": False,
    "primary_sidebar_end": [],
}

html_sidebars = {
    "index": [],
    "**": ["sidebar-collapse", "sidebar-nav-bs"],
}

html_static_path = ["_static"]
html_favicon = "_static/favicon.png"
html_css_files = [
    "site.css",
]
