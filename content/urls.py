from django.conf.urls import url

from content.views import LandingView
from django.views.decorators.csrf import ensure_csrf_cookie


urlpatterns = [
    url(r'^$', ensure_csrf_cookie(LandingView.as_view()), name='landing'),
]
