# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from faker import Factory as FakerFactory
import factory


faker = FakerFactory.create()


class AuthorshipFactory(factory.django.DjangoModelFactory):

    ABSTRACT_FACTORY = True

    created_by = factory.SubFactory('thecut.authorship.factories.UserFactory')

    updated_by = factory.SelfAttribute('created_by')


class UserFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = 'auth.User'

    FACTORY_DJANGO_GET_OR_CREATE = ['username']

    username = factory.Sequence(lambda n: 'user-{0}'.format(n))


class UserFakerFactory(UserFactory):

    FACTORY_FOR = 'auth.User'

    FACTORY_DJANGO_GET_OR_CREATE = ['username']

    first_name = factory.LazyAttribute(lambda o: faker.first_name())

    last_name = factory.LazyAttribute(lambda o: faker.last_name())

    username = factory.LazyAttribute(
        lambda o: '{0}.{1}'.format(o.first_name.lower(), o.last_name.lower()))

    email = factory.LazyAttribute(
        lambda o: '{0}@example.com'.format(o.username))
