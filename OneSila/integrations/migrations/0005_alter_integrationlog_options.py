# Generated by Django 5.1.1 on 2024-10-17 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_integrationlog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='integrationlog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Integration Log', 'verbose_name_plural': 'Integration Logs'},
        ),
    ]
