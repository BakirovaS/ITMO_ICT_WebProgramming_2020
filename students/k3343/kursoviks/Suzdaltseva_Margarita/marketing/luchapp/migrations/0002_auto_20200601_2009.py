# Generated by Django 3.0.6 on 2020-06-01 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='employee',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='luchapp.Employee'),
        ),
    ]