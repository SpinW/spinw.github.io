"""
A Sphinx Extension to add an html anchor tag with link.
Used to make a project card into a clickable link as described here:
https://stackoverflow.com/questions/796087/make-a-div-into-a-link
"""

from docutils.nodes import Element, SkipNode
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


class AnchorLinkNode(Element):
    """A custom html anchor tag with link using the anchor-link css class"""
    def html(self):
        return f'<a href="{self["link"]}"><span class="anchor-link"></span></a>\n'


def write_html(self, node):
    self.body.append(node.html())
    raise SkipNode


class AnchorLinkDirective(SphinxDirective):
    """A Sphinx Extension to add an html anchor tag with link."""

    required_arguments = 1

    def run(self):
        return [AnchorLinkNode(link=self.arguments[0])]


def setup(app):
    app.add_node(AnchorLinkNode, html=(write_html, None))
    app.add_directive('anchor_link', AnchorLinkDirective)
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
