# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0016_auto_20160411_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingsnapshot',
            name='recent_sale_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
