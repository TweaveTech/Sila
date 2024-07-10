# Generated by Django 5.0.2 on 2024-06-06 17:01

from django.db import migrations

def forwards_func(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    Product.objects.filter(type='VARIATION').update(type='SIMPLE')

def reverse_func(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    Product.objects.filter(type='SIMPLE').update(type='VARIATION')

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_unique_sku_with_supplier_and_more'),
    ]

    operations = [
       migrations.RunPython(forwards_func, reverse_func),
    ]
