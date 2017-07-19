# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_order_portfolio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ('order',), 'verbose_name': '\u041f\u0443\u043d\u043a\u0442 \u043c\u0435\u043d\u044e', 'verbose_name_plural': '\u041f\u0443\u043d\u043a\u0442\u044b \u043c\u0435\u043d\u044e'},
        ),
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.CharField(choices=[('header', 'Header'), ('footer', 'Footer')], db_index=True, default='header', max_length=10, verbose_name='\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]