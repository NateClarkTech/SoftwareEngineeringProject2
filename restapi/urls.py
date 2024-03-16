"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .rest_api import add_task, get_tasks, delete_task, add_message, \
    get_messages, delete_message, get_username, test_chat

urlpatterns = [

    # CALENDER API
    path('add_task/', add_task, name='add_task'),
    path('get_tasks/<int:userid>/', get_tasks, name='get_tasks'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),


    # CHAT API
    path('add_message/', add_message, name='add_message'),
    path('get_messages/', get_messages, name='get_messages'),
    path('delete_message/<int:message_id>/',
         delete_message, name='delete_message'),
    path('get_username/', get_username, name='get_username'),
    path('test_chat/', test_chat, name='get_username'),

]
