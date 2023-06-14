from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel

from applications.product.models import Product
from .managers import CartManager

# Create your models here.

class Cart(TimeStampedModel):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="CartItem")
    objects = CartManager()

    def __str__(self) -> str:
        return f"Carrito: {self.pk} - Usuario: {self.user.username}"

    def total_price(self):
        total = 0

        for item in self.caritem_set.all():
            total += item.quantity * item.product.price
        
        return total

class CartItem(TimeStampedModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Cantidad', default=1)

    def __str__(self) -> str:
        return f"{self.product.name} x {self.quantity}"