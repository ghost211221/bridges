from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
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


# class ProjectSolutionsCreate(CreateView):
#     form_class = ProjectSolutionsForm
#     model = Project
#     success_url = reverse_lazy('projectsapp:projects')
#
#     def get_context_data(self, **kwargs):
#         data = super(ProjectSolutionsCreate, self).get_context_data(**kwargs)
#         OrderFormSet = inlineformset_factory(Project, ProjectHasTechnicalSolutions, form=ProjectSolutionsForm, extra=1)
#
#         if self.request.POST:
#             formset = OrderFormSet(self.request.POST)
#             data['projectsolutions'] = formset
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         projectsolutions = context['projectsolutions']
#
#         with transaction.atomic():
#             form.instance.user = self.request.user
#             self.object = form.save()
#             if projectsolutions.is_valid():
#                 projectsolutions.instance = self.object
#                 projectsolutions.save()

def product_create(request):

    if request.method == 'POST':
        order_form = ProjectSolutionsForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('/')
    else:
        order_form = ProjectSolutionsForm()
    context = {
        'order_form': order_form,
    }
    return render(request, 'projectsapp/project_form.html', context)


class ProjectDelete(DeleteView):
    pass


# def product_create(request):
#     order = Project()
#     order_form = ProjectForm(instance=order)
#     OrderInlineFormSet = inlineformset_factory(Project, ProjectHasTechnicalSolutions, form=ProjectSolutionsForm, extra=1)
#     if request.method == 'POST':
#         order_form = ProjectForm(request.POST)
#         formset = OrderInlineFormSet(request.POST)
#         if order_form.is_valid():
#             created_form = order_form.save(commit=False)
#             created_form.user = request.user
#             formset = OrderInlineFormSet(request.POST, instance=created_form)
#             if formset.is_valid():
#                 created_form.save()
#                 formset.save()
#                 return redirect('/')
#     else:
#         order_form = ProjectForm()
#         formset = OrderInlineFormSet()
#     context = {
#         'order_form': order_form,
#         'orderitems': formset
#     }
#     return render(request, 'projectsapp/project_form.html', context)