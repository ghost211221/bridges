from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, UpdateView

from django.views.generic import ListView, CreateView, DeleteView, DetailView

from productsapp.models import TechnicalSolutions
from projectsapp.forms import ProjectSolutionsForm, ProjectManagerForm, ProjectCompanyForm
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


class ProjectManagersDelete(View):
    def get(self, request, pk):
        managers = ProjectManagers.objects.get(pk=pk)
        return render(request, 'projectsapp/manager_delete_form.html', context={'managers': managers})

    def post(self, request, pk):
        managers = ProjectManagers.objects.get(pk=pk)
        managers.delete()
        return redirect(reverse('projectsapp:projects'))


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

