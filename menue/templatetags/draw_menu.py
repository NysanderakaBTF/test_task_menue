from django import template

from menue.models import Menue

register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, url_string):
    m_item_path = url_string


    query = (
        f"WITH RECURSIVE x AS ("
        f"    SELECT id, title, parent_id, url FROM menue_menue WHERE menue_menue.title LIKE '{m_item_path}' "
        f"    UNION "
        f"    SELECT m.id, m.title, m.parent_id, m.url FROM menue_menue m INNER JOIN x x1 ON m.parent_id = x1.id "
        f")"
        f"SELECT * FROM x;"
    )

    shit = Menue.objects.raw(query)

    print(shit)
    res = []
    for p in shit:
        print(p)
        res.append(p)
    print(context.get('request').path)
    return {'menu_items':res, 'path':context.get('request').path.split('/')[1:], 'iteration':0}
