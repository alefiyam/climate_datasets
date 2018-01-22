from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Country(models.Model):
    """docstring for Country"""
    country_name = models.CharField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.country_name


class TemperatureType(models.Model):
    """docstring for Country"""
    temprature_type = models.CharField(null=True, blank=True, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class TemperatureData(models.Model):
    """docstring for Country"""
    temp_type = models.ForeignKey(TemperatureType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    Year = models.IntegerField(null=True, blank=True, default=None)
    JAN = models.FloatField(null=True, blank=True, default=None)
    FEB = models.FloatField(null=True, blank=True, default=None)
    MAR = models.FloatField(null=True, blank=True, default=None)
    APR = models.FloatField(null=True, blank=True, default=None)
    MAY = models.FloatField(null=True, blank=True, default=None)
    JUN = models.FloatField(null=True, blank=True, default=None)
    JUL = models.FloatField(null=True, blank=True, default=None)
    AUG = models.FloatField(null=True, blank=True, default=None)
    SEP = models.FloatField(null=True, blank=True, default=None)
    OCT = models.FloatField(null=True, blank=True, default=None)
    NOV = models.FloatField(null=True, blank=True, default=None)
    DEC = models.FloatField(null=True, blank=True, default=None)
    WIN = models.FloatField(null=True, blank=True, default=None)
    SPR = models.FloatField(null=True, blank=True, default=None)
    SUM = models.FloatField(null=True, blank=True, default=None)
    AUT = models.FloatField(null=True, blank=True, default=None)
    ANN = models.FloatField(null=True, blank=True, default=None)
    # class Meta:
    # unique_together = ["temp_type", "Year", "JAN","FEB"]
