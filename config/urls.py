# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from dictionary.users import urls as users_urls
from dictionary.topics import urls as topics_urls
from dictionary.event import urls as event_urls
from dictionary.users.views import base

urlpatterns = [
    url(r'^$', base, name='base'),
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^topics/', include(topics_urls, namespace='topics')),
    url(r'^event/', include(event_urls, namespace='event')),
    url(r'^accounts/', include('allauth.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:

    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
