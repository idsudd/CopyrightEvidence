# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='label',
            field=models.CharField(max_length=511),
        ),
    ]
