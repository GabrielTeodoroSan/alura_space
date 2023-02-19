from django.contrib import admin
from .models import Photographs

# Register your models here.


class PhotographAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "legend")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(Photographs, PhotographAdmin)