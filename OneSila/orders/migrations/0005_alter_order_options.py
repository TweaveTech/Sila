# Generated by Django 5.0.2 on 2024-06-07 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
