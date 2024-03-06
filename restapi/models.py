from django.db import models


# CALENDER MODELS
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    date = models.CharField(max_length=30, default="")
    freq = models.CharField(max_length=30, default="")
    type = models.CharField(max_length=30, default="")
    time = models.BigIntegerField(default=0)
    desc = models.TextField(default='')
    
    def __str__(self):
        return self.title
