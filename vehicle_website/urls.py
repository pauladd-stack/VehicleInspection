from django.contrib import admin
from django.urls import path, include
from user_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('user_app.urls')),
]
