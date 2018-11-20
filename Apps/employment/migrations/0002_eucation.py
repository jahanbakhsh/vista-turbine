# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-20 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eucation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
                ('majored', models.CharField(max_length=40)),
                ('field', models.CharField(max_length=50)),
                ('date_from', models.CharField(max_length=12)),
                ('date_to', models.CharField(max_length=12)),
                ('school', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('average', models.CharField(max_length=5)),
            ],
        ),
    ]