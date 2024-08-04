from django import template
from ..models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("main/list_categories.html")
def show_categories(ul_class, cat_selected=0):
    return {
        "categories": Category.objects.filter(parent_id__isnull=True),
        "ul_class": ul_class,
        "cat_selected": cat_selected
        }
