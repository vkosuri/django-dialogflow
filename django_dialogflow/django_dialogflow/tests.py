import json
from django.test import TestCase
from dialogflow_lite import dialogflow
from mock import Mock
from django.core.urlresolvers import reverse


class MockResponse(object):
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    def json(self):
        return self.data


def mock_get_response(*args, **kwargs):
    url = kwargs['url']
    endpoints = {
        'https://api.dialogflow.com/v1/query': MockResponse(200, {
            "id": "b340a1f7-abee-4e13-9bdd-5e8938a48b7d",
            "timestamp": "2017-02-09T15:38:26.548Z",
            "lang": "en",
            "result": {
                "source": "agent",
                "resolvedQuery": "my name is Sam and I live in Paris",
                "action": "greetings",
                "actionIncomplete": "false",
                "parameters": {},
                "contexts": [],
                "metadata": {
                  "intentId": "9f41ef7c-82fa-42a7-9a30-49a93e2c14d0",
                  "webhookUsed": "false",
                  "webhookForSlotFillingUsed": "false",
                  "intentName": "greetings"
                },
                "fulfillment": {
                    "speech": "Hi Sam! Nice to meet you!",
                    "messages": [
                        {
                            "type": 0,
                            "speech": "Hi Sam! Nice to meet you!"
                        }
                    ]
                },
                "score": 1
            },
            "status": {
                "code": 200,
                "errorType": "success"
            },
            "sessionId": "4b6a6779-b8ea-4094-b2ed-a302ba201815"
        })
    }

    return endpoints[url]


class ViewTestCase(TestCase):

    def setUp(self):
        super(ViewTestCase, self).setUp()
        self.url = reverse('index')

    def test_get_main_page(self):
        """
        Test that the index page can be loaded.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class ApiTestCase(TestCase):
    """
    Tests to make sure that the django_dialogflow API working fine
    """

    def setUp(self):
        super(ApiTestCase, self).setUp()
        dialogflow.requests.Session.get = Mock(side_effect=mock_get_response)
        self.api_url = reverse('chat')

    def test_post(self):
        """
        Test that a response is returned.
        """
        data = {
            'text': 'How are you?'
        }
        response = self.client.post(
            self.api_url,
            data=json.dumps(data),
            content_type='application/json',
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('text', str(response.content))
