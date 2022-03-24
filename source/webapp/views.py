from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy


def index_view(request):
    return render(request, 'index.html')
