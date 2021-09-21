from django.shortcuts import render
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    """ A view to render the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
