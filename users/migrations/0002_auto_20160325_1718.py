# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='camera',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Camera'),
        ),
        migrations.AddField(
            model_name='user',
            name='lens',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Lens'),
        ),
    ]
