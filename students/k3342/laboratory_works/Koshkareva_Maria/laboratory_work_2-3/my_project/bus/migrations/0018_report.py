# Generated by Django 3.0.7 on 2020-07-02 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0017_auto_20200701_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.IntegerField(choices=[(0, 'OK'), (1, 'Broken bus'), (2, 'Sick driver'), (3, 'No driver'), (4, 'Other')], default=0)),
                ('schedule_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.Schedule')),
            ],
        ),
    ]
