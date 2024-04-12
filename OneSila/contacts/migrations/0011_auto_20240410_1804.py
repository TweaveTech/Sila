# Generated by Django 5.0.2 on 2024-04-10 17:04

from django.db import migrations


def contact_to_people(apps, schema_editor):
    Address = apps.get_model('contacts', 'Address')
    Person = apps.get_model('contacts', 'Address')

    for address in Address.objects.filter(contact__isnull=False):
        address.people.add(address.contact)


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_remove_company_eori_number_and_more'),
    ]

    operations = [
        migrations.RunPython(contact_to_people)
    ]
