from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def nav_active(context, url_name):
    try:
        pattern = reverse(url_name)
    except NoReverseMatch:
        pattern = url_name
    path = context['request'].path
    if pattern == path:
        return 'active'  # Class name to be returned
    return ''
