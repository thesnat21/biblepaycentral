# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podc', '0003_superblock_superblockreceiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='rosettauser',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rosettauser',
            name='cpid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rosettauser',
            name='team',
            field=models.IntegerField(default=0),
        ),
    ]
