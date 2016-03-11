# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..utils import get_website_user
from django.test import TestCase


class TestGetWebsiteUser(TestCase):

    """Tests for get_website_user()."""

    def test_get_website_user_returns_user(self):
        """Test if something is returned."""
        user = get_website_user()
        self.assertTrue(user)

    def test_get_website_user_returns_same_user(self):
        """Test if the same user is returned over multiple calls."""
        user = get_website_user()
        self.assertEqual(get_website_user(), user)
