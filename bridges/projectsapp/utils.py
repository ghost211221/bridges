from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from authapp.models import Users
from projectsapp.forms import ProjectManagerCreateForm
from projectsapp.models import Project, ProjectManagers


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('projectsapp:projects')
        return render(request, self.template, context={'form': bound_form})


class CreateMixin:
    form_model = None
    form = None
    template = None

    def get(self, request, project_pk):
        project = Project.objects.get(pk=project_pk)
        form = self.form(initial={"project": project})
        context = {
            'project_manager_form': form
        }
        return render(request, template_name=self.template, context=context)

    def post(self, request, project_pk):
        project = Project.objects.get(pk=project_pk)
        form = self.form(request.POST)
        if form.is_valid():
            hacked = {
                "project": Project.objects.get(pk=form.data["project"]),
                "manager": Users.objects.get(pk=form.data["manager"])
            }
            data = {**form.data, **hacked}
            data = {k: v[0] if isinstance(v, list) else v for k, v in data.items() if
                    k in {f.name for f in self.form_model._meta.fields}}
            data['is_active'] = True if data['is_active'] == 'on' else False
            obj = self.form_model(**data)
            obj.save()
            return HttpResponseRedirect(project.get_absolute_url())
        return HttpResponse(status=400)
