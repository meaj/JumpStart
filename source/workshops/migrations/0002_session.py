# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0001_initial'),
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_title', models.CharField(default='title', max_length=48)),
                ('session_date', models.DateTimeField(default='1987-01-01 00:00')),
                ('session_location', models.CharField(default='CS Main Lab', max_length=48)),
                ('session_threshold', models.IntegerField(default=1)),
                ('registered_attendees', models.ManyToManyField(default=None, to='importing.attendee')),
                ('workshop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workshops.Workshop')),
            ],
        ),
    ]