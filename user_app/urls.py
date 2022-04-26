from django.contrib import admin
from django.urls import path, include
from . import views
from .views import user_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register_user', views.register_user, name="register_user"),
    path('user_list', user_list.as_view(), name="user_list"),
    path('update_user/<user_id>', views.update_user, name="update_user"),
    path('delete_user/<user_id>', views.delete_user, name="delete_user"),
    path('change_password/<user_id>', views.change_password, name="change_password"),
    path('delete_report/<str:report_id>', views.delete_report, name="delete_report"),
    path('report_csv', views.report_csv, name="report_csv"),
    path('report_pdf', views.report_pdf, name="report_pdf"),

    
]
