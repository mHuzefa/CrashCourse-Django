from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import *
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending,
               }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    total_order = customer.order_set.all()
    order_count = total_order.count()
    context = {'customer': customer, 'order': order, 'order_count': order_count}
    return render(request, 'accounts/profiles.html', context)


def createOrder(request):

    form = OrderForm()
    context = {'form':form}

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/OrderForm.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/OrderForm.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)



def AddCustomer(request,):
    Cform = CustomerForm()
    context={'Cform': Cform}

    if request.method == 'POST':
        Cform = CustomerForm(request.POST)
        if Cform.is_valid():
            Cform.save()
            return redirect('/')
    return render(request,'accounts/CustomerForm.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    context = {'Cform': form}
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/CustomerForm.html', context)


def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'customer': customer}
    return render(request, 'accounts/deleteCustomer.html', context)