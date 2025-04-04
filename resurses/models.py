from django.db import models
from django.contrib.auth.models import User


class Counters(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=50)
    elec_day = models.IntegerField()
    elec_night = models.IntegerField()
    water = models.IntegerField()
    gas = models.IntegerField()
