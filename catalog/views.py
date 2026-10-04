from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)
