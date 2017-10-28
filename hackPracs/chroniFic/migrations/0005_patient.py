# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chroniFic', '0004_auto_20171027_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('pFirstName', models.CharField(max_length=200)),
                ('pLastName', models.CharField(max_length=50)),
                ('pContactNumber', models.CharField(max_length=12)),
                ('textField', models.TextField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name=datetime.datetime(2017, 10, 28, 0, 45, 15, 301784, tzinfo=utc))),
            ],
        ),
    ]
