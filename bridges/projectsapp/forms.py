from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManagers
        fields = ['role', 'manager', 'project']


class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions
        fields = ['name', 'techsol', 'value']


class ProjectCompanyForm(forms.ModelForm):
    class Meta:
        model = ProjectCompany
        fields = ['company', 'role', 'project']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']
