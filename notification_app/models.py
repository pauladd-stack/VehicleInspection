from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class BroadcastNotification(models.Model):
	message = models.TextField()
	date = date = models.DateField('Date')
	driver = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.message)

	def save(self, *args, **kwargs):
		super(BroadcastNotification, self).save(*args, **kwargs)
		channel_layer = get_channel_layer()
		message=self.message
		async_to_sync(channel_layer.group_send)(
			str(self.driver.id),{
			'type': 'send_notification',
			'value':json.dumps({'message':message}),
			}
			
		)


'''
@receiver(post_save, sender = BroadcastNotification)
def notification_handler(sender, instance, created, **kwargs):
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)(
		str(instance.driver.id),{
		
		'type': 'send_notification',
		'message':instance.message,
		}
		
	)'''

class NotifUserStatus(models.Model):
	notif=models.ForeignKey(BroadcastNotification, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)
