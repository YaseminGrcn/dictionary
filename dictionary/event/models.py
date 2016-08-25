# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from dictionary.users.models import User
from dictionary.topics.models import Topic, Entry
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Event(models.Model):
    topic = models.ForeignKey(
        Topic,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = (('topic', 'user'),)
        verbose_name_plural = _("Takip Etme Olayları")

    def __str__(self):
        return self.user.username

@python_2_unicode_compatible
class Complaint(models.Model):
    entry = models.ForeignKey(
        Entry,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = (('entry', 'user'),)
        verbose_name_plural = _("Şikayetler")

    def __str__(self):
        return self.user.username


