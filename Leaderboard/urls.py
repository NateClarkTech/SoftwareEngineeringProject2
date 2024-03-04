from django.urls import path
from . import views
#https://www.reddit.com/r/django/comments/13hknj7/my_project_doesnt_recognize_the_urls_from_one_of/
urlpatterns = [
    path('', views.checklist, name='checklist'),
    path('checklist/', views.checklist, name='checklist'),
]