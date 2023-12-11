from django import template
from django.templatetags.static import PrefixNode

register = template.Library()

@register.simple_tag
def app_media_prefix(app_name, path):
    return PrefixNode.handle_simple("media/" + app_name + "/" + path)