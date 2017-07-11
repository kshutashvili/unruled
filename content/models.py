# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.db import models
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField
import datetime


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

    def last_added(self):
        return self.all()[:3]

    def indicator(self):
        period_start = datetime.datetime.today()-datetime.timedelta(days=30)
        return self.filter(release_date__gte=period_start).count()


class Portfolio(models.Model):
    class Meta:
        ordering = ('-release_date',)
        verbose_name = verbose_name_plural = "Портфолио"

    name = models.CharField("Имя клиента", max_length=255)
    image = models.ImageField("Скриншот", upload_to="portfolio", default="/img/not-found.png")
    url = models.URLField("Ссылка на сайт", blank=True, null=True)
    release_date = models.DateField("Дата релиза")
    short_description = models.TextField("Краткое описание проекта")
    detailed_description = models.TextField("Подробное описание проекта")

    objects = PortfolioManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('content:portfolio_detail', kwargs={"pk": self.id})


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


class WhyUnruled(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = 'Блок "Почему Unruled?"'

    text = models.TextField("Подпись")
    icon = models.ImageField("Иконка", upload_to="icons")

    def __unicode__(self):
        return self.text


class PortfolioImage(models.Model):
    class Meta:
        verbose_name = "Изображение галереи портфолио"
        verbose_name_plural = "Изображения галереи портфолио"

    portfolio = models.ForeignKey(Portfolio,
                                  related_name='images',
                                  verbose_name="Портфолио")
    image = models.ImageField("Картинка", upload_to="portfolio")

    def __unicode__(self):
        return '{} - {}'.format(self.portfolio.name, self.image.name)


class Message(models.Model):
    class Meta:
        ordering = ['-created_dt']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    created_dt = models.DateTimeField('Время создания', auto_now_add=True)
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Адрес электронной почты')
    text = models.TextField('Текст сообщения')

    def __unicode__(self):
        return '{} {}'.format(self.created_dt, self.email)


class Order(models.Model):
    class Meta:
        ordering = ('-created_dt',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    name = models.CharField("Имя клиента",
                            max_length=255)
    phone_or_email = models.CharField("Телефон или e-mail",
                                      max_length=255)

    description = models.TextField("Описание проекта",
                                   blank=True)
    attachment = models.FileField("Требования/тех задание",
                                  upload_to="orders",
                                  blank=True)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.phone_or_email)
