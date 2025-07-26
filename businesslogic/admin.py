from django.contrib import admin

from .models import SiteSetting, News, Program


# Register your models here.


admin.site.register(SiteSetting)
admin.site.register(News)
admin.site.register(Program)