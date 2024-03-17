from django.db import models
from django.contrib.auth.models import User


#Shopping list category that shopping list items point to
class ShoppingListCategory(models.Model):
    #Name of the category
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#Shopping list item modal
#points to a user, stores the name of the shopping list item
#points to the category it is apart of
#stores a link to an external page (store)
#Stores if the item is checked off or not
#NOTE: Extendos the todo item from project 1 but adds the feilds a shopping list item would need
class ShoppingListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ShoppingListCategory, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.name
