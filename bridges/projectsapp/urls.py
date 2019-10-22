"""bridges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from projectsapp import views as projectsapp
from .views import ProjectsList, ProjectRead

app_name = 'projectsapp'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects'),
    path('<int:pk>/', ProjectRead.as_view(), name='project'),
    path('update/<int:pk>', projectsapp.project_update, name='project_update'),
    # path('product/update/<int:pk>', projectsapp.project_solutions_update, name='product_update'),
    path('product/create/<int:project_pk>', projectsapp.ProjectsSolutionsCreateView.as_view(), name='product_create'),
    path('company/create/<int:project_pk>', projectsapp.ProjectsCompanyCreateView.as_view(), name='company_create'),
    path('company/delete/<int:pk>', projectsapp.ProjectsCompanyDeleteView.as_view(), name='company_delete'),
    path('gallery/update/<int:pk>', projectsapp.gallery_update, name='gallery_update'),
    path('manager/create/<int:project_pk>', projectsapp.ProjectsManagerCreateView.as_view(), name='manager_create'),
    path('manager/delete/<int:pk>', projectsapp.ProjectsManagerDeleteView.as_view(), name='manager_delete')
]
