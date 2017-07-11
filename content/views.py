# -*- coding: utf-8 -*-
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import (ExtraBlock, UnruledNumbers, Client, WhyUnruled,
                     Portfolio)
from .forms import MessageForm, OrderForm


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

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)

        # set previous and next page
        try:
            context['prev_portfolio'] = self.object.get_previous_by_release_date().get_absolute_url()
        except Portfolio.DoesNotExist:
            context['prev_portfolio'] = None

        try:
            context['next_portfolio'] = self.object.get_next_by_release_date().get_absolute_url()
        except Portfolio.DoesNotExist:
            context['next_portfolio'] = None

        return context


class ContactsView(TemplateView):
    template_name = 'content/contacts.html'

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name)
        return render(request, self.template_name, {'form': form})


@require_POST
def order_create_view(request):
    form = OrderForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect('content:landing')
