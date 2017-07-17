# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_safe, require_POST

import json

from config.models import SiteConfiguration
from .models import UserAnswer


@require_safe
def get_question(request):
    """Returns question data for bot"""

    obj = SiteConfiguration.get_solo().bot_question

    if obj is None:
        return JsonResponse({'status': 'fail',
                             'message': 'no question defined'})

    data = {'status': 'ok'}
    data['data'] = {
        'person_name': obj.person.name,
        'greeting': obj.person.greeting,
        'question': obj.title,
        'answers': [
            {
                'id': x.pk,
                'answer': x.title,
                'description': x.description,
                'type': x.answer_type
            } for x in obj.answers.order_by('answer_type')]
    }
    return JsonResponse(data)


@require_POST
def set_answer(request):
    """API for submitting form"""

    if not request.is_ajax():
        return HttpResponseBadRequest()

    # parse data
    try:
        data = json.loads(request.body)
    except ValueError:
        return JsonResponse({'status': 'error',
                             'message': 'Invalid request body'})

    create_data = {
        'answer_id': data.get('answerId'),
        'name': data.get('name'),
        'email': data.get('email')
    }

    obj = UserAnswer(**create_data)
    try:
        # validate UserAnswer object
        obj.full_clean()
    except ValidationError:
        return JsonResponse({'status': 'error'})
    obj.save()
    return JsonResponse({'status': 'ok',
                         'message': u'Ваше сообщение отправлено, '
                                    u'с Вами свяжется наш сотрудник'})
