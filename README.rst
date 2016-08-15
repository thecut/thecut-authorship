=============================
Welcome to thecut-authorship
=============================

..
  .. image:: https://travis-ci.org/thecut/thecut-authorship.svg
      :target: https://travis-ci.org/thecut/thecut-authorship

  .. image:: https://codecov.io/github/thecut/thecut-authorship/coverage.svg
      :target: https://codecov.io/github/thecut/thecut-authorship

  .. image:: https://readthedocs.org/projects/thecut-authorship/badge/?version=latest
      :target: http://thecut-authorship.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

A set of Django mixins to easily record authorship information for your models.

Features
--------

    * Base model allows easy recording of authorship information.
    * Integration with Django's class-based views and forms.
    * Integration with Django's admin.


Documentation
-------------

The full documentation is at https://thecut-authorship.readthedocs.org.


Quickstart
----------

Install ``thecut-authorship`` using the installation instructions found in the project documentation.

Build a model based on ``thecut.authorship.models.Authorship`` to record authorship information on it::

    from thecut.authorship.models import Authorship

    class MyModel(Authorship):

        pass

This adds ``created_by``, ``created_at``, ``updated_by``, and ``updated_at`` to your model.

Pass a user into calls to ``.save()`` to record which user changed the object::

    example = MyModel()
    example.save(user=request.user)

If you need to update model data and there's no direct link to a website user, generate and use a site-wide 'generic' user.::

    from thecut.authorship.models import get_website_user
    example = MyModel()
    example.save(user=get_website_user())

If you wish to automatically record authorship information for changes made in the Django admin, use ``thecut.authorship.admin.AuthorshipMixin``.::

    from .models import MyModel
    from django.contrib import admin
    from thecut.authorship.admin import AuthorshipMixin

    @admin.register(MyModel)
    class MyModelAdmin(AuthorshipMixin, admin.ModelAdmin):

        pass

If you wish to integrate with ``django.forms.ModelForm``, use ``thecut.authorship.forms.AuthorshipMixin`` and ``thecut.authorship.views.AuthorshipMixin``.

In your ``forms.py``::

    from .models import MyModel
    from django import forms
    from thecut.authorship.forms import AuthorshipMixin

    class MyModelForm(forms.ModelForm):

        class Meta(object):
            model = MyModel

In your ``views.py``::

    from .forms import MyModelForm
    from .models import MyModel
    from django.views.generic import CreateView
    from thecut.authorship.views import AuthorshipMixin

    class MyModelCreateView(AuthorshipMixin, CreateView):

        form_class = MyModelForm

``MyModelCreateView`` will now automatically pass ``request.user`` through to ``MyModelForm``, which will pass it through to the model's `save()` method.


Credits
-------

See ``AUTHORS.rst``.
