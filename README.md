# django-apiai

Django [API.AI](https://api.ai/) is a web client to chat.

## How to train
In progress

## Development
To make development environment clone this repository

git clone https://github.com/vkosuri/django-apiai.git

``` Bash
virtualenv venv
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt
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

## Examples
All examples are located here https://github.com/vkosuri/django-apiai/tree/master/examples
## Motivation
https://github.com/gunthercox/django_chatterbot

## LICENSE
Licensed under MIT https://github.com/vkosuri/django-apiai/blob/master/LICENSE.md