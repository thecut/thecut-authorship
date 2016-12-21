# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class AuthorshipMixin(object):

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,
                        updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
