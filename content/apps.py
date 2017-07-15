# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'content'
    verbose_name = 'Содержание'

    def ready(self):
        import content.signals
