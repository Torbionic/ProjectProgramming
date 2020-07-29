from django import template

register = template.Library()

from ..models import Blog


@register.simple_tag
def total_posts():
    return Blog.objects.count()
