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


class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions
        fields = ['techsol', 'name', 'value']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']


class ProjectManagerCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectManagers
        fields = '__all__'


class ProjectCompanyCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectCompany
        fields = '__all__'


class ProjectSolutionsCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectHasTechnicalSolutions
        fields = '__all__'


class ProjectDiscussItemForm(forms.ModelForm):
    class Meta:
        model = ProjectDiscussItem
        fields = ['comment']


class ProjectDiscussMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectDiscussMember
        fields = '__all__'
