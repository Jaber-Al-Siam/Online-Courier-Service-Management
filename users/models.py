from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Customer(User):
    phone = models.CharField(max_length=20, default=None)
    User._meta.get_field('email')._unique = True

    def get_absolute_url(self):
        return reverse('users:customer_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class DeliveryAgent(User):
    phone = models.CharField(max_length=20)
    User._meta.get_field('email')._unique = True

    class Meta:
        verbose_name = 'delivery agent'
        verbose_name_plural = 'delivery Agents'
