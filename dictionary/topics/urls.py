# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

from .views import *

urlpatterns = [
    url(r'^topic/(?P<id>[0-9]+)/$', topic, name="topic"),
    url(r'^(?P<id>[0-9]+)/$', new_entry, name="new_entry"),

    url(r'^like/(?P<id>[0-9]+)/$', like, name="like"),
    url(r'^delete_like/(?P<id>[0-9]+)/$', delete_like, name="delete_like"),
]
