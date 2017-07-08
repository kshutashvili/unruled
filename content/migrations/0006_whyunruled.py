# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyUnruled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c')),
                ('icon', models.ImageField(upload_to='icons', verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0411\u043b\u043e\u043a "\u041f\u043e\u0447\u0435\u043c\u0443 Unruled?"',
                'verbose_name_plural': '\u0411\u043b\u043e\u043a "\u041f\u043e\u0447\u0435\u043c\u0443 Unruled?"',
            },
        ),
    ]