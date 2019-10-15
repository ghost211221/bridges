from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from productsapp.models import TechnicalSolutions
from .forms import *
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions, ProjectCompany, ProjectManagers
# Create your views here.
from projectsapp.utils import ObjectCreateMixin


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


class ProjectSolutionsUpdate(ObjectCreateMixin, View):
    form_model = ProjectSolutionsForm
    template = 'projectsapp/product_update.html'


class ProjectManagersUpdate(ObjectCreateMixin, View):
    form_model = ProjectManagerForm
    template = 'projectsapp/manager_update.html'


class ProjectCompanyUpdate(ObjectCreateMixin, View):
    form_model = ProjectCompanyForm
    template = 'projectsapp/company_update.html'


class ProjectDelete(DeleteView):
    pass


# class ProjectManagersUpdate(UpdateView):
#     model = Project
#     fields = []
#     success_url = reverse_lazy('projectsapp:projects')
#
#     def get_context_data(self, **kwargs):
#         data = super(ProjectManagersUpdate, self).get_context_data(**kwargs)
#         projectformset = inlineformset_factory(Project, ProjectManagers, form=ProjectManagerForm, extra=1)
#         if self.request.POST:
#             data['managers'] = projectformset(self.request.POST, instance=self.object)
#         else:
#             formset = projectformset(instance=self.object)
#             data['managers'] = formset
#             return data

def company_update(request, pk):
    if id:
        project = Project.objects.get(pk=pk)
    else:
        project = Project()
    project_form = ProjectForm(instance=project)
    BookInlineFormSet = inlineformset_factory(Project, ProjectCompany, form=ProjectCompanyForm, extra=1)
    formset = BookInlineFormSet(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if id:
            project_form = ProjectForm(request.POST, instance=project)
            formset = BookInlineFormSet(request.POST)
            if project_form.is_valid():
                created_project = project_form.save(commit=False)
                formset = BookInlineFormSet(request.POST, instance=created_project)
                if formset.is_valid():
                    created_project.save()
                    formset.save()
                    return HttpResponseRedirect(created_project.get_absolute_url())
    context ={
        'project_form': project_form,
        'formset': formset,
        'page_title': 'Добавление контрагентов',
        'bred_title': 'Добавление контрагентов',
        'project': project
    }
    return render(request, "projectsapp/company_update.html", context)


def gallery_update(request, pk):
    if id:
        project = Project.objects.get(pk=pk)
    else:
        project = Project()
    project_form = ProjectForm(instance=project)
    BookInlineFormSet = inlineformset_factory(Project, ProjectImage, form=ProjectImageForm, extra=3)
    formset = BookInlineFormSet(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if id:
            project_form = ProjectForm(request.POST, instance=project)
            formset = BookInlineFormSet(request.POST, request.FILES)
            if project_form.is_valid():
                created_project = project_form.save(commit=False)
                formset = BookInlineFormSet(request.POST, request.FILES, instance=created_project)
                if formset.is_valid():
                    created_project.save()
                    formset.save()
                    return HttpResponseRedirect(created_project.get_absolute_url())
    context ={
        'project_form': project_form,
        'formset': formset,
        'page_title': 'Добавление фотографий',
        'bred_title': 'Добавление фотографий',
        'project': project
    }
    return render(request, "projectsapp/gallery_update.html", context)