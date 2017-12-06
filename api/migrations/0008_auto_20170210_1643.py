# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170210_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarchord',
            name='modifier',
            field=models.CharField(choices=[('m', 'minor'), ('m', 'major'), ('aug', 'aug'), ('dim', 'dim'), ('sus', 'sus'), ('add9', 'add9'), ('m6', 'm6'), ('m7', 'm7'), ('m9', 'm9'), ('mmaj7', 'mmaj7'), ('-5', '-5'), ('11', '11'), ('13', '13'), ('5', '5'), ('6', '6'), ('6add9', '6add9'), ('7', '7'), ('7-5', '7-5'), ('7maj5', '7maj5'), ('7sus4', '7sus4'), ('9', '9'), ('', '')], default='', max_length=100),
        ),
    ]
