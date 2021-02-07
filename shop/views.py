from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Product
from .forms import ProductForm
from carton.cart import Cart


def index(request):
    products = Product.objects.order_by('-updated_at')
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def add(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(pk=product_id)
    cart.add(product, price=product.price)
    products = Product.objects.order_by('-updated_at')
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def remove(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(pk=product_id)
    cart.remove(product)
    return render(request, 'shop/show-cart.html')


def minus(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(pk=product_id)
    cart.remove_single(product)
    context = {
        "cart": cart
    }
    return render(request, 'shop/show-cart.html', context)


def plus(request, product_id):
    cart = Cart(request.session)
    product = Product.objects.get(pk=product_id)
    cart.add(product, price=product.price)
    context = {
        "cart": cart
    }
    return render(request, 'shop/show-cart.html', context)


def show(request):
    cart = Cart(request.session)
    context = {
        "cart": cart
    }
    return render(request, 'shop/show-cart.html', context)


def price(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get()
    default_single_price = product.price
    cart.price += default_single_price
