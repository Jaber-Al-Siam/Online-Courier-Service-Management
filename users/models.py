from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.

class Customer(User):
    User._meta.get_field('email')._unique = True

    def get_absolute_url(self):
        return reverse('users:customer_detail', kwargs={'pk': self.pk})
