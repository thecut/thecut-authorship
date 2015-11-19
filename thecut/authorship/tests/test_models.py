# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from django import VERSION as DJANGO_VERSION
from test_app.factories import AuthorshipModelFactory as AuthorshipFactory
from test_app.models import AuthorshipModel
from unittest import skipIf
from thecut.authorship.factories import UserFakerFactory


class TestAuthorshipModel(TestCase):

    def test_sets_created_by_when_model_instance_is_first_saved(self):
        authored = AuthorshipFactory.build()
        user = UserFakerFactory()

        authored.save(user=user)

        self.assertEqual(user, authored.created_by)

    def test_sets_updated_by_when_model_instance_is_saved(self):
        authored = AuthorshipFactory()
        update_user = UserFakerFactory(username='update user')

        authored.save(user=update_user)

        self.assertEqual(update_user, authored.updated_by)

    def test_does_not_change_created_by_when_model_instance_is_saved(self):
        authored = AuthorshipFactory()
        update_user = UserFakerFactory(username='update user')

        authored.save(user=update_user)

        self.assertNotEqual(update_user, authored.created_by)

    @skipIf(DJANGO_VERSION < (1, 5),
            'update_fields argument not supported in this version of Django.')
    def test_sets_updated_at_if_update_fields_is_specified(self):
        authored = AuthorshipFactory()
        original_updated_at = authored.updated_at

        authored.save(update_fields=[])
        authored = AuthorshipModel.objects.get(pk=authored.pk)

        self.assertGreater(authored.updated_at, original_updated_at)

    @skipIf(DJANGO_VERSION < (1, 5),
            'update_fields argument not supported in this version of Django.')
    def test_sets_updated_by_if_update_fields_is_specified(self):
        authored = AuthorshipFactory()
        update_user = UserFakerFactory(username='update user')

        authored.save(user=update_user, update_fields=['updated_at'])
        updated = AuthorshipModel.objects.get(pk=authored.pk)

        self.assertEqual(updated.updated_by, update_user)
