# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import (ExtraBlock, UnruledNumbers, Client, WhyUnruled,
                     Portfolio)
from .forms import MessageForm


class LandingView(TemplateView):
    template_name = 'content/landing.html'

    def get_context_data(self, **kwargs):
        kwargs['extra_blocks'] = ExtraBlock.objects.active()
        kwargs['unruled_numbers'] = UnruledNumbers.objects.all()
        kwargs['clients'] = Client.objects.all()
        kwargs['why_unruled'] = WhyUnruled.objects.all()
        kwargs['portfolio_list'] = Portfolio.objects.last_added()
        return super(LandingView, self).get_context_data(**kwargs)


class PortfolioListView(ListView):
    queryset = Portfolio.objects.all()
    context_object_name = 'portfolio_list'
    template_name = 'content/portfolio_list.html'
    paginate_by = 6


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'content/portfolio.html'
    context_object_name = 'portfolio'


class ContactsView(TemplateView):
    template_name = 'content/contacts.html'

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name)
        return render(request, self.template_name, {'form': form})
