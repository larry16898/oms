# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientdeploy', '0008_auto_20170510_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcategory',
            name='sync_server',
        ),
        migrations.AddField(
            model_name='clientsyncsetting',
            name='sync_server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientdeploy.SyncServer'),
        ),
    ]