# character_sheet/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def attr(obj, attr_name):
    """Get an attribute of an object dynamically."""
    return getattr(obj, attr_name, False)
