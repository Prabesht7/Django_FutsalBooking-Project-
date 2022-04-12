from django.shortcuts import render, redirect
from Shopping.models.product import Product
from Shopping.models.orders import Order


def charts(request):
    product = Product.objects.all()
    order = Order.objects.all()
    context = {
        'order': order,
        'product': product,
    }
    return render(request, 'charts.html', context)
