from django.shortcuts import render
from .models import ShoppingListItem

# Create your views here.
def shoppinglist(request):
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems})