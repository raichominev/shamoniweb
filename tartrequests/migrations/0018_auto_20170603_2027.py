# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-03 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tartrequests', '0017_auto_20170522_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='tortarequest',
            name='dostavka_time',
            field=models.TimeField(null=True, verbose_name='Час'),
        ),
        migrations.AlterField(
            model_name='tortarequest',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tartrequests.TortaPictureRegister', verbose_name='Кат.No.'),
        ),
        migrations.AlterField(
            model_name='tortarequest',
            name='dostavka_date',
            field=models.DateField(null=True, verbose_name='Дата доставка'),
        ),
        migrations.AlterField(
            model_name='tortarequest',
            name='nadpis',
            field=models.CharField(blank=True, db_column='NADPIS', default='Честит рожден ден', max_length=150, verbose_name='Надпис'),
        ),
        migrations.AlterField(
            model_name='tortarequest',
            name='notes',
            field=models.TextField(blank=True, db_column='NOTES', max_length=3000, null=True, verbose_name='Забележка'),
        ),
    ]
