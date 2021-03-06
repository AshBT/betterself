# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-01 23:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('half_life_minutes', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.FloatField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplements.Ingredient')),
            ],
            options={
                'verbose_name': 'Ingredient Composition',
                'verbose_name_plural': 'Ingredient Compositions',
                'ordering': ['user', 'ingredient__name'],
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_liquid', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('ingredient_compositions', models.ManyToManyField(blank=True, to='supplements.IngredientComposition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Supplement',
                'verbose_name_plural': 'Supplements',
                'ordering': ['user', 'name'],
            },
        ),
        migrations.AddField(
            model_name='ingredientcomposition',
            name='measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplements.Measurement'),
        ),
        migrations.AddField(
            model_name='ingredientcomposition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='supplement',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientcomposition',
            unique_together=set([('user', 'ingredient', 'measurement', 'quantity')]),
        ),
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set([('name', 'user')]),
        ),
    ]
