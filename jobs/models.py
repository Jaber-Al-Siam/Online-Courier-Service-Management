from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Customer


class Job(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    vacancy = models.IntegerField()
    position = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salary = models.IntegerField()
    email = models.EmailField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    applicants = [Customer]
