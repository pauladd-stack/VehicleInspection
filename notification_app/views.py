from django.shortcuts import render, redirect, HttpResponse
from channels.layers import get_channel_layer
from .models import BroadcastNotification, NotifUserStatus
from django.http import JsonResponse



from asgiref.sync import async_to_sync
def test(request):
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)(
		"notification_"+str(request.user.id),{
		
		'type': 'send_notification',
		'message': 'Test'
		}
		
	)
	return HttpResponse("Done")

def get_notification(request):
	notification =  BroadcastNotification.objects.order_by('-id')
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
	notif=BroadcastNotification.objects.get(pk=notif)
	user=request.user

	NotifUserStatus.objects.create(notif=notif, user=user,status=True)
	return JsonResponse({'bool': True})

def mark_not_read_notif(request):
	notif=request.GET['notif']
	
	notif=BroadcastNotification.objects.get(pk=notif)
	user=request.user
	print("MARKMOTREAK"+str(notif))
	NotifUserStatus.objects.filter(notif=notif, user=user,status=True).delete()
	#NotifUserStatus.objects.remove(notif=notif, user=user,status=False)
	return JsonResponse({'bool': False})