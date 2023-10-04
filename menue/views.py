from django.shortcuts import render


def draw_menu_view(request, menu_path):
        return render(request, 'menue.html')

