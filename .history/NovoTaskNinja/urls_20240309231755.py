from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Backend-Heavy Pages
    path('dontkillmefood/', views.dontkillmefood, name='dontkillmefood'),
    
    # Frontend-Heavy Pages
    path('calendar', views.calendar, name='calendar'),
    path('ncfhours/', views.ncfhours, name='ncfhours'),
    path('', views.home, name='home'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    