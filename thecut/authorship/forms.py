# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipFormMixin(object):
    """Mixin for a :py:class:`~django.forms.ModelForm` which sets
    ``created_by`` and ``updated_by`` fields for the instance when saved.

    Requires that a ``User`` instance be passed in to the constructor. Views
    which utilise :py:class:`~thecut.authorship.views.AuthorshipViewMixin`
    handle this already.

    """

    def __init__(self, user, *args, **kwargs):
        """

        :param user: A user instance, used to set ``created_by`` /
            ``updated_by`` fields on save.

        """
        self.user = user
        super(AuthorshipFormMixin, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.updated_by = self.user
        if not self.instance.pk:
            self.instance.created_by = self.user

        return super(AuthorshipFormMixin, self).save(*args, **kwargs)
