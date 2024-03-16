from django.db import models


# CALENDER MODELS
"""
Represents a user tasks in the calender
"""
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    date = models.CharField(max_length=30, default="")
    freq = models.CharField(max_length=30, default="")
    type = models.CharField(max_length=30, default="")
    time = models.BigIntegerField(default=0)
    desc = models.TextField(default='')
    userid = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title


"""
Represents a single message in the chat page
"""
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=255, default="")
    val = models.TextField(default='')
    time = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.val
