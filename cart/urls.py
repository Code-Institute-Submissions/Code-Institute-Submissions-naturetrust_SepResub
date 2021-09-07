from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('<item_id>/', views.add_to_cart, name='add_to_cart'),
]
