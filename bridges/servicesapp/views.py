from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *


@login_required
def service_list(request):
    services = Service.objects.all().exclude(is_active=False)
    context ={
        'service_list': services,
    }
    return render(request, 'serviceapp/service_list.html', context)


@login_required
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {
        'service_detail': service,
    }
    return render(request, 'serviceapp/service_detail.html', context)
