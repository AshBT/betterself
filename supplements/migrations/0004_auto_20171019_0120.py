# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 01:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('supplements', '0003_data_migrations_for_measurements'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSupplementStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('supplements', models.ManyToManyField(blank=True, to='supplements.Supplement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Supplements Stacks',
                'ordering': ['user', 'name'],
                'verbose_name': 'Supplements Stack',
            },
        ),
        migrations.AlterUniqueTogether(
            name='usersupplementstack',
            unique_together=set([('user', 'name')]),
        ),
    ]