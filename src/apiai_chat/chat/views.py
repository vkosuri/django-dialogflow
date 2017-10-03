
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import requests
import uuid


@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'app.html')


@require_http_methods(['GET', 'POST'])
def chat_view(request):
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

    headers = {
        'Authorization': 'Bearer 86773b26ca554576971f45baff906bce'
    }

    s.headers.update(headers)

    s.mount('http://', requests.adapters.HTTPAdapter())
    s.mount('https://', requests.adapters.HTTPAdapter())

    params = (
        ('v', api_versioning),
        ('query', request.POST.text),
        ('lang', language),
        ('sessionId', session_id),
        ('timezone', timezone),
    )
    responses = []
    result = s.get(url=url, params=params).json()
    if result['status']['errorType'] == 'success':
        for msg in result['result']['fulfillment']['messages']:
            responses.append(msg['speech'])
    else:
        print('Failed to response from: ' + url)

    if request.method == "GET":
        # Return a method not allowed response
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': 'API.AI'
        }
        return JsonResponse(data, status=405)
    elif request.method == "POST":
        data = {
            'text': responses,
        }
        return JsonResponse(data, status=200)
    elif request.method == "PATCH":
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    elif request.method == "DELETE":
        data = {
            'detail': 'You should make a POST request to this endpoint.'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)
