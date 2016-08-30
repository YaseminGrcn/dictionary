# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

from .views import *

urlpatterns = [
    url(r'^contact/$', contact, name="contact"),
    url(r'^thanks/$', thanks, name="thanks"),
]
