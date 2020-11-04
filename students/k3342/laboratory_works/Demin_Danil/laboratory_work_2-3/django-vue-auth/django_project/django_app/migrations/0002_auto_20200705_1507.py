# Generated by Django 3.0.8 on 2020-07-05 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('diet_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Breed')),
                ('cage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Cage')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('cage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Cage')),
                ('chicken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Chicken')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.AddField(
            model_name='report',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Worker'),
        ),
        migrations.AddField(
            model_name='cage',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.Worker'),
        ),
    ]