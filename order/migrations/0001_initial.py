# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 22:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomenclature', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер')),
                ('rec_date', models.DateField(blank=True, null=True, verbose_name='Дата на р.д.')),
                ('rec_time_slot', models.IntegerField(blank=True, null=True, verbose_name='Слот')),
                ('rec_time', models.CharField(blank=True, max_length=80, verbose_name='Начало')),
                ('rec_time_end', models.CharField(blank=True, max_length=40, verbose_name='Край')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Телефон')),
                ('parent', models.CharField(blank=True, max_length=240, verbose_name='Родител')),
                ('child', models.CharField(blank=True, max_length=200, verbose_name='Дете')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Години')),
                ('child_count', models.IntegerField(blank=True, null=True, verbose_name='Брой деца')),
                ('adult_count', models.IntegerField(blank=True, null=True, verbose_name='Брой възрастни')),
                ('hall_count', models.IntegerField(blank=True, null=True, verbose_name='Брой зала')),
                ('hall_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Цена на зала')),
                ('deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Капаро')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Отстъпка %')),
                ('price_final', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Крайна цена')),
                ('deposit_date', models.DateField(blank=True, null=True, verbose_name='Дата на капаро')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Дата на плащане')),
                ('validity_date', models.DateField(blank=True, null=True, verbose_name='Дата на валидност')),
                ('refusal_date', models.DateField(blank=True, null=True, verbose_name='Дата на отказ')),
                ('refusal_reason', models.CharField(blank=True, max_length=400, verbose_name='Причина за отказ')),
                ('order_date', models.DateField(blank=True, null=True, verbose_name='Дата на поръчка')),
                ('notes', models.TextField(blank=True, max_length=12000, verbose_name='Забележка')),
                ('address', models.CharField(blank=True, max_length=1024, verbose_name='Адрес')),
                ('email', models.CharField(blank=True, max_length=400, verbose_name='E-mail')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата на създаване')),
                ('last_update_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата на промяна')),
                ('changes', models.TextField(blank=True, max_length=12000, verbose_name='Промени')),
                ('deposit2', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Капаро 2')),
                ('deposit2_date', models.DateField(blank=True, null=True, verbose_name='Дата на капаро2')),
                ('update_state', models.CharField(blank=True, max_length=80, verbose_name='Актуализация на състоянието')),
                ('locked', models.BooleanField(default=False, max_length=4, verbose_name='Приключено')),
                ('payed_final', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Финално плащане')),
                ('notes_torta', models.TextField(blank=True, max_length=2000, verbose_name='Забележка за тортата')),
                ('notes_kitchen', models.TextField(blank=True, max_length=2000, verbose_name='Забележка за кухнята')),
                ('store_status', models.BooleanField(default=False, verbose_name=' Изписано от склада')),
                ('club_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nomenclature.Club', verbose_name='Клуб')),
                ('saloon_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomenclature.Saloon', verbose_name='Салон за възрастни')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Служител')),
            ],
            options={
                'managed': True,
                'verbose_name': 'Поръчка',
                'verbose_name_plural': 'Поръчки',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер')),
                ('cnt', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Единична цена')),
            ],
            options={
                'managed': True,
                'verbose_name': 'Поръчка описание',
                'verbose_name_plural': 'Поръчки описание',
                'db_table': 'order_detail',
            },
        ),
        migrations.CreateModel(
            name='ArticleOrder',
            fields=[
            ],
            options={
                'verbose_name': 'Артикул продажби',
                'verbose_name_plural': 'Артикули продажби',
                'proxy': True,
            },
            bases=('nomenclature.article',),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='article_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ArticleOrder', verbose_name='Артикул'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Поръчка N'),
        ),
    ]
