from django import template
from content.models import Portfolio

register = template.Library()


@register.simple_tag
def count_portfolio():
    return Portfolio.objects.indicator()
