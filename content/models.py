# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
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


class PortfolioManager(models.Manager):
    def indicator(self):
        return self.count()


class Portfolio(models.Model):

    name = models.CharField("Имя клиента", max_length=255)
    url = models.URLField("Ссылка на сайт")
    release_date = models.DateField("Дата релиза")
    short_description = models.TextField("Краткое описание проекта")
    detailed_description = models.TextField("Подробное описание проекта")

    objects = PortfolioManager()

    def __unicode__(self):
        return self.name


class NewsManager(models.Manager):
    def indicator(self):
        return self.count()


class News(models.Model):

    title = models.CharField("Заголовок", max_length=255)
    short_content = models.TextField("Краткое содержание")
    full_content = models.TextField("Полное содержание")
    created_dt = models.DateTimeField("Дата создания", auto_now_add=True)

    objects = NewsManager()

    def __unicode__(self):
        return self.title


class MenuItem(models.Model):
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    url = models.CharField("Ссылка", max_length=120)
    title = models.CharField("Название", max_length=255)
    linked_model = models.ForeignKey(ContentType,
                                     verbose_name="Тип контента",
                                     help_text="Определяет индикатор",
                                     blank=True,
                                     null=True)

    def __unicode__(self):
        return self.title

    @property
    def indicator(self):
        try:
            return self.linked_model.model_class().objects.indicator()
        except AttributeError:
            return None


class UnruledNumbers(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "Unruled в цифрах"

    number = models.IntegerField("Значение")
    measure_unit = models.CharField("Единица измерения", max_length=120)

    def __unicode__(self):
        return "{} {}".format(self.number, self.measure_unit)


class Client(models.Model):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    name = models.CharField("Название", max_length=255)
    logo = models.ImageField("Логотип", upload_to="clients")

    def __unicode__(self):
        return self.name
