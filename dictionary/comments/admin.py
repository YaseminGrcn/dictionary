# -*- encoding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from .models import (CommentTitle, Comments)

@admin.register(CommentTitle)
class CommentTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    search_fields = ("title",)
    ordering = ("title",)
    list_display_links = list_display

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("title", "user","comment")
    search_fields = ("title",)
    ordering = ("title",)
    list_display_links = list_display

