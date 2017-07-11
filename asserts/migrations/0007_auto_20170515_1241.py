# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 04:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asserts', '0006_auto_20170515_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssertCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='类别名称')),
                ('comment', models.TextField(verbose_name='备注')),
            ],
        ),
        migrations.AddField(
            model_name='assert',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assert_set', to='asserts.AssertCategory', verbose_name='资产类别'),
        ),
    ]