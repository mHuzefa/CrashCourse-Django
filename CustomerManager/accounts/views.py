from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending
               }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)

def customers(request):
    return render(request, 'accounts/profiles.html')
