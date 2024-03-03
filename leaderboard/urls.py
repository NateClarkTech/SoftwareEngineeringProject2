from django.urls import path
from . import views

urlpatterns = [
    path('checklist/', views.checklist, name='checklist'),
]