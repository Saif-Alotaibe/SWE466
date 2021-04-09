from django.db import models
from commons.models import Model


class Task(Model):
	name = models.CharField(max_length=70)
	duration = models.PositiveSmallIntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	
	def __str__(self):
		return self.name
