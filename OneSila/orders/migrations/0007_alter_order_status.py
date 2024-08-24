# Generated by Django 5.0.7 on 2024-08-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_reason_for_sale_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PENDING_PROCESSING', 'Pending Processing'), ('PENDING_APPROVE_SHIPPING', 'Pending Shipping Approval'), ('PENDING_MANUAL_SHIPPING_APPROVAL',
                                   'Pending Manual Shipping Approval'), ('TO_SHIP', 'To Ship'), ('AWAIT_INVENTORY', 'Awaiting Inventory'), ('SHIPPED', 'Shipped'), ('CANCELLED', 'Cancelled'), ('HOLD', 'On Hold')], default='DRAFT', max_length=32),
        ),
    ]
