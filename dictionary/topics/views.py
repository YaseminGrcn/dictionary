# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from .models import User
from dictionary.topics.models import Topic, Category, Entry, Favoutire

def topic(request, id):
    topic = Topic.objects.all()
    category = Category.objects.all()
    entry = Entry.objects.select_related("topic").filter(topic_id=id)

    context = {
        'entry': entry,
        'topic': topic,
        'category': category,
    }
    return render(request, "topic/topic.html", context)

