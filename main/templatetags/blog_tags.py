from django import template
from ..models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("main/list_categories.html")
def show_categories(ul_class):
    return {
        "categories": Category.objects.all(),
        "ul_class": ul_class
        }
