from django.urls import path

from api_v1.views import add_view, get_csrf_token_view, subtract_view, \
    multiply_view, divide_view, echo_view

app_name = "api_v1"

urlpatterns = [
    path('add/', add_view, name='add_view'),
    path('csrftoken/', get_csrf_token_view, name='token_view'),
    path('subtract/', subtract_view, name='subtract_view'),
    path('multiply/', multiply_view, name='multiply_view'),
    path('divide/', divide_view, name='divide_view'),
    path('echo/', echo_view, name='echo_view'),
]
