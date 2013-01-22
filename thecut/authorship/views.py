# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipViewMixin(object):
    """Add the request's ``User`` instance to the form kwargs."""

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(AuthorshipViewMixin, self).get_form_kwargs(
            *args, **kwargs)
        form_kwargs.update({'user': self.request.user})
        return form_kwargs
