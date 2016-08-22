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
from dictionary.topics.models import Topic, Category, Entry, Favoutire

def topic(request, id):
    topic = Topic.objects.all()
    contact_list = Entry.objects.select_related("topic").filter(topic_id=id)
    paginator = Paginator(contact_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    category = Category.objects.all()
    context = {
        'topic': topic,
        'category': category,
        'contacts': contacts,
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

def like(request, id):
    new_like, created = Favoutire.objects.get_or_create(user=request.user, entry_id=id)
    if not created:
        print (5)
    else:
        print(4)
    url = reverse('topics:topic', kwargs={'id': id})
    return HttpResponseRedirect(url)
def delete_like(request, id):

    try:
        like = get_object_or_404(Favoutire, id=id)
        like.delete()
        messages.success(request, _("favori silindi"))
    except  MultipleObjectsReturned:
        like = get_object_or_404(Favoutire, id=id)[0]
        messages.warning(request, _("Favori silinirken bir hata oluştu"))

    url = reverse('topics:topic', kwargs={'id': id})
    return HttpResponseRedirect(url)
