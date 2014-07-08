# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import AuthorshipModel
import factory


class AuthorshipModelFactory(factory.DjangoModelFactory):

    created_by = factory.SubFactory('test_app.factories.UserFactory')
    updated_by = factory.LazyAttribute(lambda o: o.created_by)

    class Meta(object):
        model = AuthorshipModel


class UserFactory(factory.DjangoModelFactory):

    username = factory.Sequence(lambda n: 'User {0}'.format(n))

    class Meta(object):
        model = 'auth.User'
        django_get_or_create = ('username',)
