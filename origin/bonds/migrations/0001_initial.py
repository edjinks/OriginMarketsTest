# Generated by Django 2.2.24 on 2021-10-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin', models.CharField(max_length=12)),
                ('size', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('maturity', models.DateField()),
                ('lei', models.CharField(max_length=20)),
            ],
        ),
    ]
