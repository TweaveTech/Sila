# Generated by Django 5.0.2 on 2024-07-15 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0112_alter_multitenantuser_timezone'),
        ('eancodes', '0002_delete_all_eancodes'),
        ('products', '0024_remove_product_base_product_product_base_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='eancode',
            name='already_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eancode',
            name='inherit_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='inherited_ean_codes', to='products.supplierproduct'),
        ),
        migrations.AddField(
            model_name='eancode',
            name='internal',
            field=models.BooleanField(default=True, help_text='Generated from the prefix'),
        ),
        migrations.AlterField(
            model_name='eancode',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='eancode',
            unique_together={('product', 'ean_code', 'inherit_from')},
        ),
        migrations.AddConstraint(
            model_name='eancode',
            constraint=models.UniqueConstraint(condition=models.Q(('ean_code__isnull', False)), fields=('ean_code',), name='unique_ean_code_per_tenant'),
        ),
        migrations.AddConstraint(
            model_name='eancode',
            constraint=models.CheckConstraint(check=models.Q(('ean_code__isnull', False), ('inherit_from__isnull', False),
                                              _connector='OR'), name='ean_code_or_inherit_from_not_null'),
        ),
    ]
