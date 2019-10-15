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

from .views import ProjectsList, ProjectRead, ProjectManagersUpdate, ProjectSolutionsUpdate, ProjectCompanyUpdate, \
    ProjectManagersDelete, ProjectCompanyDelete, ProjectSolutionsDelete

app_name = 'projectsapp'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects'),
    path('<int:pk>/', ProjectRead.as_view(), name='project'),
    path('manager/update', ProjectManagersUpdate.as_view(), name='manager_update'),
    path('manager/delete/<int:pk>', ProjectManagersDelete.as_view(), name='manager_delete'),
    path('product/update', ProjectSolutionsUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProjectSolutionsDelete.as_view(), name='product_delete'),
    path('company/update', ProjectCompanyUpdate.as_view(), name='company_update'),
    path('company/delete/<int:pk>', ProjectCompanyDelete.as_view(), name='company_delete'),
]
