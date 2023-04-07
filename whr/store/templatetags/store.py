from django import template

register = template.Library()


@register.simple_tag
def abs_tag(text):
    return abs(text)