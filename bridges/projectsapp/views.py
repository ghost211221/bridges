
from django.views.generic import View

from django.views.generic import ListView, DetailView

from projectsapp.forms import ProjectSolutionsForm, ProjectManagerForm, ProjectCompanyForm
from projectsapp.models import Project, ProjectHasTechnicalSolutions, ProjectCompany, ProjectManagers

from projectsapp.utils import ObjectCreateMixin, ObjectDeleteMixin


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


#  ------------------------------------ CRUD PROJECT'S SOLUTIONS ----------------------------------------------


class ProjectSolutionsUpdate(ObjectCreateMixin, View):
    form_model = ProjectSolutionsForm
    template = 'projectsapp/product_update.html'


class ProjectSolutionsDelete(ObjectDeleteMixin, View):
    model = ProjectHasTechnicalSolutions
    template = 'projectsapp/solution_delete_form.html'
    context = 'solutions'


#  ------------------------------------ CRUD PROJECT'S COMPANIES ----------------------------------------------


class ProjectCompanyUpdate(ObjectCreateMixin, View):
    form_model = ProjectCompanyForm
    template = 'projectsapp/company_update.html'


class ProjectCompanyDelete(ObjectDeleteMixin, View):
    model = ProjectCompany
    template = 'projectsapp/company_delete_form.html'
    context = 'companies'


#  ------------------------------------ CRUD PROJECT'S MANAGERS ----------------------------------------------


class ProjectManagersUpdate(ObjectCreateMixin, View):
    form_model = ProjectManagerForm
    template = 'projectsapp/manager_update.html'


class ProjectManagersDelete(ObjectDeleteMixin, View):
    model = ProjectManagers
    template = 'projectsapp/manager_delete_form.html'
    context = 'managers'


