from django.shortcuts import render, get_object_or_404
from productsapp.models import TechnicalSolutions, Material
from projectsapp.models import ProjectHasTechnicalSolutions
from projectsapp.models import Project
from researchapp.models import Document


def products(request):
    title = "Технические решения"
    technical_solutions = TechnicalSolutions.objects.all()
    # all_products = Product.objects.filter(category__slug=slug).exclude(is_active=False)

    content = {
        'page_title': title,
        'products': technical_solutions
    }
    return render(request, 'productsapp/products.html', content)


def product(request, slug):
    title = "Технические решения"
    item = get_object_or_404(TechnicalSolutions, slug=slug)
    material_list = item.material_content.all()
    project_list = ProjectHasTechnicalSolutions.objects.filter(techsol__pk=item.pk)
    researches = Document.objects.filter(techsol__pk=item.pk).exclude(type__id=1)
    documents = Document.objects.filter(techsol__pk=item.pk).exclude(type__in=[2, 3])

    content = {
        'page_title': title,
        'product': item,
        'material_list': material_list,
        'projects': project_list,
        'researches': researches,
        'documents': documents
    }
    return render(request, 'productsapp/product.html', content)
