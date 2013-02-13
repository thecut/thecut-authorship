# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
