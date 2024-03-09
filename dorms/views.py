from django.shortcuts import render

# Create your views here.
def dorm_info_view(request):
    return render(request, 'info.html')