# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdeploy', '0004_clientsyncsetting_file_mask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='parent_folder',
            field=models.CharField(choices=[('autoPay', 'autoPay'), ('collect', 'collect'), ('cs_office', 'cs_office'), ('acc_office', 'acc_office'), ('it_office', 'it_office')], default='autoPay', max_length=50, verbose_name='父目录'),
        ),
    ]