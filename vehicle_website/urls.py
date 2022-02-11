from django.contrib import admin
from django.urls import path, include
from user_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('general_app.urls')),
    path('', include('login_app.urls')),
    path('administrator/', include('user_app.urls')),
    path('driver/', include('driver_app.urls')),
    path('mechanic/', include('mechanic_app.urls')),
    path('equipment/', include('equipment_app.urls')),
]

handler404 = 'general_app.views.handler404'
handler500 = 'general_app.views.handler500'
handler403 = 'general_app.views.handler403'
handler400 = 'general_app.views.handler400'
