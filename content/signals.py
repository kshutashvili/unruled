# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Message
from django.core.mail import EmailMessage
from django.conf import settings


@receiver(post_save, sender=Message)
def send_notification_contact(sender, instance, **kwargs):
    email = EmailMessage(
        u'Компания Unruled',
        u'Добрый день, {}. Спасибо за Ваше сообщение. Мы свяжемся с Вами в ближайшее время'.format(instance.name),
        settings.DEFAULT_FROM_EMAIL,
        [instance.email]
    )
    email.send(fail_silently=True)


@receiver(post_save, sender=Order)
def send_notification_order(sender, instance, **kwargs):
    email = EmailMessage(
        u'Заказ на сайте компании Unruled',
        u'Добрый день, {}. Спасибо за Ваш заказ. Мы свяжемся с Вами в ближайшее время'.format(instance.name),
        settings.DEFAULT_FROM_EMAIL,
        [instance.phone_or_email]
    )
    email.send(fail_silently=True)
