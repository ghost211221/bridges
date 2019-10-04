from django.shortcuts import render


def research(request):
    return render(request, 'researchapp/research.html')
