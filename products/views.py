from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Product, ProductType

def products(request):
    products = Product.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'products/products.html', context)