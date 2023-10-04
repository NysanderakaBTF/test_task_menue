from django.shortcuts import render
from django.views import generic

from menue.models import Menue
from menue.templatetags.draw_menu import draw_menu


def draw_menu_view(request, menu_path):
        return render(request, 'menue.html', {'main_menu': menu_path})


# myapp/views.py
# from django.shortcuts import render
# from .templatetags.draw_menu import draw_menu
#
# def draw_menu_view(request, menu_name):
#     return render(request, 'draw_menu.html', {'main_menu': draw_menu(menu_name)})
