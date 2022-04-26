from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('profile/<user_id>', views.user_profile, name="user_profile"),
    path('dashboard', views.dashboard, name="dashboard"),
    
    
]