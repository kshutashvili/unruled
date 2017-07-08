# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from .models import ExtraBlock, UnruledNumbers, Client


class LandingView(TemplateView):
    template_name = 'content/landing.html'

    def get_context_data(self, **kwargs):
        kwargs['extra_blocks'] = ExtraBlock.objects.active()
        kwargs['unruled_numbers'] = UnruledNumbers.objects.all()
        kwargs['clients'] = Client.objects.all()
        return super(LandingView, self).get_context_data(**kwargs)
