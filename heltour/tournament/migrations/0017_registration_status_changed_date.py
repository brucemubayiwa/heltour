# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0016_registration_status_changed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status_changed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
