from django.shortcuts import render

# Create your views here.

def projects_asgrid(request):
    return render(request, 'projectsapp/grid.html')
