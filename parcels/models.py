from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
import datetime

from users.models import Customer, DeliveryAgent


# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)


class Receiver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


class Parcel(models.Model):
    TYPE = [
        ('money', 'Money'),
        ('fruits', 'Fruits'),
        ('fragile', 'Fragile'),
        ('document', 'Document'),
        ('furniture', 'Furniture'),
        ('perishable', 'Perishable'),
        ('electronics', 'Electronics'),
    ]
    STATUS = [
        ('on_delivery', 'On Delivery'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
        ('picked', 'Picked'),
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE, default=None)
    pickup_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    receiver = models.OneToOneField(Receiver, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='pending')
    booked_on = models.DateTimeField(auto_now_add=True, editable=False)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_by', editable=False)
    delivery_agent = models.ForeignKey(DeliveryAgent, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('parcels:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)
