# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 05:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chronic_disease',
            fields=[
                ('chronic_disease_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('disease_desc', models.TextField(default='')),
                ('symptoms', models.TextField()),
                ('qanda', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('text_field', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 28, 5, 37, 14, 257664, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('specialist_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('specialist_name', models.CharField(max_length=200)),
                ('specialist_details', models.CharField(default='', max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='hospital',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Hospital'),
        ),
        migrations.AddField(
            model_name='chronic_disease',
            name='dep',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Department'),
        ),
        migrations.AddField(
            model_name='chronic_disease',
            name='spec',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Specialist'),
        ),
    ]
