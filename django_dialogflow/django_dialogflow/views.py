
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.conf import settings
from dialogflow_lite.dialogflow import Dialogflow

import json


def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data


@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'app.html')


@require_http_methods(['POST'])
def chat_view(request):
    dialogflow = Dialogflow(**settings.DIALOGFLOW)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['text']
    responses = dialogflow.text_request(str(input_text))

    if request.method == "GET":
        # Return a method not allowed response
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }
        return JsonResponse(data, status=405)
    elif request.method == "POST":
        data = {
            'text': responses[0],
        }
        return JsonResponse(data, status=200)
    elif request.method == "PATCH":
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)

    elif request.method == "DELETE":
        data = {
            'detail': 'You should make a POST request to this endpoint.',
            'name': '/chat'
        }

        # Return a method not allowed response
        return JsonResponse(data, status=405)
