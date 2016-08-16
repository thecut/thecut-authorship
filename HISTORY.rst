.. :changelog:

=======
History
=======


1.0 (2016-08-16)
----------------

* Removed deprecated APIs.
* Removed compatibility code for unsupported versions of Django.
* Improved test coverage.
* Removed code paths in ``Authorship.save()`` that could not logically be reached.


0.11 (2016-08-16)
-----------------

* Rewrote documentation.
* Redesigned testing environment.


0.10.1 (2015-11-19)
-------------------

* Fixed bug when saving on Django 1.4
* Started using ``unittest`` from Python standard library. Removes Python < 2.7 support.
* Updated tox configuration to test against newer versions of Django / Python.
* Fixed bug that stopped authorship information being updated when ``update_fields`` is defined but empty.


0.10 (2015-10-09)
-----------------

* Test against Django 1.8
* Fixed bug where models were incorrectly detected as 'not new' (for the purpose of setting ``created_at`` and ``created_by``) when a pk is manually specified.


0.9 (2015-08-25)
----------------

* Set ``on_delete=models.PROTECT` on authorship fields that relate to users.


0.7.1 (2014-12-11)
------------------

* Ensure that ``created_at`` and ``created_by`` are updated regardless of the contents of ``update_fields``.
* Added Django admin mixin to save authorship information when using inlines.


0.7 (2014-11-24)
----------------

* Updated documentation.
* Removed ``Makefile``.
* Altered testing environment to support Django 1.7
* Added Django 1.7 ``AppConfig``.


0.5.3 (2014-07-09)
------------------

* Added unit tests for model and form mixin.
* Improved Python 3 compatibility.
* Updated test environment to test against newer versions of Django.
* Ensure that ``updated_at`` and ``updated_by`` are updated regardless of the contents of ``update_fields``.

0.5.2 (2014-06-20)
------------------

* Added ``AuthorshipFactory`` for testing.


0.5.1 (2014-03-19)
------------------

* Removed ``distribute`` from the install_requires list.


0.5 (2013-03-15)
----------------

* First release.
