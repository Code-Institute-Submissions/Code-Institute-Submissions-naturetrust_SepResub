from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('update-details/', views.profile_form, name='profile_form'),
    path('my-orders/', views.user_orders, name='user_orders'),
    path('my-games/', views.profile_games, name='profile_games'),
    path('my-adoptions/', views.profile_adoptions, name='profile_adoptions'),
]
