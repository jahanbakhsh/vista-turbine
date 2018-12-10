# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-09 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcb', '0004_auto_20181205_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('hieght', models.FloatField()),
                ('position', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
    ]