# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-05 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcb', '0003_auto_20181205_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='status',
            new_name='type',
        ),
    ]
