# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-13 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20220712_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='icon',
            field=models.CharField(default='', max_length=1000),
        ),
    ]