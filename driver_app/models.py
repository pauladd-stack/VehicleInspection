from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords
from equipment_app.models import Equipment


User = get_user_model()

class VehicleInspectionReport(models.Model):

	LIGHT_CHOICES = (
		('R', 'Running'),
		('S', 'Signal'),
		('B', 'Brakes'),
	)
	EMERGENCY_CHOICES = (
		('AID', 'First Aid'),
		('EXT', 'Fire Extinguisher'),
		('TRI', 'Triangles'),
	)


	id = models.BigAutoField(primary_key=True)
	driver = models.ForeignKey(User, on_delete=models.CASCADE)
	equipment = models.CharField('Equipment', max_length=120, default="")
	date = models.DateField('Date')
	
	assignedMech = models.CharField('Assigned Mechanic', max_length=120, default="")
	repairStatus = models.BooleanField(default=False)

	lastUpdatedUser = models.DateTimeField(blank=True, null=True)  
	lastUpdatedMech = models.DateTimeField(blank=True, null=True)  




	engine_check = models.BooleanField(default=False)
	engine_desc = models.CharField(max_length=240, default="", blank=True)
	engine_fix = models.CharField(max_length=240, default="", blank=True)

	transmission_check = models.BooleanField(default=False)
	transmission_desc = models.CharField(max_length=240, default="", blank=True)
	transmission_fix = models.CharField(max_length=240, default="", blank=True)

	steering_check = models.BooleanField(default=False)
	steering_desc = models.CharField(max_length=240, default="", blank=True)
	steering_fix = models.CharField(max_length=240, default="", blank=True)

	horn_check = models.BooleanField(default=False)
	horn_desc = models.CharField(max_length=240, default="", blank=True)
	horn_fix = models.CharField(max_length=240, default="", blank=True)

	wipers_check = models.BooleanField(default=False)
	wipers_desc = models.CharField(max_length=240, default="", blank=True)
	wipers_fix = models.CharField(max_length=240, default="", blank=True)

	mirrors_check = models.BooleanField(default=False)
	mirrors_desc = models.CharField(max_length=240, default="", blank=True)
	mirrors_fix = models.CharField(max_length=240, default="", blank=True)

	lights_check = models.BooleanField(default=False)
	lights_type = models.CharField(max_length=3, choices=LIGHT_CHOICES, default="B")
	lights_desc = models.CharField(max_length=240, default="", blank=True)
	lights_fix = models.CharField(max_length=240, default="", blank=True)

	brakes_check = models.BooleanField(default=False)
	brakes_desc = models.CharField(max_length=240, default="", blank=True)
	brakes_fix = models.CharField(max_length=240, default="", blank=True)

	air_lines_check = models.BooleanField(default=False)
	air_lines_desc = models.CharField(max_length=240, default="", blank=True)
	air_lines_fix = models.CharField(max_length=240, default="", blank=True)

	tires_check = models.BooleanField(default=False)
	tires_desc = models.CharField(max_length=240, default="", blank=True)
	tires_fix = models.CharField(max_length=240, default="", blank=True)

	wheels_check = models.BooleanField(default=False)
	wheels_desc = models.CharField(max_length=240, default="", blank=True)
	wheels_fix = models.CharField(max_length=240, default="", blank=True)

	emergency_check = models.BooleanField(default=False)
	emergency_type = models.CharField(max_length=3, choices=EMERGENCY_CHOICES, default="AID")
	emergency_desc = models.CharField(max_length=240, default="", blank=True)
	emergency_fix = models.CharField(max_length=240, default="", blank=True)

	coupling_check = models.BooleanField(default=False)
	coupling_desc = models.CharField(max_length=240, default="", blank=True)
	coupling_fix = models.CharField(max_length=240, default="", blank=True)

	other_check = models.BooleanField(default=False)
	other_desc = models.CharField(max_length=240, default="", blank=True)
	other_fix = models.CharField(max_length=240, default="", blank=True)








	history = HistoricalRecords()
	#python manage.py clean_old_history --days 1 --auto
	@property
	def _history_user(self):
		return self.changed_by

	@_history_user.setter
	def _history_user(self, value):
		self.changed_by = value

	def __str__(self):
		return str(self.equipment)