from django.shortcuts import render
from .models import Adoption


def all_adoptions(request):
    """ A view to render all adoption packs
    available to view and/or purchase """

    adoptions = Adoption.objects.all()

    template = 'adoption/adoptions.html'
    context = {
        'adoptions': adoptions,
    }

    return render(request, template, context)
