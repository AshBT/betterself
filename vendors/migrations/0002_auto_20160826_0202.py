# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vendor',
            unique_together=set([('name', 'user')]),
        ),
    ]