# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from dictionary.event.models import Event, Complaint
from dictionary.topics.models import Topic, Entry


def event_index(request):
    event = Event.objects.all()
    topic = Topic.objects.all()
    context = {
        'event': event,
        'topic': topic,
    }
    return render(request, "event/event.html", context)


def event(request, id):
    show_remove_link = False
    new_event, created = Event.objects.get_or_create(user=request.user, topic_id=id)
    if not created:
        show_remove_link = False
        print(show_remove_link)
    else:
        show_remove_link = True
        print(show_remove_link)
    url = reverse('topics:topic', kwargs={'id': id})
    return HttpResponseRedirect(url)


def delete_event(request, id):
    try:
        event = get_object_or_404(Event, id=id, user=request.user)
        event.delete()
        messages.success(request, _("Takip silindi"))
    except  MultipleObjectsReturned:
        event = get_object_or_404(Event, id=id)[0]
        messages.warning(request, _("Takip silinirken bir hata oluştu"))

    url = reverse('topics:topic', kwargs={'id': id})
    return HttpResponseRedirect(url)


def complaint(request, id):
    entry_id = Entry.objects.get(topic_id=id)
    new_complaint = Complaint.objects.create(user=request.user, entry_id=entry_id.id)
    total = Complaint.objects.filter(entry_id=entry_id.id).count()

    context = {
        'id': id,
    }
    url = reverse('topics:topic', kwargs={'id': id})
    return HttpResponseRedirect(url)
