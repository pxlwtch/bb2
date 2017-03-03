# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('birthday', models.DateField(default='9999-11-29')),
                ('poke_history', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='poke',
            name='pokee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokee', to='exam.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='exam.User'),
        ),
    ]
