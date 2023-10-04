from django import template
from menue.models import Menue

register = template.Library()

@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu_recursive(context, path, menu_items, iteration):
    return {'menu_items': menu_items, 'path':path, 'iteration':iteration+1, 'draw_menu_recursive': draw_menu_recursive, 'context': context}