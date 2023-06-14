from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
# Create your views here.

class PrductsView(ListView):
    template_name = "products/products.html"
    model = Product
    context_object_name = "products"
