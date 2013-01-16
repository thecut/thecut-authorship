# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipFormMixin(object):
    """Set the ``created_by`` and ``updated_by`` fields on a model.

    This form requires that a property, ``self.user`` be set to an instance of
    :py:class`~django.contrib.auth.models.User` before the ``save()`` method is
    called.

    """

    def save(self, *args, **kwargs):
        self.instance.updated_by = self.user
        if not self.instance.pk:
            self.instance.created_by = self.user

        return super(AuthorshipFormMixin, self).save(*args, **kwargs)
