from django.db import models

class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    boxNumber = models.IntegerField()
    checked = models.BooleanField(default=False)