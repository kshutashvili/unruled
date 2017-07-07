# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class ExtraBlockQuerySet(models.QuerySet):
    def active(self, *args, **kwargs):
        kwargs['is_active'] = True
        return self.filter(*args, **kwargs)


class ExtraBlock(models.Model):

    class Meta:
        verbose_name = 'Дополнительный блок'
        verbose_name_plural = 'Дополнительные блоки'
        ordering = ('order',)

    name = models.CharField('Имя блока', max_length=120)
    html = RichTextField('Содержание блока')
    order = models.PositiveIntegerField('Порядок', default=1)
    is_active = models.BooleanField('Отображать на сайте', default=True)

    objects = ExtraBlockQuerySet.as_manager()

    def __unicode__(self):
        return self.name


class Portfolio(models.Model):

    name = models.CharField("Имя клиента", max_length=255)
    url = models.URLField("Ссылка на сайт")
    release_date = models.DateField("Дата релиза")
    short_description = models.TextField("Краткое описание проекта")
    detailed_description = models.TextField("Подробное описание проекта")

    def __unicode__(self):
        return self.name


class News(models.Model):

    title = models.CharField("Заголовок", max_length=255)
    short_content = models.TextField("Краткое содержание")
    full_content = models.TextField("Полное содержание")
    created_dt = models.DateTimeField("Дата создания", auto_now_add=True)

    def __unicode__(self):
        return self.title
