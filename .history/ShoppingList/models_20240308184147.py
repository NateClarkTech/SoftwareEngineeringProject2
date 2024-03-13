from django.db import models

class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    checked = models.BooleanField(default=False)