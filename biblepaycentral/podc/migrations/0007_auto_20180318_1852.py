# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podc', '0006_superblockreceiver_reward'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='superblockreceiver',
            unique_together=set([('superblock', 'rosettauser')]),
        ),
    ]
