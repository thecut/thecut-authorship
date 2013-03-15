# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from thecut.authorship import settings
import warnings


class Authorship(models.Model):
    """Abstract model to track when an instance was created/updated and by
    whom.

    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    """:py:class:`datetime` for when this object was first created."""

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
                                   related_name='+')
    """User who first created this object (required)."""

    updated_at = models.DateTimeField(auto_now=True, editable=False)
    """:py:class:`datetime` for when this object was last saved."""

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
                                   related_name='+')
    """User who last saved this object (required)."""

    class Meta(object):
        abstract = True

    def save(self, user=None, **kwargs):
        if user is not None:
            if not self.pk:
                self.created_by = user
            self.updated_by = user
        return super(Authorship, self).save(**kwargs)


class AbstractAuthorshipModel(Authorship):
    """AbstractAuthorshipModel is deprecated. Use Authorship model instead."""
    # Renamed for consistency with publishing models.

    class Meta(Authorship.Meta):
        abstract = True

    def __init__(self, *args, **kwargs):
        warnings.warn('AbstractAuthorshipModel is deprecated - use Authorship '
                      'model instead.', DeprecationWarning, stacklevel=2)
        return super(AbstractAuthorshipModel, self).__init__(*args, **kwargs)
