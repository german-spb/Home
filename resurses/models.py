from django.db import models
from django.contrib.auth.models import User


class Counters(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=50)
    elec_day = models.IntegerField()
    outgo_elec_day = models.IntegerField(null=True, blank=True)
    elec_night = models.IntegerField()
    outgo_elec_night = models.IntegerField(null=True, blank=True)
    water = models.IntegerField()
    outgo_water = models.IntegerField(null=True, blank=True)
    gas = models.IntegerField()
    outgo_gas = models.IntegerField(null=True, blank=True)



    class Meta:
        unique_together = ('year', 'month')


class Document(models.Model):
    title = models.CharField(max_length=200)
    document = models.ImageField(upload_to='documents')
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.title

