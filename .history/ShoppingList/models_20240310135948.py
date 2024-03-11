from django.db import models
from django.contrib.auth.models import User

class ShoppingListCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username + " - " + self.name

class ShoppingListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShoppingListCategory)
    url = models.URLField(max_length=200)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.name