# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dictionary.topics.models import Topic, Category, Entry, Favoutire



def topic(request, id):
    topic = Topic.objects.all()
    topic_id = Topic.objects.get(id=id)
    total = Favoutire.objects.filter(entry_id=id).count()
    contact_list = Entry.objects.select_related("topic").filter(topic_id=id)
    paginator = Paginator(contact_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    category = Category.objects.all()
    context = {
        'topic': topic,
        'category': category,
        'contacts': contacts,
        'topic_id': topic_id.id,
        'total': total,
    }
    return render(request, "topic/topic.html", context)


def entry(request):
    topic = request.POST.get('topic')
    if request.method == 'POST':

        content = request.POST.get('content', None)
        if len(content) == 0:
            messages.add_message(request, messages.ERROR, 'Lütfen Eksiksiz Doldurunuz')
            return HttpResponseRedirect('/')
        else:
            entry = Entry.objects.create(content=content, topic_id=topic, user_id=request.user.id)
            print(5)
            entry.save()

    url = reverse('topics:topic', kwargs={'id': topic})
    return HttpResponseRedirect(url)


def like(request, id):
    try:
        created = Favoutire.objects.create(user=request.user, entry_id=id)
    except Favoutire.DoesNotExist:
        print ("zaten ekli")
    return render(request, "topic/new_entry.html")


def delete_like(request, id):
    try:
        like = Favoutire.objects.get(entry_id=id, user=request.user)
        like.delete()
        messages.success(request, _("favori silindi"))
    except Favoutire.DoesNotExist:
        print("zaten silinmiş")
    return render(request, "topic/new_entry.html")


def search(request):
    topic = Topic.objects.all()
    try:
        if request.method == 'POST':
            search_topic = request.POST.get('search_topic', None)
        topic_search = Topic.objects.get(title=search_topic)
        entry = Entry.objects.filter(topic__title=search_topic)
        context = {
            'topic_search': topic_search,
            'entry': entry,
            'topic': topic,
        }
        return render(request, "topic/search.html", context)
    except Topic.DoesNotExist:
        url = reverse('topics:add_topic')
        return HttpResponseRedirect(url)

def add_topic(request):
    topic = Topic.objects.all()
    if request.method == 'POST':

        title = request.POST.get('title', None)
        if len(title) == 0:
            messages.add_message(request, messages.ERROR, 'Lütfen Eksiksiz Doldurunuz')
            return HttpResponseRedirect('/')
        else:
            topic = Topic.objects.create(title=title, user_id=request.user.id)
            print(5)
            topic.save()
    context = {
        'topic': topic,
    }
    return render(request, "topic/add_topic.html", context)


