from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords


User = get_user_model()

class Equipment(models.Model):
	EQUIPMENT_TYPE_CHOICES = (
        ('TCK', 'Truck'),
        ('TR', 'Trailer'),
    )
	id = models.BigAutoField(primary_key=True)
	equipment = models.IntegerField('Equipment Number', default="Null")
	equipment_type = models.CharField(max_length=3, choices=EQUIPMENT_TYPE_CHOICES, default="TRK")
	date = models.DateField('Date')
	driver = models.ForeignKey(User, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.equipment_type + " " + str(self.equipment)