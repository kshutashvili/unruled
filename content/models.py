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
