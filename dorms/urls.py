from django.urls import path
from . import views

app_name = 'dorms'

urlpatterns = [
    path('', views.dorm_info_view, name='dorms_view'),
    path('info/', views.dorm_info_view, name='dorm_info_view'),
]