# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0009_auto_20170515_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assert',
            name='assert_code',
            field=models.CharField(max_length=50, unique=True, verbose_name='资产编码'),
        ),
    ]