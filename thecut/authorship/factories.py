# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

try:
    from faker import Factory as FakerFactory
except ImportError, error:
    message = '{0}. Try running `pip install fake-factory`.'.format(error)
    raise ImportError(message)

try:
    import factory
except ImportError, error:
    message = '{0}. Try running `pip install factory_boy`.'.format(error)
    raise ImportError(message)


faker = FakerFactory.create()


class AuthorshipFactory(factory.django.DjangoModelFactory):

    class Meta(object):
        abstract = True

    created_by = factory.SubFactory('thecut.authorship.factories.UserFactory')

    updated_by = factory.SelfAttribute('created_by')


class UserFactory(factory.django.DjangoModelFactory):

    class Meta(object):
        model = 'auth.User'
        django_get_or_create = ['username']

    username = factory.Sequence(lambda n: 'user-{0}'.format(n))


class UserFakerFactory(UserFactory):

    class Meta(object):
        model = 'auth.User'
        django_get_or_create = ['username']

    first_name = factory.LazyAttribute(lambda o: faker.first_name())

    last_name = factory.LazyAttribute(lambda o: faker.last_name())

    username = factory.LazyAttribute(
        lambda o: '{0}.{1}'.format(o.first_name.lower(), o.last_name.lower()))

    email = factory.LazyAttribute(
        lambda o: '{0}@example.com'.format(o.username))
