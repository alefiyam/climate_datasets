# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-20 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Year', models.IntegerField(blank=True, default=None, null=True)),
                ('JAN', models.FloatField(blank=True, default=None, null=True)),
                ('FEB', models.FloatField(blank=True, default=None, null=True)),
                ('MAR', models.FloatField(blank=True, default=None, null=True)),
                ('APR', models.FloatField(blank=True, default=None, null=True)),
                ('MAY', models.FloatField(blank=True, default=None, null=True)),
                ('JUN', models.FloatField(blank=True, default=None, null=True)),
                ('JUL', models.FloatField(blank=True, default=None, null=True)),
                ('AUG', models.FloatField(blank=True, default=None, null=True)),
                ('SEP', models.FloatField(blank=True, default=None, null=True)),
                ('OCT', models.FloatField(blank=True, default=None, null=True)),
                ('NOV', models.FloatField(blank=True, default=None, null=True)),
                ('DEC', models.FloatField(blank=True, default=None, null=True)),
                ('WIN', models.FloatField(blank=True, default=None, null=True)),
                ('SPR', models.FloatField(blank=True, default=None, null=True)),
                ('SUM', models.FloatField(blank=True, default=None, null=True)),
                ('AUT', models.FloatField(blank=True, default=None, null=True)),
                ('ANN', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temprature_type', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climate_datasets.Country')),
            ],
        ),
        migrations.AddField(
            model_name='temperaturedata',
            name='temp_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climate_datasets.TemperatureType'),
        ),
    ]
