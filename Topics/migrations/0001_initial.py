# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-24 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(default='', max_length=30)),
                ('topic_id', models.IntegerField()),
                ('tutorial_available', models.BooleanField(default=False)),
                ('formulae_available', models.BooleanField(default=False)),
                ('questions_available', models.BooleanField(default=False)),
                ('nbr_of_ques', models.IntegerField(default=1)),
                ('topic_icon_url', models.CharField(default='/static/Table/img/', max_length=100)),
                ('tutorial_id', models.IntegerField(null=True)),
                ('formulae_id', models.IntegerField(null=True)),
                ('questions_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=150, null=True)),
            ],
        ),
    ]