# Generated by Django 5.1.3 on 2024-12-20 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('country_no', models.IntegerField()),
                ('country_pm', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Capital_name', models.CharField(max_length=100)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
