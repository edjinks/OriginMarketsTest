# Generated by Django 2.2.24 on 2021-10-15 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0009_bond_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bond',
            name='legal_name',
        ),
    ]
