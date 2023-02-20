from django.contrib import admin
from .models import Photographs

# Register your models here.


class PhotographAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category", )
    list_editable = ("published", )
    list_per_page = 10


admin.site.register(Photographs, PhotographAdmin)