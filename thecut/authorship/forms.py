# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipFormMixin(object):
    """Set the ``created_by`` and ``updated_by`` fields on a model.

    Requires that a ``User`` instance be passed in to the constructor. Views
    that inherit from ``AuthorshipViewMixin`` automatically pass this in.

    """

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AuthorshipFormMixin, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.updated_by = self.user
        if not self.instance.pk:
            self.instance.created_by = self.user

        return super(AuthorshipFormMixin, self).save(*args, **kwargs)
