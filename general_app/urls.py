from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pricing', views.pricing, name="pricing"),
    path('features', views.features, name="features"),
    path('support', views.support, name="support"),
   
]
