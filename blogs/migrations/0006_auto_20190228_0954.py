# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-28 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20190227_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
