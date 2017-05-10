from __future__ import print_function
import codecs
import io
import os
from thecut.authorship import __version__
from setuptools import setup, find_packages
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        filename = os.path.join(here, filename)
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'HISTORY.rst')

setup(
    # General information
    name='thecut-authorship',
    version=__version__,

    # Packaging
    packages=find_packages(exclude=['docs']),
    namespace_packages=['thecut'],
    include_package_data=True,

    # Dependencies
    install_requires=[],

    # Author information
    author='The Cut Creative',
    author_email='development@thecut.net.au',

    # Additional information
    url='https://github.com/thecut/thecut-authorship',
    license='Apache Software License 2.0',
    description='A set of Django mixins to easily record authorship '
                'information for your models.',
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
    ],
)
