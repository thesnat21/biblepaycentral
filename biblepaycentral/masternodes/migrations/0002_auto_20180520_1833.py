# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-20 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masternodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masternode',
            name='txid',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]