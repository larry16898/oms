# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdeploy', '0005_auto_20170506_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsyncsetting',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='启用'),
        ),
    ]
