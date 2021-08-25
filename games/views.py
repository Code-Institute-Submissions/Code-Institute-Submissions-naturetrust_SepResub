from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Game, Edition, Section, Content


def all_games(request):
    """ A view to render all games available for purchase """

    games = Game.objects.all()

    template = 'games/games.html'
    context = {
        'games': games,
    }

    return render(request, template, context)


def game_details(request, game_title):
    """ A view to show individual game details """

    game = get_object_or_404(Game, url_name=game_title)
    editions = Edition.objects.filter(game=game)
    sections = Section.objects.filter(game=game)
    content = Content.objects.filter(game=game)

    template = 'games/game-details.html'
    context = {
        'game': game,
        'editions': editions,
        'sections': sections,
        'content': content,
    }

    return render(request, template, context)


def buy_game_page(request, game_title):
    """ A view to purchase a game and
    review its contents """

    game = get_object_or_404(Game, url_name=game_title)
    editions = Edition.objects.filter(game=game)
    sections = Section.objects.filter(game=game)
    content = Content.objects.filter(game=game)

    template = 'games/buy-game.html'
    context = {
        'game': game,
        'editions': editions,
        'sections': sections,
        'content': content,
    }

    return render(request, template, context)
