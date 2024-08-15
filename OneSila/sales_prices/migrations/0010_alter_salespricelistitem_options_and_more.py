# Generated by Django 5.0.7 on 2024-07-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0130_alter_multitenantuser_timezone'),
        ('currencies', '0009_currency_unique_iso_code_multi_tenant_company'),
        ('products', '0024_remove_product_base_product_product_base_products'),
        ('sales_prices', '0009_rename_discount_auto_salespricelist_discount_pcnt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salespricelistitem',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterUniqueTogether(
            name='salesprice',
            unique_together={('product', 'currency', 'multi_tenant_company')},
        ),
        migrations.AlterField(
            model_name='salesprice',
            name='rrp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Reccomended Retail Price'),
        ),
        migrations.AlterUniqueTogether(
            name='salespricelistitem',
            unique_together={('product', 'salespricelist', 'multi_tenant_company')},
        ),
    ]
