# Generated by Django 5.1.1 on 2024-09-22 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magento2', '0014_alter_magentoattributesetattribute_remote_property'),
        ('sales_channels', '0023_alter_remotecategory_sales_channel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magentoattributeset',
            name='sales_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_channels.saleschannel'),
        ),
        migrations.AlterField(
            model_name='magentoattributesetattribute',
            name='sales_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_channels.saleschannel'),
        ),
    ]
