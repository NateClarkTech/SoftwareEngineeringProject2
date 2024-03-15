from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Checklist  # Assuming your model's name is Checklist
from django.db.models import F
from django.contrib.auth.decorators import login_required


#This is the PRIMARY VIEW for the checklist, it will render the checklist.html page and pass the context to the page (our tasks and their status) from the model
#The @login_required decorator ensures that only logged in users can access this page
@login_required(login_url='/profile/login/')
def checklist(request):
    #Try to get the users checklist from DB if it doesn't exist create a new one
    try:
        user_checklist = Checklist.objects.get(user=request.user)
    except Checklist.DoesNotExist:
        user_checklist = Checklist.objects.create(user=request.user)

    #The status of the users tasks are passed to the template as context
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

#This view is used to update the status of the tasks in the database and handle post requests from the JS
@csrf_exempt
def update_checklist(request):
    #Only handle request if it's a post request
    if request.method == 'POST':
        #Again try to get the users checklist from the DB, if it doesn't exist create a new one
        try:
            user_checklist = Checklist.objects.get(user=request.user)
        except Checklist.DoesNotExist:
            user_checklist = Checklist.objects.create(user=request.user)

        #Update the status of the tasks in the database
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

        #Return JSON response so JS knows the request was successful
        return JsonResponse({'status': 'success'})
    
#This view is for the reset button the page, and allows the user to reset all the tasks (Uncheck them) as well as updating their score
@csrf_exempt
def reset_tasks(request):
    #Only handle request if it's a post request
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

#This view is for the leaderboard page, it will render the leaderboardAlt.html page, and pass a list of players with their rank, name, and score to the page
#The @login_required decorator ensures that only logged in users can access this page
@login_required(login_url='/profile/login/')    
def leaderboard_view(request):
    # Query the database for all checklists, ordered by score in descending order
    checklists = Checklist.objects.order_by('-score')

    # Create a list of players with their rank, name, and score
    players = [
        {"rank": i + 1, "name": checklist.user.username, "score": checklist.score}
        for i, checklist in enumerate(checklists)
    ]
    # Pass the list of players to template and return the template
    return render(request, 'leaderboardAlt.html', {'players': players})