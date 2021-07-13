from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def new_pr(request):
    return HttpResponse('New Products')


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        {
            'products': products
        }
    )


