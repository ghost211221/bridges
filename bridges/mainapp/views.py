from django.shortcuts import render

from projectsapp.models import Project


def index(request):
    latest_projects = Project.objects.all().order_by('pk')[:6]
    return render(request, 'mainapp/index.html', {'latest_projects': latest_projects})


