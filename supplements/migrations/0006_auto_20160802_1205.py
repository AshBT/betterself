# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0005_auto_20160730_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientcomposition',
            old_name='measurement_unit',
            new_name='measurement',
        ),
    ]