# Generated by Django 3.0.4 on 2020-05-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0007_auto_20200530_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=200, verbose_name='Название марки')),
                ('c_type', models.CharField(max_length=200, verbose_name='Модель машины')),
                ('color', models.CharField(max_length=200, verbose_name='Цвет машины')),
                ('gov_num', models.IntegerField(max_length=200, verbose_name='Гос. номер')),
            ],
        ),
    ]
