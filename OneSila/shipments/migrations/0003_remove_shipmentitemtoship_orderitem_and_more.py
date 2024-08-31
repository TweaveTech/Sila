# Generated by Django 5.0.7 on 2024-08-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_shipment_status_shipmentitemtoship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('TODO', 'Todo'), ('IN_PROGRESS', 'In Progress'),
                                   ('DONE', 'Done'), ('CANCELLED', 'Cancelled')], default='DRAFT', max_length=11),
        ),
    ]
