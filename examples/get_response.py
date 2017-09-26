
import requests
import uuid


class ApiAi(object):

    # create session
    s = requests.Session()

    # API.AI query url
    url = 'https://api.api.ai/v1/query'

    # Headers
    headers = {}

    # https://api.ai/docs/reference/agent/#versioning
    api_versioning = '20150910'

    # https://api.ai/docs/reference/agent/#languages
    language = 'en'
    session_id = uuid.uuid4().hex
    timezone = 'Asia/Kolkata'

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


if __name__ == '__main__':
    # demo agent access token: e5dc21cab6df451c866bf5efacb40178
    client_access_token = '86773b26ca554576971f45baff906bce'

    api_ai = ApiAi(client_access_token);
    response = api_ai.get_response('how are you')
    print(response)
    response = api_ai.get_response('howz the weather today')
    print(response)

