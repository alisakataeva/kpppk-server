from django.contrib import admin

from .models import SiteSetting, News, Program, Page


# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(News)
admin.site.register(Program)
admin.site.register(Page)