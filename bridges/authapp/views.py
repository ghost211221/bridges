from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from projectsapp.models import ProjectManagers
from .forms import *
from .models import *


@login_required
def restricted_area(request):
    user = request.user
    user_companies = CompanyUsers.objects.filter(user_id=user.pk)
    user_projects = ProjectManagers.objects.filter(manager_id=user.pk)
    context = {
        'section': 'restricted_area',
        'page_title': 'Личный кабинет',
        'bred_title': 'Личный кабинет',
        'user_companies': user_companies,
        'user_projects': user_projects,
    }
    return render(request, 'authapp/restricted_area.html', context)


def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = False
            new_user.save()
            return render(request, 'authapp/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterUserForm()
    return render(request, 'authapp/register.html', {'form': user_form})



    # class RegisterUserView(CreateView):
    #     model = Users
    #     form_class = RegisterUserForm
    #     extra_context = {
    #         'page_title': 'Регистрация на сайте',
    #         'bred_title': 'Регистрация'
    #     }
    #     template_name = 'authapp/register1.html'
    #     success_url = reverse_lazy('auth:login')
    #
    #
    # class UserLoginView(LoginView):
    #     authentication_form = LoginUserForm
    #     extra_context = {
    #         'page_title': 'Авторизация на сайте',
    #         'bred_title': 'Авторизация'
    #     }
    #     template_name = 'authapp/1_login.html'
    #

    # class UserProfileView(DetailView):
    #     model = Users
    #     extra_context = {
    #         'page_title': 'Профиль пользователя',
    #         'bred_title': 'Профиль пользователя'
    #     }
    #     template_name = 'authapp/profile.html'
    #
    #     def get_context_data(self, *args, **kwargs):
    #         context = super().get_context_data(*args, **kwargs)
    #         return context

    # def profile(request, pk):
    #     user_companies = CompanyUsers.objects.filter(user_id=pk)
    #     user = get_object_or_404(Users, pk=pk)
    #     user_projects = ProjectManagers.objects.filter(manager_id=pk)
    #     context = {
    #         'user': user,
    #         'user_projects': user_projects,
    #         'user_companies': user_companies,
    #         'page_title': 'Профиль пользователя',
    #         'bred_title': 'Профиль пользователя'
    #     }
    #     return render(request, 'authapp/profile.html', context)
    #
    #
    # class UserLogoutView(LogoutView):
    #     extra_context = {
    #         'page_title': 'Выход с сайта',
    #         'bred_title': 'Выход с сайта'
    #     }
    #     template_name = 'authapp/1_logout.html'


def company_self_user_update(request, pk):
    company_user = get_object_or_404(Users, pk=pk)
    company_user_form = UsersForCompanyUsersForm(instance=company_user)
    InlineFormset = inlineformset_factory(Users, CompanyUsers, form=CompanyUsersForm, extra=1)
    formset = InlineFormset(instance=company_user)
    if request.method == 'POST':
        company_user_form = UsersForCompanyUsersForm(request.POST, instance=company_user)
        formset = InlineFormset(request.POST)
        if company_user_form.is_valid():
            updated_company_user_form = company_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_company_user_form)
            if formset.is_valid():
                updated_company_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_company_user_form.get_self_absolute_url())
    context = {
        'form': company_user_form,
        'formset': formset,
        'user': company_user,
        'page_title': 'Редактор компаний пользователя',
        'bred_title': 'Редактор компаний пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)


def profile_self_user_update(request, pk):
    user = get_object_or_404(Users, pk=pk)
    user_form = UsersForEditProfileForm(instance=user)
    if request.method == 'POST':
        user_form = UsersForEditProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(user.get_self_absolute_url())
    context ={
        'form': user_form,
        'page_title': 'Редактор профиля пользователя',
        'bred_title': 'Редактор профиля пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)


def project_self_user_update(request, pk):
    project_user = get_object_or_404(Users, pk=pk)
    project_user_form = UsersForProjectManagersForm(instance=project_user)
    InlineFormset = inlineformset_factory(Users, ProjectManagers, form=ProjectManagersForm, extra=1)
    formset = InlineFormset(instance=project_user)
    if request.method == 'POST':
        project_user_form = UsersForCompanyUsersForm(request.POST, instance=project_user)
        formset = InlineFormset(request.POST)
        if project_user_form.is_valid():
            updated_project_user_form = project_user_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_project_user_form)
            if formset.is_valid():
                updated_project_user_form.save()
                formset.save()
                return HttpResponseRedirect(updated_project_user_form.get_self_absolute_url())
    context = {
        'form': project_user_form,
        'formset': formset,
        'page_title': 'Редактор проектов пользователя',
        'bred_title': 'Редактор проектов пользователя'
    }
    return render(request, 'authapp/self_profile_update.html', context)
