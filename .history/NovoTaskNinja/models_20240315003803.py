from django.db import models
from django import forms
from .models import *
from django.contrib.auth.models import User

class Meta:
    ordering = ['name']


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
    
