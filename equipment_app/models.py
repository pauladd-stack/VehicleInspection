from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords



User = get_user_model()

class Equipment(models.Model):
	EQUIPMENT_TYPE_CHOICES = (
        ('Truck', 'Truck'),
        ('Trailer', 'Trailer'),
    )
	id = models.BigAutoField(primary_key=True)

	equipment = models.IntegerField('Equipment Number', default="Null")
	equipment_type = models.CharField(max_length=20, choices=EQUIPMENT_TYPE_CHOICES, default="Truck")
	date = models.DateField('Date')
	driver = models.ForeignKey(User, on_delete=models.CASCADE)
	mileage = models.IntegerField(default="0")
	predicted_mileage = models.IntegerField(default="0")
	

	def __str__(self):
		return self.equipment_type + " " + str(self.equipment)