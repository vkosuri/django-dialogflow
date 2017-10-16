# Django Dialogflow

[![Package Version](https://img.shields.io/pypi/v/django-dialogflow.svg)](https://pypi.python.org/pypi/django-dialogflow/)
[![Build Status](https://travis-ci.org/vkosuri/django-dialogflow.svg?branch=master)](https://travis-ci.org/vkosuri/django-dialogflow)

Django [Dialogflow](https://dialogflow.com) is a web client to chat.

## Table of contents

1. [API View](#api-view)
2. [Sync your database](#sync-your-database)
3. [Production your BOT](#production-your-bot)
4. [Installation](#installation)
5. [Configuring Webservice](#configuring-webservice)
6. [Examples](#examples)
7. [Motivation](#motivation)l
8. [License](#license)
9. [Contributing](#contributing)

## API View

If you need a django_dialogflow API endpoint you will want to add the following to your [urls.py](./django_dialogflow/urls.py)

``` Python
urlpatterns = [
    url(r'chat/$', chat_view, name='chat'),
    url(r'^$', index_view, name='index'),
    url(r'^admin/', admin.site.urls),
]

```

The endpoint expects a JSON request with the following data:

``` Python
{"text": "My input statement"}
```

See detailed example how retrieve end point translated information [app.html](.django_dialogflow/django_dialogflow/templates/app.html)


## Sync your database

You will then want to create the necessary tables. If you generating schema migrations, you'll want to run:

``` Bash
$ python manage.py migrate django_dialogflow
```

## Production your Bot

### Configuring Dialogflow

To configure Dialogflow [client access token](https://dialogflow.com/docs/reference/agent/#using_access_tokens), go [settings.py](./django_dialogflow/settings.py)

``` Python
# Dialogflow settings
DIALOGFLOW = {
    'client_access_token': 'e5dc21cab6df451c866bf5efacb40178',
}
```

### ALLOWD_HOSTS

Modify Django Allowed hosts to access your application everywhere, to do this modify settings.py as suggested below

``` Python
ALLOWED_HOSTS = ['A.B.C.D', 'localhost']
```

### CORS_ORIGIN_WHITELIST

Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources (e.g. fonts) on a web page to be requested from another domain outside the domain from which the first resource was served.

To do this modify settings.py as suggested below

``` Python
CORS_ORIGIN_WHITELIST = (
    'A.B.C.D:9000',
)
```

### Deploy

``` Bash
python manage.py runserver 0.0.0.0:8000
```

Further documentation on getting set up with Django and ChatterBot can be found in the ChatterBot documentation

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


## Configuring Webservice

If you want to host your Django app, you need to choose a method through which it will be hosted. There are a few free services that you can use to do this such as [Heroku](https://dashboard.heroku.com/) and [PythonAnyWhere](https://www.pythonanywhere.com/details/django_hosting).

### WSGI

A common method for serving Python web applications involves using a Web Server Gateway Interface (WSGI) package.

Gunicorn is a great choice for a WSGI server. They have detailed documentation and installation instructions on their website.

### Hosting static files

There are numerous ways to host static files for your Django application. One extreemly easy way to do this is by using WhiteNoise, a python package designed to make it possible to serve static files from just about any web application.

## Using the development version

You can clone the git repository by doing the following:

``` Bash
$ git clone git://github.com/vkosuri/django-dialogflow.git
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