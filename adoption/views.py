from django.shortcuts import get_object_or_404, render
from .models import Adoption, Package


def all_adoptions(request):
    """ A view to render all adoption packs
    available to view and/or purchase """

    adoptions = Adoption.objects.all()

    template = 'adoption/adoptions.html'
    context = {
        'adoptions': adoptions,
    }

    return render(request, template, context)


def adoption_package(request, animal):
    """ A view to purchase an adoption package """

    animal = get_object_or_404(Adoption, animal=animal)
    packages = Package.objects.all()

    template = 'adoption/adoption-packages.html'
    context = {
        'animal': animal,
        'packages': packages,
    }

    return render(request, template, context)
