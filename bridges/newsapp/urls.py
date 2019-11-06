from django.urls import path
from .views import NewsListView
from .views import NewsDetailView
# from .views import NewsCreateView
# from .views import NewsDeleteView
# from .views import NewsUpdateView

from .views import CreateDiscussItem

app_name = 'newsapp'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    # из админки
    # path('update/<int:pk>', NewsUpdateView.as_view(), name='news_supdate'),
    # path('create/<int:news_pk>', NewsCreateView.as_view(), name='news_create'),
    # path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    
    path('discuss/items/<int:pk>', CreateDiscussItem.as_view(), name='project_discuss_items'),
    # path('discuss/edit/members/<int:pk>', projectsapp.project_discuss_edit_members,
         # name='project_discuss_edit_members'),
]
