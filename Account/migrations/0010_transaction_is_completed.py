# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-13 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_debt_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]