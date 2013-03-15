# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import warnings


class AuthorshipMixin(object):
    """Adds the request's ``User`` instance to the form kwargs."""

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(AuthorshipMixin, self).get_form_kwargs(*args,
                                                                   **kwargs)
        form_kwargs.update({'user': self.request.user})
        return form_kwargs


class AuthorshipViewMixin(AuthorshipMixin):
    """AuthorshipViewMixin is deprecated. Use AuthorshipMixin instead."""
    # Renamed for consistency with other mixins.

    def __init__(self, *args, **kwargs):
        warnings.warn('AuthorshipViewMixin is deprecated - use '
                      'AuthorshipMixin instead.', DeprecationWarning,
                      stacklevel=2)
        return super(AuthorshipViewMixin, self).__init__(*args, **kwargs)
