# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0007_auto_20170515_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assertcategory',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
    ]