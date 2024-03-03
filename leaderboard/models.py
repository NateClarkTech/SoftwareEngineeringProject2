from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Checklist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    task1 = models.BooleanField(default=False)
    task2 = models.BooleanField(default=False)
    task3 = models.BooleanField(default=False)
    task4 = models.BooleanField(default=False)
    task5 = models.BooleanField(default=False)