from django.shortcuts import render, get_object_or_404
from projectsapp.models import Project


def map(request):
    projects = Project.objects.all()
    context = {
        'page_title': 'Карта проектов',
        'projects': projects,
        'bred_title': 'Карта проектов'
    }
    return render(request, 'ymapapp/map.html', context)


def project(request, slug):
    projects = get_object_or_404(Project, slug=slug)
    context = {
        'projects': projects,
    }
    return render(request, 'projectsapp/project.html', context)
