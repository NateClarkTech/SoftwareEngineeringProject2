from django.urls import path
from . import views


#Name the app so that the url can be accessed by the base template
app_name = 'dorms'

#Attach the view to the url
urlpatterns = [
    path('', views.dorm_info_view, name='dorms_view'),
    path('info/', views.dorm_info_view, name='dorm_info_view'),
]