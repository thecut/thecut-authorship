# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from django import forms
from mock import patch
from test_app.models import AuthorshipModel
from thecut.authorship.factories import UserFactory
from thecut.authorship.forms import AuthorshipMixin


class AuthorshipModelForm(AuthorshipMixin, forms.ModelForm):

    class Meta:
        model = AuthorshipModel
        fields = []


class DummyUser(object):

    pass


class TestAuthorshipMixin(TestCase):

    def test_requires_an_extra_argument_on_creating_an_instance(self):
        """Ensure that
        :py:class:`thecut.authorship.forms.AuthorshipMixin`-based forms cannot
        be instantiated without passing in a user."""
        self.assertRaises(TypeError, AuthorshipModelForm)

    def test_sets_user_attribute(self):
        """Ensure that
        :py:class:`thecut.authorship.forms.AuthorshipMixin`-based forms
        properly set :py:attr:`thecut.authorship.forms.AuthorshipMixin.user`
        when one is passed on instantiation."""
        dummy_user = DummyUser()

        form = AuthorshipModelForm(user=dummy_user)

        self.assertEqual(dummy_user, form.user)


class DummyUnsavedModel(object):

    def __init__(self):
        self.created_at = None


class TestAuthorshipMixinSave(TestCase):

    @patch('django.forms.ModelForm.save')
    def test_calls_super_class_save_method(self, superclass_save):

        """Ensure that
        :py:meth:`thecut.authorship.forms.AuthorshipMixin.save` calls the
        superclass's save method.."""
        form = AuthorshipModelForm(user=UserFactory())
        form.instance = DummyUnsavedModel()

        form.save()

        self.assertTrue(superclass_save.called)

    @patch('django.forms.ModelForm.save')
    def test_sets_updated_by_to_given_user(self, superclass_save):
        """Ensure that
        :py:class:`thecut.authorship.forms.AuthorshipMixin`-based forms
        appropriately set
        :py:attr:`thecut.authorship.models.AuthorshipMixin.updated_by` when
        a user is provided."""
        user = DummyUser()
        form = AuthorshipModelForm(user=user)
        form.instance = DummyUnsavedModel()
        form.cleaned_data = {}

        form.save()

        self.assertEqual(user, form.instance.updated_by)

    @patch('django.forms.ModelForm.save')
    def test_sets_created_by_if_instance_is_not_saved(self, superclass_save):
        """Ensure that
        :py:class:`thecut.authorship.forms.AuthorshipMixin`-based forms
        appropriately set
        :py:attr:`thecut.authorship.models.AuthorshipMixin.created_by` when
        a user is provided and the target object has not been saved before."""
        user = DummyUser()
        form = AuthorshipModelForm(user=user)
        form.instance = DummyUnsavedModel()
        form.cleaned_data = {}

        form.save()

        self.assertEqual(user, form.instance.created_by)

    @patch('django.forms.ModelForm.save')
    def test_does_not_set_created_by_if_instance_is_saved(self,
                                                          superclass_save):
        """Ensure that
        :py:class:`thecut.authorship.forms.AuthorshipMixin`-based forms do
        not set
        :py:attr:`thecut.authorship.models.AuthorshipMixin.created_by` if the
        target object has already been saved."""
        class DummySavedModel(object):

            def __init__(self):
                self.created_at = 'arbitrary-value'
                self.created_by = 'arbitrary-value'

        user = DummyUser()
        form = AuthorshipModelForm(user=user)
        form.instance = DummySavedModel()
        form.cleaned_data = {}

        form.save()

        self.assertNotEqual(user, form.instance.created_by)
