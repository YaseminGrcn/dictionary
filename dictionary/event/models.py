# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from dictionary.users.models import User
from dictionary.topics.models import Topic

@python_2_unicode_compatible
class Event(models.Model):
    topic = models.ForeignKey(
        Topic,
    )
    user = models.ForeignKey(
        User,
    )

    class Meta:
        unique_together = (('topic', 'user'),)

    def __str__(self):
        return self.username
