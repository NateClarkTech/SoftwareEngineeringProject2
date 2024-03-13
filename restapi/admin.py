from django.apps import apps
from django.contrib import admin
from .models import Message,Task

app = apps.get_app_config('restapi')

admin.site.register(Message)
admin.site.register(Task)
