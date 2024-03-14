from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.shoppinglist, name='shoppinglist'),
    path('update_shoppinglist', views.update_shoppinglist, name='update_shoppinglist'),
]