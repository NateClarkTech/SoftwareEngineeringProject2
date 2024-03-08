from django.shortcuts import render

# Create your views here.
def shoppinglist(request):
    return render(request, 'shoppinglist.html')