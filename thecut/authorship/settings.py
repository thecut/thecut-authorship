# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
"""The user model that :py:meth:`thecut.authorship.utils.get_website_user`
will query against. Defaults to ``settings.AUTH_USER_MODEL``."""

WEBSITE_USER = getattr(settings, 'AUTHORSHIP_WEBSITE_USER',
                       {'username': 'website'})
"""A dictionary that :py:meth:`thecut.authorship.utils.get_website_user` will
pass to ``get_or_create()`` in order to return the generic website user."""
