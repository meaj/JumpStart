# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='workshop',
        ),
    ]