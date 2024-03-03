from django.shortcuts import render

# Create your views here.

#A simple view that returns checklist.html
def checklist(request):
    return render(request, 'checklist.html', {})