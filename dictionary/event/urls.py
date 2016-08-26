# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

from .views import *

urlpatterns = [

    url(r'^event_index/$', event_index, name="event_index"),
    url(r'^event/(?P<id>[0-9]+)/$', event, name="event"),
    url(r'^delete_event/(?P<id>[0-9]+)/$', delete_event, name="delete_event"),
    url(r'^(?P<id>[0-9]+)/$', complaint, name="complaint"),
]
