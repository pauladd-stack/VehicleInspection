from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from ajaxnotification_app.models import Notify, NotifUserStatus

def get_notification(request):
	notification =  Notify.objects.order_by('-id')
	filteredlist = []
	notifStatusData = False
	totalUnread = 0
	for notif in notification:
		try:
			notifStatusData = NotifUserStatus.objects.get(user=request.user, notif=notif)
			if notifStatusData:
				notifStatus = True
			else:
				notifStatus = False
		except NotifUserStatus.DoesNotExist:
			notifStatus = False
		
		if notif.driver == request.user:
			if not notifStatus:
				totalUnread+= 1
			filteredlist.append({
				'pk': notif.id,
				'message': notif.message,
				'notifStatus': notifStatus,
				})

	#jsonData = serializers.serialize('json', filteredlist)
	return JsonResponse({'data': filteredlist, 'totalUnread': totalUnread})

def mark_read_notif(request):
	notif=request.GET['notif']
	notif=Notify.objects.get(pk=notif)
	user=request.user

	NotifUserStatus.objects.create(notif=notif, user=user,status=True)
	return JsonResponse({'bool': True})