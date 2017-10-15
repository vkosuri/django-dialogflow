# Django Dialogflow

[![Package Version](https://img.shields.io/pypi/v/django-dialogflow.svg)](https://pypi.python.org/pypi/django-dialogflow/)
[![Build Status](https://travis-ci.org/vkosuri/django-dialogflow.svg?branch=master)](https://travis-ci.org/vkosuri/django-dialogflow)

Django [Dialogflow](https://dialogflow.com) is a web client to chat.

## Using the development version

You can clone the git repository by doing the following:

``` Bash
$ git clone git://github.com/vkosuri/django-dialogflow.git
```

## Production your Bot

Start the Django app by running

``` Bash
python manage.py runserver 0.0.0.0:8000
```

Further documentation on getting set up with Django and ChatterBot can be found in the ChatterBot documentation

## ALLOWD_HOSTS

Modify Django Allowed hosts to access your application everywhere, to do this modify settings.py as suggested below

``` Python
ALLOWED_HOSTS = ['A.B.C.D', 'localhost']
```

## CORS_ORIGIN_WHITELIST

Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources (e.g. fonts) on a web page to be requested from another domain outside the domain from which the first resource was served.

To do this modify settings.py as suggested below

``` Python
CORS_ORIGIN_WHITELIST = (
    'A.B.C.D:9000',
)
```

## Installation

If you are trying ``django_dialogflow`` as app,

Then you could install django-dialogflow either via the Python Package Index (PyPI) or from source.

To install using pip :

``` Bash
$ pip install django-dialogflow
```

and then add it to your installed apps:

``` Bash
INSTALLED_APPS = (
    ...
    'django_dialogflow',
    ...
)
```

You will then want to create the necessary tables. If you generating schema migrations, you'll want to run:

``` Bash
$ python manage.py migrate django_dialogflow
```

## Examples

All [examples](./examples) are located here Github repo

## Motivation

https://github.com/gunthercox/django_chatterbot

## LICENSE
Licensed under [MIT](./LICENSE.md)

## Contributing

Development of django_dialogflow happens at Github: http://github.com/vkosuri/django-dialogflow

You are highly encouraged to participate in the development. If you don't like Github (for some reason) you're welcome to send regular patches.