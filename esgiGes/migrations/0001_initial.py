# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='professor',
            unique_together=set([('first_name', 'last_name')]),
        ),
        migrations.AddField(
            model_name='cours',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esgiGes.Professor'),
        ),
        migrations.AddField(
            model_name='cours',
            name='student',
            field=models.ManyToManyField(to='esgiGes.Student'),
        ),
    ]
