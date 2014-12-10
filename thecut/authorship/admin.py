# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import Authorship


class AuthorshipInlineMixin(object):
    """Mixin for a model admin to set created/updated by on save for related
    inline models."""

    def save_formset(self, request, form, formset, *args, **kwargs):
        if issubclass(formset.model, Authorship):
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save(user=request.user)
            formset.save_m2m()
            for obj in formset.deleted_objects:
                obj.delete()
        else:
            return super(AuthorshipInlineMixin, self).save_formset(
                request, form, formset, *args, **kwargs)


class AuthorshipMixin(AuthorshipInlineMixin):
    """Mixin for a model admin to set created/updated by on save."""

    def save_model(self, request, obj, form, change, *args, **kwargs):
        # Set created_by / updated_by fields using request.user
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super(AuthorshipMixin, self).save_model(request, obj, form,
                                                       change, *args, **kwargs)
