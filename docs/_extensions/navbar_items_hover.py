"""
A pydata-sphinx-theme specific extension which overrides the top navbar to show
sub-menu items when users hover over the main menu item like in Jekyll
"""

from functools import cache
from pydata_sphinx_theme.utils import traverse_or_findall
from pydata_sphinx_theme.toctree import add_inline_math
from sphinx.addnodes import toctree as TocTreeNodeClass
from docutils import nodes

def dropdown_nav_bar(app, pagename, templatename, context, doctree):
    """Overrides the pydata-sphinx-theme toctree-generator navbar to have hover dropdown menus"""

    @cache
    def _get_toc_children(toc_root):
        rv = []
        for toc in traverse_or_findall(app.env.tocs[toc_root], TocTreeNodeClass):
            for title, page in toc.attributes['entries']:
                page = toc.attributes['parent'] if page == 'self' else page
                if title is None:
                    title = "".join([add_inline_math(node) if isinstance(node, nodes.math) else node.astext()
                                     for node in app.env.titles[page].children])
                rv.append([title, page])
        return rv

    original_header = context.get("generate_header_nav_html")

    if original_header is not None:

        @cache
        def generate_header_nav_html(*args, **kwargs):
            navheader = original_header(*args, **kwargs)
            sections = _get_toc_children(app.config.root_doc)
            for title, page in sections:
                splits = navheader.split(title)
                if len(splits) > 1 and 'nav-item dropdown' not in splits[0]:
                    subitems = [f'<li><a href="{context["pathto"](pp)}">{ti}</a></li>' for ti, pp in _get_toc_children(page)]
                    childtext = '\n<ul class="nav-item-children">' + '\n  '.join(subitems) + '\n</ul>\n'
                    asplit = splits[1].split('</a>')
                    navheader = splits[0] + title + asplit[0] + '</a>' + childtext + '</a>'.join(asplit[1:])
            return navheader

        context['generate_header_nav_html'] = generate_header_nav_html


def setup(app):
    app.connect("html-page-context", dropdown_nav_bar, priority=999)
