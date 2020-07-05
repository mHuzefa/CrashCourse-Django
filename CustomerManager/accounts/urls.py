from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('create-order/', views.createOrder, name='create-order'),
    path('create-customer/', views.AddCustomer, name='create-customer'),
    path('update-order/<str:pk>/', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order'),
    path('update-customer/<str:pk>', views.updateCustomer, name='update-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),
    ]