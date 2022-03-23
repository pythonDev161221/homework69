from django.urls import path

from api_v1.views import add_view, get_csrf_token_view, subtract_view

urlpatterns = [
    path('add/', add_view, name='add'),
    path('csrftoken/', get_csrf_token_view, name='token'),
    path('subtract/', subtract_view, name='subtract'),

]
