from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Sum, F

from .models import Cart, CartItem
from applications.product.models import Product
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class CartView(TemplateView):
    template_name = "cart/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.select_related('product').annotate(total_quantity=Sum('quantity'),total_price=Sum(F('quantity') * F('product__price')))
        for item in cart_items:
            print(item)
        context["cart_items"]= cart_items
        return context
    
class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        user =self.request.user
        product_id = request.GET.get('product_id')
        quantity = request.GET.get('quantity')
        cart, created = Cart.objects.get_or_create(user=user)
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        messages.success(self.request, "Se Agrego producto al carrito")
        return redirect(reverse_lazy('app_product:products'))


class DeleteProduct(View):
    def post(self, request, *args, **kwargs):
        user =self.request.user
        product_id = self.request.POST.get('product_id')
        cart = Cart.objects.get(user=user)
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
        except CartItem.DoesNotExist:
            return redirect(reverse_lazy('app_cart:cart'))

        cart_item.delete()
        messages.error(self.request, "Eliminación de producto exitosa")
        
        return redirect(reverse_lazy('app_cart:cart'))
     