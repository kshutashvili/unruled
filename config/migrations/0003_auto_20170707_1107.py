# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_siteconfiguration_bot_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_slogan',
            field=models.TextField(blank=True, verbose_name='\u0421\u043b\u043e\u0433\u0430\u043d'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_text',
            field=models.TextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_about',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438"'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_clients',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041a\u043b\u0438\u0435\u043d\u0442\u044b"'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_contacts',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b"'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_portfolio',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e"'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_team',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041a\u043e\u043c\u0430\u043d\u0434\u0430"'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='show_why_unruled',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a "\u041f\u043e\u0447\u0435\u043c\u0443 \u0430\u043d\u0440\u0443\u043b\u0434"'),
        ),
    ]
