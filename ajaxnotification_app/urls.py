from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [    
path('get_notification', views.get_notification, name="get_notification"),
path('mark_read_notif', views.mark_read_notif, name="mark_read_notif"),
]
