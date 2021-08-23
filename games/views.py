from django.shortcuts import render


def all_games(request):
    """ A view to render all games available for purchase """

    return render(request, 'games/games.html')
