from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def menu_item_title(menu_item):
    str_format = u'{}'
    indicator = menu_item.indicator
    if indicator is not None:
        str_format = u'{}&nbsp;<span>{}</span>'

    return mark_safe(str_format.format(menu_item.title, indicator))
