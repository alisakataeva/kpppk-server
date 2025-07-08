"""API URL configuration"""

from django.urls import path, include, re_path
from mysite import views


#


urlpatterns = [
    path('blank/', views.blank),

]
