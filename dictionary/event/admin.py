# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import (Event, Complaint)

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic',)

@admin.register(Complaint)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'entry',)

