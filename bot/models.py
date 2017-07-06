# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class BotPerson(models.Model):
    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

    name = models.CharField('Имя персонажа', max_length=120)
    greeting = models.TextField('Текст приветствия')

    def __unicode__(self):
        return self.name


class BotQuestion(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    person = models.ForeignKey(BotPerson, verbose_name='Персонаж')
    title = models.CharField('Вопрос', max_length=255)

    def __unicode__(self):
        return self.title


class BotAnswer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    class AnswerTypes:
        POSITIVE = 'positive'
        REJECT = 'reject'
        CHOICES = (
            (POSITIVE, 'Позитивный'),
            (REJECT, 'Отказной'),
        )

    question = models.ForeignKey(BotQuestion,
                                 related_name='answers',
                                 verbose_name='Вопрос')
    answer_type = models.CharField('Тип ответа',
                                   max_length=20,
                                   choices=AnswerTypes.CHOICES,
                                   default=AnswerTypes.POSITIVE
                                   )
    title = models.CharField('Ответ', max_length=255)
    description = RichTextField('Описание ответа', null=True, blank=True)

    def __unicode__(self):
        return self.title


class UserAnswer(models.Model):
    class Meta:
        verbose_name = 'Ответ клиента'
        verbose_name_plural = 'Ответы клиентов'

    answer = models.ForeignKey(BotAnswer, verbose_name='Ответ')
    name = models.CharField('Имя клиента', max_length=255)
    email = models.EmailField('e-mail клиента')
    created_dt = models.DateTimeField('Дата ответа', auto_now_add=True)

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.email)
