from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notify(models.Model):
	message = models.TextField()
	date = date = models.DateField('Date')
	driver = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.message)

class NotifUserStatus(models.Model):
	notif=models.ForeignKey(Notify, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)

