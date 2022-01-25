from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords


User = get_user_model()

class VehicleInspectionReport(models.Model):
	id = models.BigAutoField(primary_key=True)
	driver = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField('Date')
	truck = models.CharField('Truck Number', max_length=120)
	
	assignedMech = models.CharField('Assigned Mechanic', max_length=120, default="")
	repairStatus = models.BooleanField(default=False)

	lastUpdatedUser = models.DateTimeField(blank=True, null=True)  
	lastUpdatedMech = models.DateTimeField(blank=True, null=True)  




	engine_check = models.BooleanField(default=False)
	engine_desc = models.CharField('Engine Description', max_length=240, default="")
	engine_fix = models.CharField('Engine Fix', max_length=240, default="")

	history = HistoricalRecords()
	#python manage.py clean_old_history --days 1 --auto
	@property
	def _history_user(self):
		return self.changed_by

	@_history_user.setter
	def _history_user(self, value):
		self.changed_by = value

	def __str__(self):
		return self.truck





