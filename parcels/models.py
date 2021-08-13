import self as self
from django.db import models

# Create your models here.


class Parcel(models.Model):
    parcel_type = models.CharField(max_length=20)
    receivers_email = models.CharField(max_length=100)
    url = self.object.get_absolute_url()

