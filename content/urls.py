from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import static

from content.views import LandingView
from django.views.decorators.csrf import ensure_csrf_cookie


urlpatterns = [
    url(r'^$', ensure_csrf_cookie(LandingView.as_view()), name='landing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
