# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdeploy', '0006_clientsyncsetting_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='file_mask',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='文件同步掩码'),
        ),
    ]
