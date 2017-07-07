from django import template
from content.models import Portfolio, News

register = template.Library()


@register.simple_tag
def count_portfolio():
    return Portfolio.objects.count()


@register.simple_tag
def count_news():
    return News.objects.count()
