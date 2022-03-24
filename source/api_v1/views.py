import json
from datetime import datetime

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.


def echo_view(request):
    response_data = {
        "method": request.method,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    print(request.body)
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
        print('POST')
    dump = json.loads(request.body)

    try:
        s = int(dump['A']) + int(dump['B'])
    except:
        s = "Need to input two numbers"
    print(s)
    return JsonResponse({"answer": s})


def subtract_view(request):
    f = json.loads(request.body)
    s = int(f['A']) - int(f['B'])
    return JsonResponse({'answer': s})


def multiply_view(request):
    f = json.loads(request.body)
    s = int(f['A']) * int(f['B'])
    return JsonResponse({'answer': s})


def divide_view(request):
    f = json.loads(request.body)
    s = int(f['A'])/int(f['B'])
    return JsonResponse({'answer': s})
