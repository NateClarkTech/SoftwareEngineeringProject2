from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# The view that renders our dorm info page
# Login required decorator ensures that only logged in users can access this page
@login_required(login_url='/profile/login/')
def dorm_info_view(request):
    #Nothing fancy just take get request and return our html page
    return render(request, 'info.html')