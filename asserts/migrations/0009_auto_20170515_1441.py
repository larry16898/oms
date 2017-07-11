# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0008_auto_20170515_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assert',
            name='name',
        ),
        migrations.AddField(
            model_name='assert',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='assert',
            name='ip_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='IP地址'),
        ),
    ]