from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ShoppingListItem

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        ShoppingList = [
        ShoppingListItem.objects.create(user=instance, name="Twin XL bedding set", category="Room Essentials", url="https://www.amazon.com/s?k=twin+xl+sheet+sets").save(),
        ShoppingListItem.objects.create(user=instance, name="Pillows", category="Room Essentials", url="https://www.amazon.com/s?k=bed+pillow").save(),
        ShoppingListItem.objects.create(user=instance, name="Mattress pad", category="Room Essentials", url="https://www.amazon.com/s?k=mattress+pad").save(),
        ShoppingListItem.objects.create(user=instance, name="Comforter and/or blanket", category="Room Essentials", url="https://www.amazon.com/s?k=comforter").save(),
        ShoppingListItem.objects.create(user=instance, name="Alarm clock", category="Room Essentials", url="https://www.amazon.com/s?k=alarm+clock").save(),
        ShoppingListItem.objects.create(user=instance, name="Lamp", category="Room Essentials", url="https://www.amazon.com/s?k=lamp").save(),
        ShoppingListItem.objects.create(user=instance, name="Trash bin", category="Room Essentials", url="https://www.amazon.com/s?k=trash+bin"),
        ShoppingListItem.objects.create(user=instance, name="Key chain that you would bet $148 on (price of a lost key)", category="Room Essentials", url="https://www.amazon.com/s?k=key+chain").save(),
        ShoppingListItem.objects.create(user=instance, name="Clothes hangers", category="Room Essentials", url="clothes hangers").save(),
        ShoppingListItem.objects.create(user=instance, name="Laundry basket", category="Room Essentials", url="https://www.amazon.com/s?k=laundry+basket").save(),
        ShoppingListItem.objects.create(user=instance, name="Bath Towel", category="Hygiene", url="").save(),
        ShoppingListItem.objects.create(user=instance, name="Soap", category="Hygiene", url="").save(),
        ShoppingListItem.objects.create(user=instance, name="Shampoo and Conditioner", category="Hygiene", url="https://www.amazon.com/s?k=shampoo+and+conditioner").save(),
        ShoppingListItem.objects.create(user=instance, name="Deodorant", category="Hygiene", url="https://www.amazon.com/s?k=deodorant").save(),
        ShoppingListItem.objects.create(user=instance, name="Toothbruh and Toothpaste", category="Hygiene", url="https://www.amazon.com/s?k=toothbrush+and+toothpaste").save(),
        ShoppingListItem.objects.create(user=instance, name="Shaving supplies", category="Hygiene", url="https://www.amazon.com/s?k=shaving+supplies").save(),
        ShoppingListItem.objects.create(user=instance, name="Toilet Paper", category="Hygiene", url="https://www.amazon.com/s?k=toilet+paper").save(),
        ShoppingListItem.objects.create(user=instance, name="Dish Towel", category="Cleaning Supplies", url="https://www.amazon.com/s?k=dish+towel").save(),
        ShoppingListItem.objects.create(user=instance, name="Dish Soap", category="Cleaning Supplies", url="https://www.amazon.com/s?k=dish+soap").save(),
        ShoppingListItem.objects.create(user=instance, name="Room Deodorizing Spray", category="Cleaning Supplies", url="https://www.amazon.com/s?k=room+deodorizing+spray").save(),
        ShoppingListItem.objects.create(user=instance, name="Laundry Soap", category="Cleaning Supplies", url="https://www.amazon.com/s?k=laundry+soap").save(),
        ShoppingListItem.objects.create(user=instance, name="Disinfectant Wipes", category="Cleaning Supplies", url="https://www.amazon.com/s?k=disinfectant+wipes").save(),
        ShoppingListItem.objects.create(user=instance, name="Lysol Spray", category="Cleaning Supplies", url="https://www.amazon.com/s?k=lysol+spray").save(),
        ShoppingListItem.objects.create(user=instance, name="Swimsuit", category="Beach Supplies", url="https://www.amazon.com/s?k=swimsuit").save(),
        ShoppingListItem.objects.create(user=instance, name="Beach Towel", category="Beach Supplies", url="https://www.amazon.com/s?k=beach+towel").save(),
        ShoppingListItem.objects.create(user=instance, name="Sunscreen", category="Beach Supplies", url="https://www.amazon.com/s?k=sunscreen").save(),
        ShoppingListItem.objects.create(user=instance, name="Refillable Water Bottle", category="Beach Supplies", url="https://www.amazon.com/s?k=refillable+water+bottle").save(),
        ShoppingListItem.objects.create(user=instance, name="Personal Computer", category="School Supplies", url="https://www.amazon.com/s?k=personal+computer").save(),
        ShoppingListItem.objects.create(user=instance, name="Printer", category="School Supplies", url="https://www.amazon.com/s?k=printer").save(),
        ShoppingListItem.objects.create(user=instance, name="Printer Paper", category="School Supplies", url="https://www.amazon.com/s?k=printer+paper").save(),
        ShoppingListItem.objects.create(user=instance, name="Ethernet Cable", category="School Supplies", url="https://www.amazon.com/s?k=ethernet+cable").save(),
        ShoppingListItem.objects.create(user=instance, name="Flash Drive", category="School Supplies", url="https://www.amazon.com/s?k=flash+drive").save(),
        ShoppingListItem.objects.create(user=instance, name="Notebooks", category="School Supplies", url="https://www.amazon.com/s?k=notebooks").save(),
        ShoppingListItem.objects.create(user=instance, name="Laptop Lock", category="School Supplies", url="https://www.amazon.com/s?k=laptop+lock").save(),
        ShoppingListItem.objects.create(user=instance, name="Office Supplies (Poster Putty, Stapler, Push Pins, Pen/Pencils, Envelopes and Stamps)", category="School Supplies", url="https://www.amazon.com/s?k=office+supplies").save(),
        ShoppingListItem.objects.create(user=instance, name="Desk Lamp", category="School Supplies", url="https://www.amazon.com/s?k=desk+lamp").save(),
        ShoppingListItem.objects.create(user=instance, name="Power Strip with Surge Protector", category="School Supplies", url="https://www.amazon.com/s?k=power+strip+with+surge+protector").save(),
        ShoppingListItem.objects.create(user=instance, name="Multi-port USB Charger", category="School Supplies", url="https://www.amazon.com/s?k=multi-port+usb+charger").save(),
        ShoppingListItem.objects.create(user=instance, name="Headset", category="School Supplies", url="https://www.amazon.com/s?k=headset").save(),
        ShoppingListItem.objects.create(user=instance, name="Flashlight", category="Emergency Preparedness", url="https://www.amazon.com/s?k=flashlight").save(),
        ShoppingListItem.objects.create(user=instance, name="Batteries", category="Emergency Preparedness", url="https://www.amazon.com/s?k=batteries").save(),
        ShoppingListItem.objects.create(user=instance, name="First-aid Kit", category="Emergency Preparedness", url="https://www.amazon.com/s?k=first-aid+kit").save(),
        ShoppingListItem.objects.create(user=instance, name="Fan", category="Other Items", url="https://www.amazon.com/s?k=fan").save(),
        ShoppingListItem.objects.create(user=instance, name="Umbrella", category="Other Items", url="https://www.amazon.com/s?k=umbrella").save(),
        ShoppingListItem.objects.create(user=instance, name="Ear Plugs", category="Other Items", url="https://www.amazon.com/s?k=ear+plugs").save(),
        ShoppingListItem.objects.create(user=instance, name="Small Sewing Kit", category="Other Items", url="https://www.amazon.com/s?k=sewing+kit").save(),
        ShoppingListItem.objects.create(user=instance, name="Small Tool Kit", category="Other Items", url="https://www.amazon.com/s?k=tool+kit").save(),
        ShoppingListItem.objects.create(user=instance, name="Storage Bins", category="Other Items", url="https://www.amazon.com/s?k=storage+bins").save(),
        ShoppingListItem.objects.create(user=instance, name="Dishes and Utensils", category="Other Items", url="https://www.amazon.com/s?k=dishes+and+utensils").save(),
        ShoppingListItem.objects.create(user=instance, name="Camera", category="Other Items", url="https://www.amazon.com/s?k=camera").save(),
        ShoppingListItem.objects.create(user=instance, name="Can Opener", category="Other Items", url="https://www.amazon.com/s?k=can+opener").save(),
        ]
        
        for item in ShoppingList:
            item.save()
