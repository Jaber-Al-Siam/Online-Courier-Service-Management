from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Parcel(models.Model):
    parcel_type = models.CharField(max_length=20)
    receiver_email = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('parcels:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)
