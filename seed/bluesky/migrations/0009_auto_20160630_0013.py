# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bluesky', '0008_auto_20160629_2358'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taxlotproperty',
            unique_together=set([('property_view', 'taxlot_view')]),
        ),
    ]
