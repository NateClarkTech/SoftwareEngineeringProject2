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
    score = models.IntegerField(default=0)

    def update_score(self):
        self.score = sum([self.task1, self.task2, self.task3, self.task4, self.task5])
        self.save()