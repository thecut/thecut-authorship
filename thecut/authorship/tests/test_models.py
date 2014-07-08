# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from test_app.factories import AuthorshipModelFactory as AuthorshipFactory
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
