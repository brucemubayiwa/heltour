# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-22 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0150_team_slack_channel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['league__name', '-name'], 'permissions': (('manage_players', 'Can manage players'), ('review_nominated_games', 'Can review nominated games'))},
        ),
    ]
