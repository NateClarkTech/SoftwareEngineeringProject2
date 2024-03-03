from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register  # Make sure to create this view

urlpatterns = [

    # Backend-Heavy Pages
    path('todo/', views.todo, name='todo'),
    path("bilgestodo/", views.bilgestodo, name='bilgestodo'),
    path('cycreq/', views.cycreq, name='cycreq'),
    path('dontkillmefood/', views.dontkillmefood, name='dontkillmefood'),
    path('profile/', views.profile, name='profile'),  # For the logged-in user's profile
    path('profile/<str:username>/', views.public_profile, name='public_profile'),  # For viewing other users' profiles
    # Frontend-Heavy Pages
    path('', views.calendar, name='calendar'),
    path('timer/', views.timer, name='timer'),
    path('ncfhours/', views.ncfhours, name='ncfhours'),
    path('surprise/', views.surprise, name='surprise'),
    
    
    # Login/logout stuff
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    # profile search
    path('search/', views.search_profiles, name='search_profiles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

