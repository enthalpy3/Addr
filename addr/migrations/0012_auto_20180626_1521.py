# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addr', '0011_auto_20180626_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addr',
            old_name='approved',
            new_name='approved_addr',
        ),
    ]