# Generated by Django 3.0.5 on 2020-04-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightsapp', '0004_auto_20200417_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flighttype',
            field=models.CharField(choices=[('D', 'отлёт'), ('A', 'прилёт')], max_length=1),
        ),
    ]
