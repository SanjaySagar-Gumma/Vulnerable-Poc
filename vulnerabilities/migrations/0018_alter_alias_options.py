# Generated by Django 4.0.6 on 2022-08-18 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0017_delete_reference_to_cpes_with_empty_urls'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alias',
            options={'ordering': ['alias']},
        ),
    ]
