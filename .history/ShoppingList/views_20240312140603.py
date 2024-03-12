from django.shortcuts import render
from .models import ShoppingListItem, ShoppingListCategory

@login_required(login_url='/profile/login/')
def shoppinglist(request):
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    itemCategories = ShoppingListCategory.objects.all

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems, 'itemCategories': itemCategories})