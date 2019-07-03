from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point


class Event(models.Model):
    title = models.CharField(max_length=50, default='')
    location = models.PointField(default=Point(0, 0))
    date = models.DateTimeField(default=timezone.now)
