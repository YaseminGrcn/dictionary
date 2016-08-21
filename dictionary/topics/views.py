# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.db import IntegrityError
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

def new_entry(request):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        if len(content) == 0:
            messages.add_message(request, messages.ERROR, 'Lütfen Eksiksiz Doldurunuz')
            return HttpResponseRedirect('/')
        else:
            entry = Entry.objects.create(content=content, topic_id=5, user_id=request.user.id)
            print(5)
            entry.save()
    return HttpResponseRedirect('/')

