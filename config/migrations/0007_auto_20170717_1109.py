# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_remove_siteconfiguration_show_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='social_behance',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Behance'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='social_facebook',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Facebook'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='social_linkedin',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 LinkedIn'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='social_twitter',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 Twitter'),
        ),
    ]
