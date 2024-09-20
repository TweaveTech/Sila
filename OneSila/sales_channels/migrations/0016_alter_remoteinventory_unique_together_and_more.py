# Generated by Django 5.1.1 on 2024-09-17 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_channels', '0015_remoteproductconfigurator_remote_product_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='remoteinventory',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='remoteprice',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='remoteproductcontent',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='remoteinventory',
            name='remote_product',
        ),
        migrations.RemoveField(
            model_name='remoteprice',
            name='remote_product',
        ),
        migrations.RemoveField(
            model_name='remoteproductcontent',
            name='remote_product',
        ),
    ]
