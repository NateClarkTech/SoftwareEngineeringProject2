from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Backend-Heavy Pages
    path('todo/', views.todo, name='todo'),
    path("bilgestodo/", views.bilgestodo, name='bilgestodo'),
    path('cycreq/', views.cycreq, name='cycreq'),
    path('dontkillmefood/', views.dontkillmefood, name='dontkillmefood'),

    # Frontend-Heavy Pages
    path('', views.calendar, name='calendar'),
    path('calendar/', views.calendar, name='calendar'),
    path('timer/', views.timer, name='timer'),
    path('ncfhours/', views.ncfhours, name='ncfhours'),
    path('surprise/', views.surprise, name='surprise'),
    
    path('home/', views.home, name='home'),
    
    # Student organization page
    path('student_organizations/', views.student_organizations, name='orgs'),
    

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

