# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='pasta_do_server',
            field=models.CharField(default='7days', max_length=255),
            preserve_default=False,
        ),
    ]