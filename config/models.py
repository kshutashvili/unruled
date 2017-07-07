# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from solo.models import SingletonModel
from bot.models import BotQuestion


class SiteConfiguration(SingletonModel):
    class Meta:
        verbose_name = "Конфигурация сайта"

    brand_name = models.CharField('Название компании',
                                  max_length=70,
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
    bot_question = models.ForeignKey(BotQuestion,
                                     verbose_name='Вопрос бота',
                                     blank=True,
                                     null=True)

    about_slogan = models.TextField('Слоган', blank=True)
    about_text = models.TextField('Текст о компании', blank=True)

    show_about = models.BooleanField('Блок "О компании"', default=True)
    show_clients = models.BooleanField('Блок "Клиенты"', default=True)
    show_why_unruled = models.BooleanField('Блок "Почему анрулд"', default=True)
    show_portfolio = models.BooleanField('Блок "Портфолио"', default=True)
    show_team = models.BooleanField('Блок "Команда"', default=True)
    show_contacts = models.BooleanField('Блок "Контакты"', default=True)

    def __unicode__(self):
        return "Конфигурация сайта"
