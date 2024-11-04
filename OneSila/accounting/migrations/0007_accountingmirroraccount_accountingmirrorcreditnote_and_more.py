# Generated by Django 5.1.1 on 2024-10-20 11:10

import dirtyfields.dirtyfields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_creditnote_total_invoice_total'),
        ('contacts', '0023_alter_address_options_and_more'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0134_demodatarelation_created_by_multi_tenant_user_and_more'),
        ('integrations', '0008_alter_integration_internal_company'),
        ('taxes', '0007_vatrate_created_by_multi_tenant_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingMirrorAccount',
            fields=[
                ('integration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integrations.integration')),
                ('due_days', models.IntegerField(blank=True, help_text='The number of days before payment is due.', null=True)),
                ('invoice_layout', models.FileField(blank=True, help_text='The invoice layout PDF.', null=True, upload_to='invoices/')),
            ],
            options={
                'verbose_name': 'AccountingMirror Account',
                'verbose_name_plural': 'AccountingMirror Accounts',
            },
            bases=('integrations.integration',),
        ),
        migrations.CreateModel(
            name='AccountingMirrorCreditNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remote_id', models.CharField(blank=True, help_text='ID of the object in the remote system.', max_length=255, null=True)),
                ('created_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('last_update_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_update_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('local_instance', models.ForeignKey(help_text='The local credit note associated with this AccountingMirror credit note.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.creditnote')),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('remote_account', models.ForeignKey(help_text='The remote account associated with this object.', on_delete=django.db.models.deletion.CASCADE, to='accounting.accountingmirroraccount')),
            ],
            options={
                'verbose_name': 'AccountingMirror Credit Note',
                'verbose_name_plural': 'AccountingMirror Credit Notes',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AccountingMirrorCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remote_id', models.CharField(blank=True, help_text='ID of the object in the remote system.', max_length=255, null=True)),
                ('created_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('last_update_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_update_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('local_instance', models.ForeignKey(help_text='The local customer associated with this AccountingMirror customer.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.company')),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('remote_account', models.ForeignKey(help_text='The remote account associated with this object.', on_delete=django.db.models.deletion.CASCADE, to='accounting.accountingmirroraccount')),
            ],
            options={
                'verbose_name': 'AccountingMirror Customer',
                'verbose_name_plural': 'AccountingMirror Customers',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AccountingMirrorInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remote_id', models.CharField(blank=True, help_text='ID of the object in the remote system.', max_length=255, null=True)),
                ('created_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('last_update_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_update_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('local_instance', models.ForeignKey(help_text='The local invoice associated with this AccountingMirror invoice.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.invoice')),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('remote_account', models.ForeignKey(help_text='The remote account associated with this object.', on_delete=django.db.models.deletion.CASCADE, to='accounting.accountingmirroraccount')),
            ],
            options={
                'verbose_name': 'AccountingMirror Invoice',
                'verbose_name_plural': 'AccountingMirror Invoices',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AccountingMirrorVat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remote_id', models.CharField(blank=True, help_text='ID of the object in the remote system.', max_length=255, null=True)),
                ('created_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('last_update_by_multi_tenant_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_update_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL)),
                ('local_instance', models.ForeignKey(help_text='The local VAT rate associated with this AccountingMirror VAT.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxes.vatrate')),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.multitenantcompany')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('remote_account', models.ForeignKey(help_text='The remote account associated with this object.', on_delete=django.db.models.deletion.CASCADE, to='accounting.accountingmirroraccount')),
            ],
            options={
                'verbose_name': 'AccountingMirror VAT',
                'verbose_name_plural': 'AccountingMirror VATs',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
