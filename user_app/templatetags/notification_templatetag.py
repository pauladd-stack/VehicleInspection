from django import template
import datetime
from django.contrib.auth import get_user_model
from notification_app.models import BroadcastNotification
from django.core import serializers


User = get_user_model()



register = template.Library()

@register.filter(name='get_notification')
def get_notification(request):
    notification = BroadcastNotification.objects.order_by('-id')
    filteredlist = []

    for notif in notification:
        #if notif.driver == noti:
        filteredlist.append(notif.message)

    return filteredlist

'''
@register.filter(name='get_time')
def get_time(time):
    today = datetime.date.today()
    start = today - datetime.timedelta(days=today.weekday())
    end = start + datetime.timedelta(days=6)
    return start
'''


