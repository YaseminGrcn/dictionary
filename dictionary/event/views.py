# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User
from dictionary.event.models import User, Event

def event_index(request):
    event = Event.objects.all()
    context = {
        'event': event,
    }
    return render(request, "event/event.html", context)


def event(request, id):
    new_event, created = Event.objects.get_or_create(user=request.user, topic_id=id)
    if not created:
        print (5)
    else:
        print(4)
    url = reverse('event:event_index')
    return HttpResponseRedirect(url)
