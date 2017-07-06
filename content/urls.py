from django.conf.urls import url

from content.views import LandingView


urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
]
