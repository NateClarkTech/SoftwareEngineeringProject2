from django.utils.dateparse import parse_time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # for celebration message
from django.views.decorators.http import require_http_methods
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def calendar(request):
    return render(request, 'calendar.html')

def ncfhours(request):
    return render(request, 'ncfhours.html')

def home(request):
    return render(request, 'home.html')

@require_http_methods(["GET", "POST"])
def dontkillmefood(request):
    # Handling food status, ripped from CYC
    if request.method == "POST":
        action = request.POST.get('action')
        if 'toggle_foodstatus' in request.POST:
            foodstatus_id = request.POST.get('foodstatus_id', '')
            foodstatus = foodDay.objects.get(id=foodstatus_id)
            foodstatus.is_lethal = not foodstatus.is_lethal
            foodstatus.save()
        return redirect('dontkillmefood')

    # Querysets for the context
    weekdays = foodDay.objects.all()

    context = {
        'weekdays': weekdays
    }
    return render(request, 'dontkillmefood.html', context)

