from django import template
from ..models import Category


register = template.Library()

@register.inclusion_tag("main/list_categories.html")
def show_categories(ul_class, cat_selected=0):
    cats = Category.objects.all()
    return {
        "categories": cats,
        "ul_class": ul_class,
        "cat_selected": cat_selected
        }
