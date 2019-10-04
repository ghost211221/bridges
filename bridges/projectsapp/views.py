from django.shortcuts import render, get_object_or_404

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


def projects(request):
    projects = Project.objects.all()
    products = TechnicalSolutions.objects.all()

    content = {
        'projects': projects,
        'products': products
    }
    return render(request, 'projectsapp/grid.html', content)


def project(request, pk):
    title = 'Проекты компании'
    item = get_object_or_404(Project, pk=pk)
    gallery = ProjectImage.objects.filter(project__pk=pk)
    solutions = ProjectHasTechnicalSolutions.objects.filter(project__pk=pk)
    all_values = ProjectHasTechnicalSolutions.objects.filter(project__pk=pk)

    content = {
        'page_title': title,
        'project': item,
        'gallery': gallery,
        'solutions': solutions,
        'values': all_values
    }
    return render(request, 'projectsapp/project.html', content)

