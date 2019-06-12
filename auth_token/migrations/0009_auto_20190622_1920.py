# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-22 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_token', '0008_auto_20190509_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='two_factor_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
