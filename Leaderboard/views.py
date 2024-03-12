from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Checklist  # Assuming your model's name is Checklist
from django.db.models import F
from django.contrib.auth.decorators import login_required


# A simple view that returns checklist.html
@login_required(login_url='/profile/login/')
def checklist(request):
    try:
        user_checklist = Checklist.objects.get(user=request.user)
    except Checklist.DoesNotExist:
        user_checklist = Checklist.objects.create(user=request.user)

    context = {
        'task1': user_checklist.task1,
        'task2': user_checklist.task2,
        'task3': user_checklist.task3,
        'task4': user_checklist.task4,
        'task5': user_checklist.task5,
        'task6': user_checklist.task6,
        'task7': user_checklist.task7,
        'task8': user_checklist.task8,
        'task9': user_checklist.task9,
        'task10': user_checklist.task10
    }
    return render(request, 'checklist.html', context)

@csrf_exempt
def update_checklist(request):
    if request.method == 'POST':
        try:
            user_checklist = Checklist.objects.get(user=request.user)
        except Checklist.DoesNotExist:
            user_checklist = Checklist.objects.create(user=request.user)

        user_checklist.task1 = request.POST.get('task1') == 'true'
        user_checklist.task2 = request.POST.get('task2') == 'true'
        user_checklist.task3 = request.POST.get('task3') == 'true'
        user_checklist.task4 = request.POST.get('task4') == 'true'
        user_checklist.task5 = request.POST.get('task5') == 'true'
        user_checklist.task6 = request.POST.get('task6') == 'true'
        user_checklist.task7 = request.POST.get('task7') == 'true'
        user_checklist.task8 = request.POST.get('task8') == 'true'
        user_checklist.task9 = request.POST.get('task9') == 'true'
        user_checklist.task10 = request.POST.get('task10') == 'true'

        # Update the score
        user_checklist.update_score()

        return JsonResponse({'status': 'success'})
    

@csrf_exempt
def reset_tasks(request):
    if request.method == 'POST':
        # Assuming the user is authenticated and available as request.user
        checklist = Checklist.objects.get(user=request.user)

        # Reset all tasks and score
        checklist.task1 = request.POST.get('task1') != 'false'
        checklist.task2 = request.POST.get('task2') != 'false'
        checklist.task3 = request.POST.get('task3') != 'false'
        checklist.task4 = request.POST.get('task4') != 'false'
        checklist.task5 = request.POST.get('task5') != 'false'
        checklist.task6 = request.POST.get('task6') != 'false'
        checklist.task7 = request.POST.get('task7') != 'false'
        checklist.task8 = request.POST.get('task8') != 'false'
        checklist.task9 = request.POST.get('task9') != 'false'
        checklist.task10 = request.POST.get('task10') != 'false'
        checklist.score = int(request.POST.get('score'))
        checklist.save()

        # Return a success response
        return JsonResponse({'status': 'success'})

@login_required(login_url='/profile/login/')    
def leaderboard_view(request):
    # Query the database for all checklists, ordered by score in descending order
    checklists = Checklist.objects.order_by('-score')

    # Create a list of players with their rank, name, and score
    players = [
        {"rank": i + 1, "name": checklist.user.username, "score": checklist.score}
        for i, checklist in enumerate(checklists)
    ]

    return render(request, 'leaderboardAlt.html', {'players': players})