from django.contrib import admin

from menue.models import Menue


# Register your models here.
@admin.register(Menue)
class Menue_Admin(admin.ModelAdmin):
    pass