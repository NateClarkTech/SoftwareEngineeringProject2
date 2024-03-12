from django.shortcuts import render
from .models import ShoppingList

# Create your views here.
def shoppinglist(request):
    shoppingItems = ShoppingList.objects.filter(user=request.user)

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems})