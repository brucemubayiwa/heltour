# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0027_auto_20160726_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaguedocument',
            name='type',
            field=models.CharField(blank=True, choices=[('faq', 'FAQ')], max_length=255, null=True),
        ),
    ]
