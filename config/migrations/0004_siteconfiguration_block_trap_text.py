# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20170707_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block_trap_text',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0431\u043b\u043e\u043a\u0430-\u043b\u043e\u0432\u0443\u0448\u043a\u0438'),
        ),
    ]