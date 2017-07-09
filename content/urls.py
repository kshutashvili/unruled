from django.conf.urls import url


from content.views import (LandingView, PortfolioListView, PortfolioDetailView,
                           ContactsView)

from django.views.decorators.csrf import ensure_csrf_cookie


urlpatterns = [
    url(r'^$', ensure_csrf_cookie(LandingView.as_view()), name='landing'),
    url(r'^portfolio/$', PortfolioListView.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<pk>[0-9_-]+)/$',
        PortfolioDetailView.as_view(),
        name='portfolio_detail'),
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
]
