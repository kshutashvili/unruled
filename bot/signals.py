# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAnswer
from django.core.mail import EmailMessage
from django.conf import settings


@receiver(post_save, sender=UserAnswer)
def send_notification(sender, instance, **kwargs):
    email = EmailMessage(
        u'Бот компании Unruled',
        u"Добрый день, {}. Спасибо за Ваш ответ. Мы свяжемся с Вами в ближайшее время.".format(instance.name),
        settings.DEFAULT_FROM_EMAIL,
        [instance.email]
    )
    email.send(fail_silently=True)

