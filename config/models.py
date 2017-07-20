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

    brand_slogan = models.CharField('Слоган компании',
                                    max_length=255,
                                    default='Rule the rules')

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

    google_maps_address = models.CharField(
        'Адрес на карте',
        max_length=255,
        blank=True
    )
    bot_question = models.ForeignKey(BotQuestion,
                                     verbose_name='Вопрос бота',
                                     blank=True,
                                     null=True)

    trap_block_text_1 = models.TextField('Текст первого блока-ловушки',
                                         blank=True)
    trap_block_text_2 = models.TextField('Текст второго блока-ловушки',
                                         blank=True)
    trap_block_text_3 = models.TextField('Текст третьего блока-ловушки',
                                         blank=True)
    trap_block_text_4 = models.TextField('Текст четвертого блока-ловушки',
                                         blank=True)

    about_slogan = models.TextField('Слоган', blank=True)
    about_slogan_text = models.TextField('Текст под слоганом', blank=True)
    about_text = models.TextField('Текст о компании', blank=True)

    show_about = models.BooleanField('Блок "О компании"', default=True)
    show_clients = models.BooleanField('Блок "Клиенты"', default=True)
    show_why_unruled = models.BooleanField('Блок "Почему анрулд"', default=True)
    show_portfolio = models.BooleanField('Блок "Портфолио"', default=True)
    show_contacts = models.BooleanField('Блок "Контакты"', default=True)

    # social links
    social_facebook = models.CharField('Ссылка Facebook',
                                       max_length=120,
                                       default="",
                                       blank=True)
    social_twitter = models.CharField('Ссылка Twitter',
                                      max_length=120,
                                      default="",
                                      blank=True)
    social_linkedin = models.CharField('Ссылка LinkedIn',
                                       max_length=120,
                                       default="",
                                       blank=True)
    social_behance = models.CharField('Ссылка Behance',
                                      max_length=120,
                                      default="",
                                      blank=True)

    def __unicode__(self):
        return "Конфигурация сайта"
