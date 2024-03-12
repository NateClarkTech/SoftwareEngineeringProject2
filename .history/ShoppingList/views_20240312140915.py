from django.shortcuts import render
from .models import ShoppingListItem, ShoppingListCategory
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/profile/login/')
def shoppinglist(request):
    try:
        shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    except ShoppingListItem.DoesNotExist:
        shoppingItems = None
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    itemCategories = ShoppingListCategory.objects.all

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems, 'itemCategories': itemCategories})

@csrf_exempt
def update_shoppinglist(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = ShoppingListItem.objects.get(pk=item_id)
        item.completed = not item.completed
        item.save()

    return JsonResponse({'status': 'ok'})