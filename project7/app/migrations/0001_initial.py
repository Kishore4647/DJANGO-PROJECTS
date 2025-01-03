# Generated by Django 5.1.3 on 2024-12-20 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_name', models.CharField(max_length=100)),
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('losal', models.IntegerField()),
                ('hisal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('emp_no', models.IntegerField()),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('comm', models.DecimalField(decimal_places=True, max_digits=4)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
