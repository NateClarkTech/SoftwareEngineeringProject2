from django.shortcuts import render
from .models import ShoppingList

# Create your views here.
def shoppinglist(request):
    shoppingItems = ShoppingList.objects.all()

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems})