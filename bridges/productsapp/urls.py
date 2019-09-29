from django.contrib import admin
from django.urls import path
from productsapp import views as productsapp


app_name = 'productsapp'

urlpatterns = [
    path('', productsapp.products, name='products'),
    path('products/<int:pk>/', productsapp.products, name='product'),
]
