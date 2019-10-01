from django.shortcuts import render

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project


def projects(request):
    all_projects = Project.objects.all()
    products = TechnicalSolutions.objects.all()

    content = {
        'all_projects': all_projects,
        'products': products
    }
    return render(request, 'projectsapp/grid.html', content)
