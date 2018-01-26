# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-26 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180126_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': '\u83dc\u5355',
                'verbose_name_plural': '\u83dc\u5355',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, null=True, to='app01.Menu'),
        ),
    ]
