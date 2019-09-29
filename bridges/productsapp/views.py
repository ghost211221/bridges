from django.shortcuts import render


def products(request):
    title = "Технические решения"
    technical_solutions = TechnicalSolutions.objects.all()

    content = {'title': title, 'products': technical_solutions}
    return render(request, 'productsapp/products.html', content)
