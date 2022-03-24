import json
from datetime import datetime

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.


def echo_view(request):
    response_data = {
        "method": request.method,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if request.body:
        response_data["body"] = json.loads(request.body)

    response = JsonResponse(response_data)

    return response


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def add_view(request):
    if request.method == "POST":
        dump = json.loads(request.body)
        try:
            s = int(dump['A']) + int(dump['B'])
            print('ok')
        except ValueError:
            return JsonResponse({'error': 'error'}, status=400)
        return JsonResponse({"answer": s})
    else:
        return HttpResponseNotAllowed(['POST'])


def subtract_view(request):
    if request.method == "POST":
        f = json.loads(request.body)
        try:
            s = int(f['A']) - int(f['B'])
        except ValueError:
            return JsonResponse({'error': 'error'}, status=400)
        return JsonResponse({'answer': s})
    else:
        return HttpResponseNotAllowed(['POST'])


def multiply_view(request):
    if request.method == "POST":
        f = json.loads(request.body)
        try:
            s = int(f['A']) * int(f['B'])
        except ValueError:
            return JsonResponse({'error': 'error'}, status=400)
        return JsonResponse({'answer': s})
    else:
        return HttpResponseNotAllowed(['POST'])


def divide_view(request):
    if request.method == "POST":
        f = json.loads(request.body)
        try:
            s = int(f['A'])/int(f['B'])
        except ZeroDivisionError:
            s = "Zero division error"
            return JsonResponse({'error': s}, status=400)
        except ValueError:
            return JsonResponse({'error': 'error'}, status=400)
        return JsonResponse({'answer': s})
    else:
        return HttpResponseNotAllowed(['POST'])
