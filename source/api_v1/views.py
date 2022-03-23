import json

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def add_view(request):
    dump = json.loads(request.body)
    s = int(dump['A']) + int(dump['B'])
    dict_s = {'answer': s}
    return JsonResponse(dict_s)


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
