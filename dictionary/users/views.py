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
from django.shortcuts import get_object_or_404
from dictionary.topics.models import Topic, Category, Entry, Favoutire


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

def profile_login(request):
    if request.user.is_authenticated():
        url = reverse('base')
        return HttpResponseRedirect(url)
    if request.method == 'GET':
        return render(request, "account/login.html")

    elif request.method == 'POST':

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        try:
            authenticate_check = authenticate(username=username, password=password)
        except User.DoesNotExist:
            user = False
            messages.add_message(request, messages.ERROR, 'Böyle Bir Kullanıcı Bulunamadı')
            return HttpResponseRedirect('/login')

        if authenticate_check:
            login(request, authenticate_check)
            messages.add_message(request, messages.INFO, 'Hoşgeldiniz ')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Giriş Hatası')
            return HttpResponseRedirect('/login/')

def profile_detail(request, id):
    user = get_object_or_404(User, id=id)
    topic = Topic.objects.all()
    context = {
        'user': user,
        'topic': topic,
    }
    return render(request, "users/profile.html", context)
def base(request):
    user = request.user
    topic = Topic.objects.all()
    category = Category.objects.all()
    context = {
        'user': user,
        'topic': topic,
        'category': category,
    }
    return render(request, "base.html", context)




