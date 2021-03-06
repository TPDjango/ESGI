# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esgiGes', '0003_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cours',
            unique_together=set([('name', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('image_url', 'image_url')]),
        ),
        migrations.AlterUniqueTogether(
            name='professor',
            unique_together=set([('first_name', 'last_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('code', 'name')]),
        ),
    ]
