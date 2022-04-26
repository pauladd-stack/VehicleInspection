from django import template
import datetime
from django.contrib.auth import get_user_model
from notification_app.models import BroadcastNotification
from django.core import serializers
from driver_app.models import VehicleInspectionReport


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


@register.filter(name='prev')
def prev(passed):
    print("passed", passed)
    report = VehicleInspectionReport.objects.all()
    prev_el = 0
    curr_el = 0
    next_el = 0
    for index, elem in enumerate(report):
        if(len(report) > 3):
            if (passed == elem.id):
                if (index+1 < len(report) and index - 1 < 0):
                    prev_el = str(elem.id)
                    curr_el = str(elem.date)
                    next_el = str(report[index+1].id)
                    #print("previous Element:",prev_el,"\n", "current Element:",curr_el, "\n\n\n\n")

                elif (index+1 < len(report) and index - 1 >= 0):
                    prev_el = str(report[index-1].id)
                    curr_el = str(elem.date)
                    next_el = str(report[index+1].id)
                   # print("previous Element:",prev_el,"\n", "current Element:",curr_el, "\n\n\n\n")

                elif (index+1 >= len(report) and index - 1 >= 0):
                    prev_el = str(report[index-1].id)
                    curr_el = str(elem.date)
                    next_el = str(elem.id)
                    #print("previous Element:",prev_el,"\n", "current Element:",curr_el, "\n\n\n\n")
                print("previous Element:",prev_el,"\n", "current Element:",curr_el, "\n\n\n\n")

    return report