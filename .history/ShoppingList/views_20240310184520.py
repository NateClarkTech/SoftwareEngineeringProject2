from django.shortcuts import render
from .models import ShoppingListItem, ShoppingListCategory

# Create your views here.
def shoppinglist(request):
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    itemCategories = ShoppingListCategory.objects.all

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems, 'itemCategories': itemCategories})