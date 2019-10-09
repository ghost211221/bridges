from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


# Create your views here.
class ProjectsList(ListView):
    """docstring for ProductList"""
    paginate_by = 6
    model = Project
    template_name = 'projectsapp/grid.html'
    extra_content = {}
    order_by = ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = TechnicalSolutions.objects.all()
        values = ProjectHasTechnicalSolutions.objects.all()
        context.update({'products': products,
                        'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context

    def get_queryset(self):
        return super().get_queryset().order_by(*self.order_by)


def project(request, pk):
    title = 'Проекты компании'
    item = get_object_or_404(Project, pk=pk)
    gallery = ProjectImage.objects.filter(project__pk=pk)
    values = ProjectHasTechnicalSolutions.objects.filter(project__pk=pk)

    content = {
        'page_title': title,
        'bred_title': title,
        'project': item,
        'gallery': gallery,
        'values': values
    }
    return render(request, 'projectsapp/project.html', content)
