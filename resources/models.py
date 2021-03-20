from django.db import models
from commons.models import Model


class Resource(Model):
    name = models.CharField(max_length=70)
    resource_type = models.CharField(max_length=70)  # Todo: check for all possible values and convert it to list
    material = models.CharField(max_length=70)  # Todo: check whether it's list or not
    max_number_of_resources = models.FloatField()
    '''
    1-Check for many-to-many with task
    2- Check for st.resource and add it
    3- Check for ovt and add it
    4- Check for cost/use and add it
    '''