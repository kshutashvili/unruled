# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    class Meta:
        verbose_name = "Конфигурация сайта"

    brand_name = models.CharField('Название компании', max_length=70,
                                  default='Unruled Lab_')

    phone = models.CharField(
        'Телефон',
        max_length=50,
        blank=True
    )
    email = models.EmailField(
        'Адрес электронной почты',
        max_length=50,
        blank=True
    )
    address = models.CharField(
        'Адрес',
        max_length=128,
        blank=True
    )

    def __unicode__(self):
        return "Конфигурация сайта"
