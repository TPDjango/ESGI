# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esgiGes', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='professor',
            unique_together=set([]),
        ),
    ]
