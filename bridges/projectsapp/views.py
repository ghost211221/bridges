from django.contrib.auth.decorators import user_passes_test, login_required
from django.forms import inlineformset_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from projectsapp.utils import CreateMixin, DeleteMixin
from .forms import *
from projectsapp.models import ProjectImage, ProjectManagers
from django.views.generic import View
from django.views.generic import ListView, DetailView
from projectsapp.models import Project, ProjectHasTechnicalSolutions, ProjectCompany


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


#  ------------------------------------ PROJECT'S DETAILS ----------------------------------------------


@user_passes_test(lambda u: u.is_superuser)
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


#  ------------------------------------ PROJECT'S SOLUTIONS ----------------------------------------------


class ProjectsSolutionsCreateView(CreateMixin, View):
    form_model = ProjectHasTechnicalSolutions
    form = ProjectSolutionsCreateForm
    template = 'projectsapp/projectsolutions_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'techsol'
    viriable_model = TechnicalSolutions


class ProjectsSolutionsDeleteView(DeleteMixin, View):
    form_model = ProjectHasTechnicalSolutions
    template = 'projectsapp/projectmanagers_confirm_delete.html'


#  ------------------------------------ PROJECT'S COMPANIES ----------------------------------------------


class ProjectsCompanyCreateView(CreateMixin, View):
    form_model = ProjectCompany
    form = ProjectCompanyCreateForm
    template = 'projectsapp/projectcompany_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'company'
    viriable_model = Company


class ProjectsCompanyDeleteView(DeleteMixin, View):
    form_model = ProjectCompany
    template = 'projectsapp/projectmanagers_confirm_delete.html'


#  ------------------------------------ PROJECT'S MANAGERS ----------------------------------------------

class ProjectsManagerCreateView(CreateMixin, View):
    form_model = ProjectManagers
    form = ProjectManagerCreateForm
    template = 'projectsapp/projectmanagers_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'manager'
    viriable_model = Users


class ProjectsManagerDeleteView(DeleteMixin, View):
    form_model = ProjectManagers
    template = 'projectsapp/projectmanagers_confirm_delete.html'


#  ------------------------------------ PROJECT'S GALLERY ----------------------------------------------


@user_passes_test(lambda u: u.is_superuser)
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
        'formset': formset,
        'page_title': 'Добавление фотографий',
        'bred_title': 'Добавление фотографий',
        'project': project
    }
    return render(request, "projectsapp/gallery_update.html", context)


def project_discuss_items(request, pk):
    project = Project.objects.get(pk=pk)
    project_discuss_items = ProjectDiscussItem.objects.filter(project_id=pk)
    discuss_users = ProjectDiscussMember.objects.filter(project_id=pk)
    self_user = request.user
    if discuss_users.filter(user=self_user).exists():
        if request.method == 'POST':
            report_form = ProjectDiscussItemForm(data=request.POST)
            if report_form.is_valid():
                new_report_form = report_form.save(commit=False)
                new_report_form.project = project
                new_report_form.user = request.user
                new_report_form.save()
                return redirect(project.get_absolute_discuss_url())
        else:
            report_form = ProjectDiscussItemForm()
        context = {
            'object': project,
            'project_discuss_items': project_discuss_items,
            'discuss_users': discuss_users,
            'form': report_form,
            'page_title': 'Обсуждение проекта',
            'bred_title': 'Обсуждение проекта',
        }
        return render(request, 'projectsapp/project_discuss_detail.html', context)
    else:
        context = {
            'page_title': 'Доступ запрещен',
        }
        return render(request, 'projectsapp/project_access_denied.html', context)


def project_discuss_edit_members(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectForm(instance=project)
    InlineFormset = inlineformset_factory(Project, ProjectDiscussMember, form=ProjectDiscussMemberForm, extra=1)
    formset = InlineFormset(instance=project)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        formset = InlineFormset(request.POST)
        if project_form.is_valid():
            updated_project_form = project_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_project_form)
            if formset.is_valid():
                updated_project_form.save()
                formset.save()
                return HttpResponseRedirect(project.get_absolute_discuss_url())
    context = {
        'project': project,
        'form': project_form,
        'formset': formset,
        'page_title': 'Редактирование участников проекта',
        'bred_title': 'Редактирование участников проекта',
    }
    return render(request, 'projectsapp/discuss_members_update.html', context)
