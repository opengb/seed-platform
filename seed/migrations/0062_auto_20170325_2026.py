# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-26 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0061_green_assessments'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='greenassessment',
            unique_together=set([('organization', 'name', 'award_body')]),
        ),
    ]
