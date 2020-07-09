# Generated by Django 3.0.7 on 2020-07-01 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0012_auto_20200626_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='work_end',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='work_start',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='bus',
            field=models.ForeignKey(default=4, help_text="Don't change to get the driver's bus", on_delete=django.db.models.deletion.CASCADE, to='bus.Bus'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='route',
            field=models.ForeignKey(default=3, help_text="Don't change to get the driver's route", on_delete=django.db.models.deletion.CASCADE, to='bus.Route'),
        ),
    ]