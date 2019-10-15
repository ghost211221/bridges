from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View

from django.views.generic import ListView, CreateView, DeleteView, DetailView

from productsapp.models import TechnicalSolutions
from projectsapp.forms import ProjectSolutionsForm, ProjectManagerForm
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


class ProjectSolutionsUpdate(View):
    def get(self, request):
        form = ProjectSolutionsForm()
        return render(request, 'projectsapp/product_update.html', context={'form': form})

    def post(self, request):
        bound_form = ProjectSolutionsForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('projectsapp:projects')
        return render(request, 'projectsapp/product_update.html', context={'form': bound_form})


class ProjectManagesUpdate(View):
    def get(self, request):
        form = ProjectManagerForm()
        return render(request, 'projectsapp/manager_update.html', context={'form': form})

    def post(self, request):
        bound_form = ProjectManagerForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('projectsapp:projects')
        return render(request, 'projectsapp/manager_update.html', context={'form': bound_form})


class ProjectDelete(DeleteView):
    pass
