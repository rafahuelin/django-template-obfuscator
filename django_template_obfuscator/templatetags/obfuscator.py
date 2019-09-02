import codecs

from django import template
from django.template.base import Node

register = template.Library()


class ObfuscateNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        processed = codecs.encode(output, 'rot_13')
        return processed


@register.tag
def obfuscate(parser, token):
    nodelist = parser.parse(('endobfuscate',))
    parser.delete_first_token()
    return ObfuscateNode(nodelist)
