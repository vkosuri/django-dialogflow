
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
import json
import requests
import uuid


class ApiAi(object):
    """
    Subclass this mixin for access to the 'chat' attribute.
    """

    # create session
    s = requests.Session()

    # API.AI query url
    url = settings.API_URL

    api_version = settings.API_VERSION

    # Headers
    headers = {}

    # https://api.ai/docs/reference/agent/#languages
    language = settings.LANGUAGE_CODE.split('-')[0]
    session_id = uuid.uuid4().hex
    timezone = settings.TIME_ZONE

    def __init__(self, client_access_token):
        """ Create Session: create a HTTP session to a server
        """
        self.headers = {
            'Authorization': 'Bearer ' + client_access_token,
        }
        self.s.headers.update(self.headers)

        self.s.mount('http://', requests.adapters.HTTPAdapter())
        self.s.mount('https://', requests.adapters.HTTPAdapter())

        self.url = self.url

    def get_response(self, text):
        params = (
            ('v', self.api_versioning),
            ('query', text),
            ('lang', self.language),
            ('sessionId', self.session_id),
            ('timezone', self.timezone),
        )
        responses = []
        result = self.s.get(url=self.url, params=params).json()
        if result['status']['errorType'] == 'success':
            for msg in result['result']['fulfillment']['messages']:
                responses.append(msg['speech'])
        else:
            print('Failed to response from: ' + api_ai.url)

        return responses

