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

from .rest_api import add_task, get_tasks, delete_task

urlpatterns = [

    # API OR CALENDER
    path('add_task/', add_task,name='add_task'),
    path('get_tasks/', get_tasks,name='get_tasks'),
    path('delete_task/<int:task_id>/', delete_task,name='delete_task'),
   
    
]