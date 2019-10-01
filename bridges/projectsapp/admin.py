from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin:
    list_display = ('name', 'city',)
    list_display_links = ('name', 'city',)
    search_fields = ('name',)
