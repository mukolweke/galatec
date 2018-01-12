# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=120)),
                ('date_reg', models.DateTimeField()),
            ],
        ),
    ]