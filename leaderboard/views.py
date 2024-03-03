from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Checklist  # Assuming your model's name is Checklist

# A simple view that returns checklist.html
def checklist(request):
    user_checklist = Checklist.objects.get(user=request.user)
    context = {
        'task1': user_checklist.task1,
        'task2': user_checklist.task2,
        'task3': user_checklist.task3,
        'task4': user_checklist.task4,
        'task5': user_checklist.task5
    }
    return render(request, 'checklist.html', context)

@csrf_exempt
def update_checklist(request):
    if request.method == 'POST':
        user_checklist = Checklist.objects.get(user=request.user)
        user_checklist.task1 = request.POST.get('task1') == 'true'
        user_checklist.task2 = request.POST.get('task2') == 'true'
        user_checklist.task3 = request.POST.get('task3') == 'true'
        user_checklist.task4 = request.POST.get('task4') == 'true'
        user_checklist.task5 = request.POST.get('task5') == 'true'
        user_checklist.save()
        return JsonResponse({'status': 'success'})