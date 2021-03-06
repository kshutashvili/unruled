# -*- coding: utf-8 -*-
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, DetailView
from .models import (ExtraBlock, UnruledNumbers, Client, WhyUnruled,
                     Portfolio)
from .forms import MessageForm, OrderForm
from django.http import (JsonResponse, HttpResponseBadRequest,
                         HttpResponse, HttpResponseForbidden)
import json
import os
from django.utils.encoding import smart_str
from django.conf import settings


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

        context['left_menu_hide'] = True

        return context


class ContactsView(TemplateView):
    template_name = 'content/contacts.html'

    def post(self, request):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        # parse data
        try:
            data = json.loads(request.body)
        except ValueError:
            return JsonResponse({'status': 'error',
                                 'message': 'Invalid request body'})

        form = MessageForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok',
                                 'message': u'Ваше сообщение отправлено, '
                                            u'с Вами свяжется наш сотрудник'})

        return JsonResponse({'status': 'error'})


@require_POST
def order_create_view(request):
    form = OrderForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()

        return JsonResponse({'status': 'ok',
                             'message': u'Ваше сообщение отправлено, '
                                        u'с Вами свяжется наш сотрудник'})

    return JsonResponse({'status': 'error'})


def attachment_view(request, filename):
    """Allow to download files only for authorized users"""
    if request.user.is_authenticated:
        response = HttpResponse()
        url = os.path.join('/media/orders/', filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
        path = os.path.join(settings.MEDIA_ROOT, 'orders/', filename)
        length = os.path.getsize(path)
        response['Content-Length'] = str(length)
        response['X-Accel-Redirect'] = url
        return response

    else:
        return HttpResponseForbidden("Restricted Access")
