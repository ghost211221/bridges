from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions, ProjectCompany, ProjectManagers
from projectsapp.models import ProjectImage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from projectsapp.forms import ProjectSolutionsForm, ProjectManagerForm, ProjectCompanyForm
from projectsapp.forms import ProjectManagerUpdateFormset
from projectsapp.models import Project, ProjectHasTechnicalSolutions, ProjectCompany
from authapp.models import Users

from django.http import HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth.mixins import  PermissionRequiredMixin
from django.urls import reverse_lazy


class ProjectsList(ListView):
    """docstring for ProductList"""    
    model = Project

    template_name = 'projectsapp/grid.html'
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = TechnicalSolutions.objects.all()
        values = ProjectHasTechnicalSolutions.objects.all()
        # context.update({'values': values,
        context.update({'products': products,
                        'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context


class ProjectRead(DetailView):
    model = Project
    extra_context = {}    
    not_empty_url = reverse_lazy('projects:project')

    def get_context_data(self, **kwargs):
        context = super(ProjectRead, self).get_context_data(**kwargs)
        context.update({'page_title': 'Детальная информация о проекте',
                        'bred_title': 'Информация о проекте'
                        })
        return context


def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectUpdateForm(instance=project)
    if request.method == 'POST':
        project_form = ProjectUpdateForm(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect(project.get_absolute_url())
    context = {
        'project_form': project_form,
        'page_title': 'Редактирование основной информации',
        'bred_title': 'Обновление проекта',
        'project': project
    }
    return render(request, 'projectsapp/company_update.html', context)

#  ------------------------------------ UPDATE PROJECT'S SOLUTIONS ----------------------------------------------


def project_solutions_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectForm(instance=project)
    solutions_formset = inlineformset_factory(Project, ProjectHasTechnicalSolutions, form=ProjectSolutionsForm, extra=1)
    formset = solutions_formset(instance=project)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        formset = solutions_formset(request.POST)
        if project_form.is_valid():
            updated_project = project_form.save(commit=False)
            formset = solutions_formset(request.POST, instance=updated_project)
            if formset.is_valid():
                updated_project.save()
                formset.save()
                return HttpResponseRedirect(updated_project.get_absolute_url())
    context = {
        'project_form': project_form,
        'formset': formset,
        'page_title': 'Обновление технических решений',
        'bred_title': 'Обновление техрешений',
        'project': project
    }
    return render(request, 'projectsapp/company_update.html', context)


#  ------------------------------------ UPDATE PROJECT'S COMPANIES ----------------------------------------------


def company_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectForm(instance=project)
    company_formset = inlineformset_factory(Project, ProjectCompany, form=ProjectCompanyForm, extra=1)
    formset = company_formset(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        project_form = ProjectForm(request.POST, instance=project)
        formset = company_formset(request.POST)
        if project_form.is_valid():
            created_project = project_form.save(commit=False)
            formset = company_formset(request.POST, instance=created_project)
            if formset.is_valid():
                created_project.save()
                formset.save()
                return HttpResponseRedirect(created_project.get_absolute_url())
    context ={
        'project_form': project_form,
        'formset1': formset,
        'page_title': 'Добавление контрагентов',
        'bred_title': 'Добавление контрагентов',
        'project': project
    }
    return render(request, "projectsapp/company_update.html", context)

#  ------------------------------------ PROJECT'S MANAGERS CRUD ----------------------------------------------

def get_manager(pk):
    """находит менеджера по id"""
    return Users.objects.get(pk=pk)
 
class ProjectManagersList(ListView):
    model = ProjectManagers
    template_name = 'projectsapp/manager_update.html'

    pk_field = 'project'
    def get_queryset(self):
        query = Q()
        if 'pk' in self.kwargs:
            query = Q((self.pk_field, self.kwargs['pk']))
        return super().get_queryset().filter(query)

    def get_context_data(self, **kwargs):
        context = super(ProjectManagersList, self).get_context_data(**kwargs)
        context['form'] = ProjectManagerForm()
        """может быть есть более быстрый и правильный способ добавить инфу о менеджере в объект по его manager_id"""
        for obj in context['object_list']:
            setattr(obj, 'manager_name', get_manager(obj.manager_id))
        return context

    





class CreateProjectManager(PermissionRequiredMixin, CreateView):
    model = ProjectManagers

class UpdateProjectManager(PermissionRequiredMixin, UpdateView):
    model = ProjectManagers

class DeleteProjectManager(PermissionRequiredMixin, UpdateView):
    model = ProjectManagers


# #  ------------------------------------ UPDATE PROJECT'S MANAGERS ----------------------------------------------
# class ProductManagersUpdate(PermissionRequiredMixin, UpdateView):
#     model = Project
#     form_class = ProjectManagerForm
#     permission_required = f'{model._meta.app_label}.change_{model.__name__}'
#     template_name = 'projectsapp/company_update.html'
#     request = None

#     def get_formset_class(self, formset=ProjectManagerUpdateFormset, extra=1, form=ProjectManagerForm, fk_name='project', **kwargs):
#         return inlineformset_factory(
#             self.model, ProjectManagerForm._meta.model, formset=formset, extra=extra, form=form, fk_name=fk_name)

#     def get_formset(self, **kwargs):
#         self.formset = self.get_formset_class(**kwargs)(
#             data=self.request and self.request.POST or None,
#             files=self.request and self.request.FILES or None,
#             instance=getattr(self, 'object', self.get_object()), initial=kwargs.get('initial', {}))
#         print("fomset: ", self.formset)
#         return self.formset

#     def form_valid(self, form, **kwargs):
#         response = super().form_valid(form)
#         if self.get_formset(**kwargs).is_valid():
#             self.formset.save()
#         print("===============================")
#         print("responce: ", response)
#         print("===============================")
#         return response

#     def get_context_data(self, **kwargs):
#         print("===============================")
#         print("context: ", super().get_context_data(formset1=self.get_formset(), **kwargs))
#         print("===============================")
#         return super().get_context_data(formset1=self.get_formset(), **kwargs)

# def project_managers_update(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     project_form = ProjectForm(instance=project)
#     managers_formset = inlineformset_factory(Project, ProjectManagers, form=ProjectManagerForm, extra=1)
#     formset = managers_formset(instance=project)
#     if request.method == 'POST':
#         project_form = ProjectForm(request.POST, instance=project)
#         formset = managers_formset(request.POST)
#         if project_form.is_valid():
#             updated_project = project_form.save(commit=False)
#             formset = managers_formset(request.POST, instance=updated_project)
#             if formset.is_valid():
#                 updated_project.save()
#                 formset.save()
#                 return HttpResponseRedirect(updated_project.get_absolute_url())
#     context = {
#         'project_form': project_form,
#         'formset': formset,
#         'page_title': 'Обновление списка участников',
#         'bred_title': 'Список участников',
#         'project': project
#     }
#     return render(request, 'projectsapp/company_update.html', context)


#  ------------------------------------ UPDATE PROJECT'S GALLERY ----------------------------------------------


def gallery_update(request, pk):
    project = Project.objects.get(pk=pk)
    project_form = ProjectForm(instance=project)
    BookInlineFormSet = inlineformset_factory(Project, ProjectImage, form=ProjectImageForm, extra=3)
    formset = BookInlineFormSet(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST, instance=project)
        formset = BookInlineFormSet(request.POST, request.FILES)
        if project_form.is_valid():
            created_project = project_form.save(commit=False)
            formset = BookInlineFormSet(request.POST, request.FILES, instance=created_project)
            if formset.is_valid():
                created_project.save()
                formset.save()
                return HttpResponseRedirect(created_project.get_absolute_url())
    context = {
        'project_form': project_form,
        'formset1': formset,
        'page_title': 'Добавление фотографий',
        'bred_title': 'Добавление фотографий',
        'project': project
    }
    return render(request, "projectsapp/gallery_update.html", context)
