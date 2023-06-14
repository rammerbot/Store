from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField

# Create your models here.

class Product(TimeStampedModel):
    name = models.CharField('Producto', max_length=40)
    price = models.DecimalField('Precio',max_digits=10, decimal_places=2)
    description = RichTextField('Descripcion')
    image = models.ImageField('Imagen', upload_to="img-product")

    def __str__(self):
        return self.name
    