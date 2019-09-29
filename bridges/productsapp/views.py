from django.shortcuts import render
from productsapp.models import TechnicalSolutions


def products(request):
    title = "Технические решения"
    technical_solutions = TechnicalSolutions.objects.all()

    content = {'page_title': title, 'products': technical_solutions}
    return render(request, 'productsapp/products.html', content)
