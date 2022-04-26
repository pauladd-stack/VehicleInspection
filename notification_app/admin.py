from django.contrib import admin

from .models import BroadcastNotification, NotifUserStatus
admin.site.register(BroadcastNotification)
admin.site.register(NotifUserStatus)