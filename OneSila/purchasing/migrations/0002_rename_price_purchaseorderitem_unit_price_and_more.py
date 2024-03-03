# Generated by Django 4.2.9 on 2024-02-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchasing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorderitem',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='supplierproduct',
            name='unit_price',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
