# Generated by Django 5.0.2 on 2024-04-04 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_inventorylocation_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylocation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
