from django.contrib import admin
from django.urls import path, include
from . import views
from .views import user_list

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('admin_area', views.admin_area, name="admin_area"),
    path('register_user', views.register_user, name="register_user"),
    path('user_list', user_list.as_view(), name="user_list"),
    path('update_user/<user_id>', views.update_user, name="update_user"),

    
]
