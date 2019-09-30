from django.shortcuts import render, get_object_or_404
from productsapp.models import TechnicalSolutions


def products(request):
    title = "Технические решения"
    technical_solutions = TechnicalSolutions.objects.all()
    # all_products = Product.objects.filter(category__slug=slug).exclude(is_active=False)

    content = {
        'page_title': title,
        'products': technical_solutions
    }
    return render(request, 'productsapp/products.html', content)


def product(request, pk):
    title = "Технические решения"
    item = get_object_or_404(TechnicalSolutions, pk=pk)
    # all_products = Product.objects.filter(category__slug=slug).exclude(is_active=False)

    content = {
        'page_title': title,
        'product': item
    }
    return render(request, 'productsapp/product.html', content)


# def product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'page_title': 'страница продукта',
#         'products_menu': get_products_menu(),
#         'category': product.category,
#         'object': product,
#     }
#     return render(request, 'mainapp/product_page.html', context)
