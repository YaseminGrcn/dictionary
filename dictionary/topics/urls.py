# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

from .views import *

urlpatterns = [
    url(r'^topic/(?P<id>[0-9]+)/$', topic, name="topic"),
]
