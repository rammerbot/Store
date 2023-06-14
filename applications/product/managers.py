from django.db import models


# Manager para los productos
class ProductManaget(models.Manager):

    # Obtener productos
    def product_get(self, id):
        product = self.get(id=id)
        return product