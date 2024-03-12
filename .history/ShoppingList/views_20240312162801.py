from django.shortcuts import render
from .models import ShoppingListItem, ShoppingListCategory
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@login_required(login_url='/profile/login/')
def shoppinglist(request):
    #Make sure the user has a shopping list
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    if shoppingItems.count() == 0:
        create_user_shopping_list(request.user)
        shoppingItems = ShoppingListItem.objects.filter(user=request.user)
        
    #get the shopping list items and categories
    shoppingItems = ShoppingListItem.objects.filter(user=request.user)
    itemCategories = ShoppingListCategory.objects.all

    return render(request, 'shoppinglist.html', {'shoppingItems': shoppingItems, 'itemCategories': itemCategories})

@csrf_exempt
def update_shoppinglist(request):
    if request.method == 'POST':
        #Make sure the user has a shopping list
        shoppingItems = ShoppingListItem.objects.filter(user=request.user)
        if shoppingItems.count() == 0:
            create_user_shopping_list(request.user)
            shoppingItems = ShoppingListItem.objects.filter(user=request.user)
            
        i = 0
        for item in shoppingItems:
            i = i + 1
            #if the item is checked, delete it from the shopping list
            
            if request.POST.get('item-' + str(i)) == 'true':
                item.checked = request.POST.get('item' + i)
                item.save()

    print(request.POST)            
                
    return JsonResponse({'status': 'success'})




#If for some reason the user does not have a shopping list (i.e. the user was created before the shopping list feature was added), create a shopping list for the user
def create_user_shopping_list(current_user):
    roomEssentials = ShoppingListCategory.objects.get(name="Room Essentials")
    hygiene = ShoppingListCategory.objects.get(name="Hygiene")
    cleaningSupplies = ShoppingListCategory.objects.get(name="Cleaning Supplies")
    beachSupplies = ShoppingListCategory.objects.get(name="Beach Supplies")
    schoolSupplies = ShoppingListCategory.objects.get(name="School Supplies")
    emergencyPreparedness = ShoppingListCategory.objects.get(name="Emergency Preparedness")
    otherItems = ShoppingListCategory.objects.get(name="Other Items")
    
    ShoppingListItem.objects.create(user=current_user, name="Twin XL bedding set", category=roomEssentials, url="https://www.amazon.com/s?k=twin+xl+sheet+sets")
    ShoppingListItem.objects.create(user=current_user, name="Pillows", category=roomEssentials, url="https://www.amazon.com/s?k=bed+pillow")
    ShoppingListItem.objects.create(user=current_user, name="Mattress pad", category=roomEssentials, url="https://www.amazon.com/s?k=mattress+pad")
    ShoppingListItem.objects.create(user=current_user, name="Comforter and/or blanket", category=roomEssentials, url="https://www.amazon.com/s?k=comforter")
    ShoppingListItem.objects.create(user=current_user, name="Alarm clock", category=roomEssentials, url="https://www.amazon.com/s?k=alarm+clock")
    ShoppingListItem.objects.create(user=current_user, name="Lamp", category=roomEssentials, url="https://www.amazon.com/s?k=lamp")
    ShoppingListItem.objects.create(user=current_user, name="Trash bin", category=roomEssentials, url="https://www.amazon.com/s?k=trash+bin")
    ShoppingListItem.objects.create(user=current_user, name="Key chain that you would bet $148 on (price of a lost key)", category=roomEssentials, url="https://www.amazon.com/s?k=key+chain")
    ShoppingListItem.objects.create(user=current_user, name="Clothes hangers", category=roomEssentials, url="https://www.amazon.com/s?k=clothes+hangers")
    ShoppingListItem.objects.create(user=current_user, name="Laundry basket", category=roomEssentials, url="https://www.amazon.com/s?k=laundry+basket")
    
    ShoppingListItem.objects.create(user=current_user, name="Bath Towel", category=hygiene, url="https://www.amazon.com/s?k=bath+towels")
    ShoppingListItem.objects.create(user=current_user, name="Soap", category=hygiene, url="https://www.amazon.com/s?k=soap")
    ShoppingListItem.objects.create(user=current_user, name="Shampoo and Conditioner", category=hygiene, url="https://www.amazon.com/s?k=shampoo+and+conditioner")
    ShoppingListItem.objects.create(user=current_user, name="Deodorant", category=hygiene, url="https://www.amazon.com/s?k=deodorant")
    ShoppingListItem.objects.create(user=current_user, name="Toothbrush and Toothpaste", category=hygiene, url="https://www.amazon.com/s?k=toothbrush+and+toothpaste")
    ShoppingListItem.objects.create(user=current_user, name="Shaving supplies", category=hygiene, url="https://www.amazon.com/s?k=shaving+supplies")
    ShoppingListItem.objects.create(user=current_user, name="Toilet Paper", category=hygiene, url="https://www.amazon.com/s?k=toilet+paper")
    
    ShoppingListItem.objects.create(user=current_user, name="Dish Towel", category=cleaningSupplies, url="https://www.amazon.com/s?k=dish+towel")
    ShoppingListItem.objects.create(user=current_user, name="Dish Soap", category=cleaningSupplies, url="https://www.amazon.com/s?k=dish+soap")
    ShoppingListItem.objects.create(user=current_user, name="Room Deodorizing Spray", category=cleaningSupplies, url="https://www.amazon.com/s?k=room+deodorizing+spray")
    ShoppingListItem.objects.create(user=current_user, name="Laundry Soap", category=cleaningSupplies, url="https://www.amazon.com/s?k=laundry+soap")
    ShoppingListItem.objects.create(user=current_user, name="Disinfectant Wipes", category=cleaningSupplies, url="https://www.amazon.com/s?k=disinfectant+wipes")
    ShoppingListItem.objects.create(user=current_user, name="Lysol Spray", category=cleaningSupplies, url="https://www.amazon.com/s?k=lysol+spray")
    
    ShoppingListItem.objects.create(user=current_user, name="Swimsuit", category=beachSupplies, url="https://www.amazon.com/s?k=swimsuit")
    ShoppingListItem.objects.create(user=current_user, name="Beach Towel", category=beachSupplies, url="https://www.amazon.com/s?k=beach+towel")
    ShoppingListItem.objects.create(user=current_user, name="Sunscreen", category=beachSupplies, url="https://www.amazon.com/s?k=sunscreen")
    ShoppingListItem.objects.create(user=current_user, name="Refillable Water Bottle", category=beachSupplies, url="https://www.amazon.com/s?k=refillable+water+bottle")
    
    ShoppingListItem.objects.create(user=current_user, name="Personal Computer", category=schoolSupplies, url="https://www.amazon.com/s?k=personal+computer")
    ShoppingListItem.objects.create(user=current_user, name="Printer", category=schoolSupplies, url="https://www.amazon.com/s?k=printer")
    ShoppingListItem.objects.create(user=current_user, name="Printer Paper", category=schoolSupplies, url="https://www.amazon.com/s?k=printer+paper")
    ShoppingListItem.objects.create(user=current_user, name="Ethernet Cable", category=schoolSupplies, url="https://www.amazon.com/s?k=ethernet+cable")
    ShoppingListItem.objects.create(user=current_user, name="Flash Drive", category=schoolSupplies, url="https://www.amazon.com/s?k=flash+drive")
    ShoppingListItem.objects.create(user=current_user, name="Notebooks", category=schoolSupplies, url="https://www.amazon.com/s?k=notebooks")
    ShoppingListItem.objects.create(user=current_user, name="Laptop Lock", category=schoolSupplies, url="https://www.amazon.com/s?k=laptop+lock")
    ShoppingListItem.objects.create(user=current_user, name="Office Supplies (Poster Putty, Stapler, Push Pins, Pen/Pencils, Envelopes and Stamps)", category=schoolSupplies, url="https://www.amazon.com/s?k=office+supplies")
    ShoppingListItem.objects.create(user=current_user, name="Desk Lamp", category=schoolSupplies, url="https://www.amazon.com/s?k=desk+lamp")
    ShoppingListItem.objects.create(user=current_user, name="Power Strip with Surge Protector", category=schoolSupplies, url="https://www.amazon.com/s?k=power+strip+with+surge+protector")
    ShoppingListItem.objects.create(user=current_user, name="Multi-port USB Charger", category=schoolSupplies, url="https://www.amazon.com/s?k=multi-port+usb+charger")
    ShoppingListItem.objects.create(user=current_user, name="Headset", category=schoolSupplies, url="https://www.amazon.com/s?k=headset")
    
    ShoppingListItem.objects.create(user=current_user, name="Flashlight", category=emergencyPreparedness, url="https://www.amazon.com/s?k=flashlight")
    ShoppingListItem.objects.create(user=current_user, name="Batteries", category=emergencyPreparedness, url="https://www.amazon.com/s?k=batteries")
    ShoppingListItem.objects.create(user=current_user, name="First-aid Kit", category=emergencyPreparedness, url="https://www.amazon.com/s?k=first-aid+kit")
    
    ShoppingListItem.objects.create(user=current_user, name="Fan", category=otherItems, url="https://www.amazon.com/s?k=fan")
    ShoppingListItem.objects.create(user=current_user, name="Umbrella", category=otherItems, url="https://www.amazon.com/s?k=umbrella")
    ShoppingListItem.objects.create(user=current_user, name="Ear Plugs", category=otherItems, url="https://www.amazon.com/s?k=ear+plugs")
    ShoppingListItem.objects.create(user=current_user, name="Small Sewing Kit", category=otherItems, url="https://www.amazon.com/s?k=sewing+kit")
    ShoppingListItem.objects.create(user=current_user, name="Small Tool Kit", category=otherItems, url="https://www.amazon.com/s?k=tool+kit")
    ShoppingListItem.objects.create(user=current_user, name="Storage Bins", category=otherItems, url="https://www.amazon.com/s?k=storage+bins")
    ShoppingListItem.objects.create(user=current_user, name="Dishes and Utensils", category=otherItems, url="https://www.amazon.com/s?k=dishes+and+utensils")
    ShoppingListItem.objects.create(user=current_user, name="Camera", category=otherItems, url="https://www.amazon.com/s?k=camera")
    ShoppingListItem.objects.create(user=current_user, name="Can Opener", category=otherItems, url="https://www.amazon.com/s?k=can+opener")
