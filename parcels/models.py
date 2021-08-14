from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Parcel(models.Model):
    type = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('parcels:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)
