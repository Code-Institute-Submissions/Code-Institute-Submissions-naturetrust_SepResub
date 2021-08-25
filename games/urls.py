from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.all_games, name='games'),
    path('<game_title>/', views.game_details, name='game_details'),
    path('buy/<game_title>/', views.buy_game_page, name='buy_game'),
]
