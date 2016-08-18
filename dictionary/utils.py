# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _




class TimeStampModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Zamanı"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncellenme Zamanı"))

    class Meta:
        abstract = True
