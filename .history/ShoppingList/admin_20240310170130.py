from django.contrib import admin
from .models import ShoppingListItem, ShoppingListCategory

# Register your models here.
admin.site.register(ShoppingListItem)
admin.site.register(ShoppingListCategory)