# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0014_auto_20160723_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonplayer',
            name='registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.Registration'),
        ),
    ]
