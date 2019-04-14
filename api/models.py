from django.db import models


class BusStop(models.Model):
    id = models.AutoField(primary_key=True, null=None, unique=True)
    busStopName = models.CharField(max_length=32)
    latitude = models.DecimalField(max_digits=15, decimal_places=13)
    longitude = models.DecimalField(max_digits=15, decimal_places=13)
