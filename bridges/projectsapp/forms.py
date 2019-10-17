from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'city', 'address', 'coordinate', 'description', 'is_active']


class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManagers
        fields = ['manager', 'role']


class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions
        fields = ['techsol', 'name', 'value']


class ProjectCompanyForm(forms.ModelForm):
    class Meta:
        model = ProjectCompany
        fields = ['company', 'role']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']
