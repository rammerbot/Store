from django.db import models

# Manager para el Carrito
class CartManager(models.Manager):

    # Crear u obtener carrito
    def start_cart(self, user):
        cart = self.get(user=user)
        if cart:
            return cart
        else:
            cart = self.create(user=user)
        return cart

# Manager de items en el carrito
class CartItem(models.Manager):

    # Agregar items
    def add_to_card(self, cart, product, quantity):
        cartitem = self.create(cart=cart, product=product, quantity=quantity)
        return cartitem
    
    # Eliminar Items
    def delete_item(self, pk):
        cart_item_del = self.get(id=pk)
        cart_item_del.delete()
