# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdeploy', '0002_auto_20170506_0436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientsyncsetting',
            options={'ordering': ('created',)},
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='host',
            field=models.CharField(max_length=20, verbose_name='同步源主机'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='parent_folder',
            field=models.CharField(choices=[('autoPay', '自动提款'), ('collect', '采集器'), ('cs_office', '客服办公工具'), ('acc_office', '财务办公工具'), ('it_office', '技术办公工具')], default='autoPay', max_length=50, verbose_name='父目录'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='password',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='program_filename',
            field=models.CharField(max_length=50, verbose_name='可执行文件'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='shortcut_filename',
            field=models.CharField(max_length=50, verbose_name='桌面快捷方式'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='sub_folder',
            field=models.CharField(max_length=50, verbose_name='子目录'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='username',
            field=models.CharField(max_length=50, verbose_name='同步账户'),
        ),
        migrations.AlterField(
            model_name='clientsyncsetting',
            name='version_num',
            field=models.CharField(max_length=5, verbose_name='版本号'),
        ),
    ]
