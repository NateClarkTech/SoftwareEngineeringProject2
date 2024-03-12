from django.db import models
from django import forms
from .models import *
from authentication.models import User

class Meta:
    ordering = ['name']

class Task(models.Model):

    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    completed = models.BooleanField(default=False)
    # everytime an item is created, it will be automatically added
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
      
class InProgressCourse(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    days_of_week = models.CharField(max_length=5, null=True, blank=True)  # e.g. 'MWF' for Monday, Wednesday, Friday

    def __str__(self):
        return f"{self.name} ({self.days_of_week} {self.start_time}-{self.end_time})"

class CompletedCourse(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CYCRequirement(models.Model):
    completedByCourse = models.ForeignKey(CompletedCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class foodDay(models.Model):
    name = models.CharField(max_length=200)
    is_lethal = models.BooleanField(default=False)
    #days_of_week = models.CharField(max_length=7, null=True, blank=True)  # e.g. 'MWF' for Monday, Wednesday, Friday

    def __str__(self):
        return self.name


class Event:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now_add=True)
    eventType = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)

class Chatroom(models.Model):
    roomName = models.CharField(max_length=200)

class Message(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    message = models.CharField(max_length=2000)
    #days_of_week = models.CharField(max_length=7, null=True, blank=True)  # e.g. 'MWF' for Monday, Wednesday, Friday

    def __str__(self):
        return self.name
    
class Leaderboard():
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    boxNumber = models.IntegerField()
    checked = models.BooleanField(default=False)