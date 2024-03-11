# Generated by Django 5.0.2 on 2024-03-04 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_address_contact'),
        ('purchasing', '0003_rename_delivery_address_purchaseorder_shipping_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipping_address_set', to='contacts.shippingaddress'),
        ),
    ]
