from django.urls import path
from projectsapp import views as projectsapp
from .views import ProjectsList, ProjectRead

app_name = 'projectsapp'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects'),
    path('<int:pk>/', ProjectRead.as_view(), name='project'),
    path('update/<int:pk>', projectsapp.project_update, name='project_update'),
    path('manager/update/<int:pk>', projectsapp.project_managers_update, name='manager_update'),
    path('product/update/<int:pk>', projectsapp.project_solutions_update, name='product_update'),
    path('company/update/<int:pk>', projectsapp.company_update, name='company_update'),
    path('gallery/update/<int:pk>', projectsapp.gallery_update, name='gallery_update'),
    path('discuss/items/<int:pk>', projectsapp.project_discuss_items, name='project_discuss_items'),
    path('discuss/edit/members/<int:pk>', projectsapp.project_discuss_edit_members,name='project_discuss_edit_members'),
]
