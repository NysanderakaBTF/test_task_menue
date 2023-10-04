from django import template

from menue.models import Menue

register = template.Library()


@register.inclusion_tag('draw_menu.html')
def draw_menu(url_string):
    m_item_path = url_string.split("/")

    #
    # query = (f"WITH RECURSIVE x AS ("
    #          f"SELECT * FROM menue_menue WHERE menue_menue.title LIKE \'{m_item_path[0]}\' "
    #          f"UNION "
    #          f"SELECT * FROM menue_menue as m INNER JOIN x x1 ON m.parent_id = x1.id "
    #          f")"
    #          f"SELECT * FROM x;")

    query = (
        f"WITH RECURSIVE x AS ("
        f"    SELECT id, title, parent_id, url FROM menue_menue WHERE menue_menue.title LIKE '{m_item_path[0]}' "
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

    return {'menu_items':res, 'path':m_item_path, 'iteration':0}


    # menu_items = Menue.objects.filter(parent__isnull=True, title=m_item_path[0]).prefetch_related('children').first()
    # items = {
    #     'title': menu_items.title,
    #     "url": menu_items.url,
    #     'children': []
    # }
    # i_c = items
    # index = 0
    # for child in i_c['children']:
    #     if child['title'] == m_item_path[0]:
    #         break
    #     index += 1
    # if index < len(i_c['children']):
    #     i_c = i_c['children'][index]
    #
    #
    # m_item_path = m_item_path[1:]
    #
    # if len(m_item_path) > 0:
    #
    #     menu_items = menu_items.children.filter(title__iexact=m_item_path[0]).first()
    #
    #
    # def get_children_recursive(menu_item, i_c1, m_item_path1):
    #
    #     print(i_c1)
    #     print(m_item_path1)
    #     print(menu_item)
    #
    #     curr_children = menu_item.children.all()
    #     if not curr_children:
    #         return
    #     if len(m_item_path1)==0:
    #         return
    #     for child in curr_children:
    #         i_c1['children'].append({
    #             'title': child.title,
    #             "url": child.url,
    #             'children': []
    #         })
    #
    #
    #     index = 0
    #     m_item_path1 = m_item_path1[1:]
    #
    #
    #     if len(m_item_path1) == 0:
    #         return
    #
    #
    #
    #     for child in i_c1['children']:
    #         if child['title'] == m_item_path1[0]:
    #             break
    #         index +=1
    #     if index == len(i_c1['children']):
    #         return
    #
    #
    #     print(index)
    #     print(i_c1)
    #     print(m_item_path1)
    #     print(menu_item)
    #     i_c1 = i_c1['children'][index]
    #
    #     menu_item = menu_item.children.all().filter(title__iexact=m_item_path[0])
    #
    #     get_children_recursive(menu_item, i_c1, m_item_path1)
    #
    # get_children_recursive(menu_items, i_c, m_item_path)
    # return {'menu': shit}

# myapp/templatetags/menu_tags.py
# from django import template
# from menue.models import Menue
#
# register = template.Library()
#
# @register.inclusion_tag('draw_menu.html')
# def draw_menu(menu_name):
#     menu_items = Menue.objects.filter(parent__isnull=True, title=menu_name).prefetch_related('children').first()
#     return {'menu_items': menu_items}
#

