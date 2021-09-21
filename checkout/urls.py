from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<order_number>', views.checkout_success, name='checkout_success'),
]
