from django.shortcuts import render
from .models import Products, ProductCategory


def index(request):
    context = {
        'title': 'Store',
        'is_promotion': False,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Shope - Products',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
