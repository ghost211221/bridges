from django.shortcuts import render

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project


def projects(request):
    projects = Project.objects.all()
    products = TechnicalSolutions.objects.all()

    content = {
        'projects': projects,
        'products': products
    }
    return render(request, 'projectsapp/grid.html', content)
