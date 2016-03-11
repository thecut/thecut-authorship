=================
thecut.authorship
=================

There is no need to add ``thecut.authorship`` to your project's
``INSTALLED_APPS`` setting, as it provides only abstract models.

Testing
=======

To run the project's tests, first set up a virtual environment for running the
tests::
    virtualenv /path/to/virtual/environment
    source /path/to/virtual/environment/bin/activate
    pip install -r requirements-test.txt

To run the tests for your current environemt::
    DJANGO_SETTINGS_MODULE=test_app.settings django-admin.py test authorship

To run the tests against Python versions 2.7, 3.4, and 3.5::
    tox --recreate
