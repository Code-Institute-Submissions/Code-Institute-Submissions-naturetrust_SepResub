from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.all_adoptions, name='adoptions'),
    path('adopt/<animal>', views.adoption_package, name='adopt'),
]
