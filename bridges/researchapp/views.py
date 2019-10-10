from django.shortcuts import render

from authapp.models import Company
from researchapp.models import Document


def research(request):
    title = 'Научно-исследовательские работы, публикации и заключения'
    bred_title = 'Исследовательские работы'
    documents = Document.objects.filter(type_id__in=(2, 3,)).order_by('-company').values('company__name',
                                                                                         'company__logo',
                                                                                         'company__form__name',
                                                                                         'file__file', 'pk', 'name',
                                                                                         'type_id', 'description')
    companies = documents.distinct('company__name')

    content = {
        'companies': companies,
        'documents': documents,
        'page_title': title,
        'bred_title': bred_title
    }

    return render(request, 'researchapp/research.html', content)
