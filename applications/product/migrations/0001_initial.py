# Generated by Django 4.2.2 on 2023-06-14 16:12

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=40, verbose_name='Producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='img-product', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
