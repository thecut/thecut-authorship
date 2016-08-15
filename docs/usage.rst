=====
Usage
=====

Creating a model
----------------

Subclass :py:class:`thecut.authorship.models.Authorship` to create the necessary fields::

    class MyModel(Authorship):

        pass


Saving authorship information
-----------------------------

:py:meth:`thecut.authorship.models.Authorship.save` will populate the authorship fields when necessary::

    m = MyCoolModel()
    m.save(user=request.user)

This will update the model's :py:attr:`thecut.authorship.models.Authorship.updated_by` and :py:attr:`thecut.authorship.models.Authorship.updated_at` fields automatically, as well as :py:attr:`thecut.authorship.models.Authorship.created_by` and :py:attr:`thecut.authorship.models.Authorship.created_at` if the object is new.

If the model creation / update doesn't directly relate to a user, use the site-wide generic authorship user. This can be retrieved with :py:func:`thecut.authorship.utils.get_website_user`::

    m = MyCoolModel()
    m.save(user=get_website_user())


Integrating with ``django.contrib.admin``
-----------------------------------------

You can automatically update authorship information when a model is altered in the Django admin interface by using :py:class:`thecut.authorship.admin.AuthorshipMixin`::

    class MyAdmin(AuthorshipMixin, admin.ModelAdmin):

        pass

.. HINT::
  This also applies to child inlines if they refer to subclasses of :py:class:`thecut.authorship.models.Authorship`.


Integrating with class-based views and ``ModelForm``\s
------------------------------------------------------

Use :py:class:`thecut.authorship.views.AuthorshipMixin` on your :py:class:`django.views.generic.edit.ModelFormMixin`-based views (:py:class:`django.views.generic.edit.CreateView`, :py:class:`django.views.generic.edit.UpdateView`.etc)::

    class MyModelCreateView(AuthorshipMixin, CreateView):

        form_class = MyModelForm

Then, use :py:class:`thecut.authorship.forms.AuthorshipMixin` on your :py:class:`django.forms.ModelForm`-based forms::

    class MyModelForm(AuthorshipMixin, ModelForm):

        class Meta(object):
            model = MyModel

Together, these mixins will—upon a successful form submission—appropriately record ``request.user`` on the target object.

.. WARNING::
  You must use :py:class:`thecut.authorship.views.AuthorshipMixin` on the view *and* :py:class:`thecut.authorship.forms.AuthorshipMixin` on the form for this to work.
