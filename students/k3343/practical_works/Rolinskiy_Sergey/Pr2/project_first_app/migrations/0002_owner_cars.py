# Generated by Django 3.0.4 on 2020-03-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Car'),
        ),
    ]