# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_name', models.CharField(default='name', max_length=16)),
                ('email_subject', models.CharField(default='subject', max_length=48)),
                ('email_body', models.TextField(default='body', max_length=2000)),
                ('email_signature', models.CharField(default='jumpstartutsa@gmail.com', max_length=48)),
            ],
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='survery_title',
        ),
        migrations.AddField(
            model_name='attendee',
            name='group',
            field=models.CharField(default='group', max_length=48),
        ),
        migrations.AddField(
            model_name='workshop',
            name='survey_title',
            field=models.CharField(default='title', max_length=48),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='first_name',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='last_name',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='last_name',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(max_length=48),
        ),
    ]
