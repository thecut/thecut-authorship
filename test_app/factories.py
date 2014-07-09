# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import AuthorshipModel
from thecut.authorship.factories import AuthorshipFactory


class AuthorshipModelFactory(AuthorshipFactory):

    class Meta(object):
        model = AuthorshipModel
