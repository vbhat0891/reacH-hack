# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chroniFic', '0003_auto_20171020_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='dep',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chroniFic.Department'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answers',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faq',
            name='questions',
            field=models.TextField(max_length=50),
        ),
    ]