# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castingShop', '0002_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizeOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company_profit', models.PositiveIntegerField(default=0)),
                ('total_cost', models.PositiveIntegerField(default=0)),
                ('shape', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]