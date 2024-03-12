from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# The view that renders our dorm info page
@login_required(login_url='/profile/login/')
def dorm_info_view(request):
    return render(request, 'info.html')