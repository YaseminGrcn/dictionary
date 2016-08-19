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

def profile_detail(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, "users/profile.html", context)

