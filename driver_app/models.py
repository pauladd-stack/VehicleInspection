from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VehicleInspectionReport(models.Model):
	id = models.BigAutoField(primary_key=True)
	driver = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField('Date')
	truck = models.CharField('Truck Number', max_length=120)

	def __str__(self):
		return self.truck




