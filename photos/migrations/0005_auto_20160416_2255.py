# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-16 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20160416_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
    ]