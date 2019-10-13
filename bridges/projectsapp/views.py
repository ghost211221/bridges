from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView, DetailView

from productsapp.models import TechnicalSolutions
from projectsapp.forms import ProjectSolutionsForm
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


# Create your views here.
class ProjectsList(ListView):
    """docstring for ProductList"""
    paginate_by = 12
    model = Project
    template_name = 'projectsapp/grid.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        values = ProjectHasTechnicalSolutions.objects.all()
        context.update({'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context


class ProjectRead(DetailView):
    model = Project
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ProjectRead, self).get_context_data(**kwargs)
        context.update({'page_title': 'Детальная информация о проекте',
                        'bred_title': 'Информация о проекте'
                        })
        return context


class ProjectSolutionsCreate(CreateView):
    form_class = ProjectSolutionsForm
    model = Project
    success_url = reverse_lazy('projectsapp:projects')

    def get_context_data(self, **kwargs):
        data = super(ProjectSolutionsCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Project, ProjectHasTechnicalSolutions, form=ProjectSolutionsForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
            data['projectsolutions'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        projectsolutions = context['projectsolutions']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if projectsolutions.is_valid():
                projectsolutions.instance = self.object
                projectsolutions.save()


class ProjectDelete(DeleteView):
    pass
