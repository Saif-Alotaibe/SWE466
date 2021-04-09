from django.db import models
from commons.models import Model
from djmoney.models.fields import MoneyField
from commons.models import User
from tasks.models import Task


class Resource(Model):
    WORK = "WORK"
    MATERIAL = "MATERIAL"
    COST = "COST"
    FULL_RESOURCE = 100.0
    HALF_RESOURCE = 50.0
    ZERO_RESOURCE = 0.0
    TYPES = (
        (WORK, "WORK"),
        (MATERIAL, "MATERIAL"),
        (COST, "COST"),
    )
    MAX_NUMBER_OF_RESOURCES = (
        (FULL_RESOURCE, "100.0%"),
        (HALF_RESOURCE, "50.0%"),
        (ZERO_RESOURCE, "0%")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resource', null=True)
    task = models.ManyToManyField(Task, blank=True, related_name="resources")
    name = models.CharField(max_length=70)
    resource_type = models.CharField(max_length=70, choices=TYPES)
    material_label = models.CharField(max_length=70)  # a measurment for a given resource  ex:tons,box
    max_number_of_resources = models.FloatField(choices=MAX_NUMBER_OF_RESOURCES)  # Either 100, 50 , 0
    standard_rate = MoneyField(max_digits=14, decimal_places=2, default_currency="USD", null=True)
    overtime_rate = MoneyField(max_digits=14, decimal_places=2, default_currency="USD", null=True)
    cost_of_use = MoneyField(max_digits=14, decimal_places=2, default_currency="USD", null=True)
    
    def __str__(self):
        return self.name
