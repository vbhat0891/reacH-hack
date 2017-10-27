# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chroniFic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faq',
            name='faq_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]