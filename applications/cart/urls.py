from django.contrib import admin
from django.urls import path
from . import views

app_name = "app_cart"
urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/',views.AddToCartView.as_view(), name='add_to_cart'),
    path('delete_item/', views.DeleteProduct.as_view(), name='detele_item')

]
