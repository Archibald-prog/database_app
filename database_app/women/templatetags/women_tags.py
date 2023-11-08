from django import template
from women.models import Category

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if filter is None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}



