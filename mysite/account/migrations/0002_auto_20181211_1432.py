# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-11 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
