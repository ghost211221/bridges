from django.shortcuts import render

from researchapp.models import Document


def research(request):
    researches = Document.objects.all().exclude(type__id=1)
    documents = Document.objects.all().exclude(type__in=[2, 3])

    # documents = Document.objects.filter(author__in=[1,]).exclude(type__id=2)
    # documents = Document.objects.all()

    content = {
        'researches': researches,
        'documents': documents,
    }

    return render(request, 'researchapp/research.html', content)
