# Generated by Django 2.0.2 on 2020-06-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rooms',
            field=models.CharField(max_length=500, verbose_name='Rooms'),
        ),
    ]
