# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-09 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tartrequests', '0003_auto_20170509_0800'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tortapictureregister',
            options={'managed': True, 'verbose_name': 'Вид на торта', 'verbose_name_plural': 'Видове торти'},
        ),
    ]
