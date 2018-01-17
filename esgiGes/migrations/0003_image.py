# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esgiGes', '0002_auto_20180116_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=220)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='esgiGes.Student')),
            ],
        ),
    ]