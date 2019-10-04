from django.contrib import admin
from django.urls import path
from ymapapp import views as ymapapp

app_name = 'ymapapp'

urlpatterns = [
    path('', ymapapp.map, name='map'),
    path('<slug:slug>', ymapapp.project, name='project'),
]
