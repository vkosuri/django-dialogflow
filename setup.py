#!/usr/bin/env python

"""
Django Dialogflow setup file.
"""

from setuptools import setup


# Dynamically retrieve the version information from the django_dialogflow module
DJANGO_DIALOGFLOW = __import__('django_dialogflow')
VERSION = DJANGO_DIALOGFLOW.__version__
AUTHOR = DJANGO_DIALOGFLOW.__author__
AUTHOR_EMAIL = DJANGO_DIALOGFLOW.__email__
URL = DJANGO_DIALOGFLOW.__url__
DESCRIPTION = 'Django Dialogflow chat agent'
LONG_DESCRIPTION = 'Django Dialogflow chat agent'

with open('requirements.txt') as requirements:
    REQUIREMENTS = requirements.readlines()

setup(
    name='django-dialogflow',
    version=VERSION,
    url=URL,
    download_url='{}/tarball/{}'.format(URL, VERSION),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=[
        'django_dialogflow',
    ],
    package_dir={'django_dialogflow': 'django_dialogflow'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='BSD',
    zip_safe=True,
    platforms=['any'],
    keywords=['Django', 'Dialogflow', 'api.ai', 'chat', 'bot'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
