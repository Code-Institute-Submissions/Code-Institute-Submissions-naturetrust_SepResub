from django.shortcuts import render
from .models import Game, Edition, Section, Content


def all_games(request):
    """ A view to render all games available for purchase """

    games = Game.objects.all()

    template = 'games/games.html'
    context = {
        'games': games,
    }

    return render(request, template, context)
