from django.conf.urls import url

from .views import get_question, set_answer


urlpatterns = [
    url(r'get_question$', get_question, name='bot_get_question'),
    url(r'set_answer/$', set_answer, name='bot_set_answer'),
]
