# Generated by Django 5.1.1 on 2024-11-28 11:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0134_demodatarelation_created_by_multi_tenant_user_and_more'),
        ('products', '0036_billofmaterial_created_by_multi_tenant_user_and_more'),
        ('units', '0003_unit_created_by_multi_tenant_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SupplierPrices',
            new_name='SupplierPrice',
        ),
    ]
