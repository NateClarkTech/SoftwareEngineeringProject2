from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Checklist  # Assuming your model's name is Checklist
from django.db.models import F


# A simple view that returns checklist.html
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
        'task5': user_checklist.task5
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

        # Update the score
        user_checklist.update_score()

        return JsonResponse({'status': 'success'})
    
def leaderboard_view(request):
    # Query the database for all checklists, ordered by score in descending order
    checklists = Checklist.objects.order_by('-score')

    # Create a list of players with their rank, name, and score
    players = [
        {"rank": i + 1, "name": checklist.user.username, "score": checklist.score}
        for i, checklist in enumerate(checklists)
    ]

    return render(request, 'leaderboard.html', {'players': players})