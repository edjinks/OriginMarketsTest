# Generated by Django 2.2.24 on 2021-10-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0011_bond_legal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bond',
            name='legal_name',
            field=models.CharField(default='AUTO FILLS FROM LEI', max_length=50),
        ),
    ]