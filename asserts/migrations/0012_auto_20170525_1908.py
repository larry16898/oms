# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0011_auto_20170525_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assert',
            name='assert_code',
            field=models.CharField(default='NULL', max_length=50, verbose_name='资产编码'),
            preserve_default=False,
        ),
    ]
