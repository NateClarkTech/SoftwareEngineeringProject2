from django.urls import path
from . import views
urlpatterns = [
    path('', views.dorm_info_view, name='dorms_view'),
    path('info/', views.dorm_info_view, name='dorms_view'),
]