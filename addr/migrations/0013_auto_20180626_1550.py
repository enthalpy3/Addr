# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addr', '0012_auto_20180626_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addr',
            name='approved_addr',
        ),
        migrations.AddField(
            model_name='addr',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]