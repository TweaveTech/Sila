# Generated by Django 5.0.7 on 2024-08-11 15:49

import core.validators
import dirtyfields.dirtyfields
import django.db.models.deletion
import shipments.models_helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0019_internalshippingaddress'),
        ('core', '0133_alter_multitenantuser_timezone'),
        ('orders', '0005_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('BOX', 'Box'), ('PALLET', 'Pallet')], max_length=6)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('IN_PROGRESS', 'In Progress'),
                 ('PACKAGED', 'Packaged'), ('DISPATCHED', 'Dispatched')], default='NEW', max_length=11)),
                ('tracking_code', models.CharField(blank=True, max_length=254, null=True)),
                ('tracking_link', models.URLField(blank=True, max_length=254, null=True)),
                ('shipping_label', models.FileField(blank=True, null=True,
                 upload_to=shipments.models_helpers.get_shippinglabel_folder_upload_path, validators=[core.validators.validate_pdf_extension])),
                ('customs_document', models.FileField(blank=True, null=True,
                 upload_to=shipments.models_helpers.get_customs_document_folder_upload_path, validators=[core.validators.validate_pdf_extension])),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qty', models.IntegerField()),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipments.package')),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments_from', to='contacts.shippingaddress')),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.order')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments_to', to='contacts.shippingaddress')),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='package',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shipments.shipment'),
        ),
    ]
