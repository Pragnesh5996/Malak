# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-12 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20220712_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='language',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
