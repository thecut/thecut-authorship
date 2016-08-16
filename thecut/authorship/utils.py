# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import settings
from django.contrib.auth import get_user_model


def get_website_user():
    """Get a generic 'website' user.

    Can be used to specify the required user when there is no direct link to
    a real user.

    """

    UserModel = get_user_model()
    user, created = UserModel.objects.get_or_create(**settings.WEBSITE_USER)

    if created:
        user.set_unusable_password()
        user.is_active = False
        user.save()

    return user
