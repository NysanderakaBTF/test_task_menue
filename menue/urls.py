# myapp/urls.py
from django.urls import path
from .views import draw_menu_view

urlpatterns = [
    path('<path:menu_path>/', draw_menu_view, name='draw_menu'),
]
