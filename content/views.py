# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'content/landing.html'
