# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-12 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20220712_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='currency',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='language',
            field=models.CharField(default=None, max_length=255),
        ),
    ]