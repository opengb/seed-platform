# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluesky', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertystate',
            name='pm_parent_property_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
