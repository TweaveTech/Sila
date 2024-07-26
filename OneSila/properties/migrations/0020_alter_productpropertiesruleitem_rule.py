# Generated by Django 5.0.7 on 2024-07-26 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0019_alter_productpropertiesrule_product_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpropertiesruleitem',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items',
                                    to='properties.productpropertiesrule', verbose_name='Rule'),
        ),
    ]
