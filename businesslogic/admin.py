from django.contrib import admin

from .models import SiteSetting, News, Program, Page, File, Feedback


# Filtering, sorting


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "url", "group_name"]
    list_filter = ["group_name"]


class FileAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["created_at", "email", "name", "message", "is_completed"]
    list_filter = ["is_completed"]


# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(News)
admin.site.register(Program)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(File, FileAdmin)
