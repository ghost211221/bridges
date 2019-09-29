from django.shortcuts import render


def products(request):
    context = {
        'page_title': 'технологии',
    }
    return render(request, 'productsapp/products.html', context)
