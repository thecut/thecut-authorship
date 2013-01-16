# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class AbstractAuthorshipModel(models.Model):
    """Track when a record was created/updated and by whom.

    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    """:py:class:`datetime` for when this object was first created."""

    created_by = models.ForeignKey('auth.User', editable=False,
                                   related_name='+')
    """:py:class:`~django.contrib.auth.models.User` who first created this
    object (required)."""

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    """:py:class:`datetime` for when this object was last saved."""

    updated_by = models.ForeignKey('auth.User', editable=False,
                                   related_name='+')
    """:py:class:`~django.contrib.auth.models.User` who last saved this
    object (required)."""

    class Meta(object):
        abstract = True

    def save(self, user=None, **kwargs):
        if user is not None:
            if not self.pk:
                self.created_by = user
            self.updated_by = user
        return super(AbstractAuthorshipModel, self).save(**kwargs)
