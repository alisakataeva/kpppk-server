from django.contrib import admin

from .models import SiteSetting, News, Program, Page, File


# Filtering, sorting


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "url", "group_name"]
    list_filter = ["group_name"]


class FileAdmin(admin.ModelAdmin):
    list_display = ["category", "name"]
    list_filter = ["category"]


# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(News)
admin.site.register(Program)
admin.site.register(Page, PageAdmin)
admin.site.register(File, FileAdmin)
