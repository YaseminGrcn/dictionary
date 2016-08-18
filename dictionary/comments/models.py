# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from dictionary.utils import TimeStampModel
from django.utils.translation import ugettext_lazy as _
from dictionary.users.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class CommentTitle(TimeStampModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Yorum Basligi")
    )
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name=_("Kullanici")
    )
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Comments(TimeStampModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_("Yorum"),
    )

    comment = models.ForeignKey(
        CommentTitle,
        blank=True,
        null=True,
        verbose_name=_("Yorum Basligi")
    )

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name=_("Kullanici"),
    )
    def __str__(self):
        return self.title
