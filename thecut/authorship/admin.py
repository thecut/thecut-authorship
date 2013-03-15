# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipMixin(object):
    """Mixin for a model admin to set created/updated by on save."""

    def save_model(self, request, obj, form, change, *args, **kwargs):
        # Set created_by / updated_by fields using request.user
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super(AuthorshipMixin, self).save_model(
            request, obj, form, change, *args, **kwargs)
