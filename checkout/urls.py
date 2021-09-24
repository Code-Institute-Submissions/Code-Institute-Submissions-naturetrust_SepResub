from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'success/<order_number>',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
    path('wh/', webhook, name='webhook'),
]
