# Generated by Django 5.0.2 on 2024-03-11 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_producttranslation_url_key'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together={('product', 'language')},
        ),
    ]
